# -*-coding:utf-8 -*-

# File       : getRule.py
# Time       ：2022/4/5 18:23
# Author     ：BEE2E7
# Description：

from scipy import sparse
import pandas as pd
import numpy as np
import datetime
from collections import defaultdict
import operator

global rule_features,rule_thresholds,rule_symbols,rule_values,rule_sample,rule_predict,rule_index_t,sorted_features #规则特征 规则阈值 规则符号 规则返回值 规则样本数目 规则预测值 规则索引表 规则特征排序表
global rule_amount,rule_pool_size,all_rule_amount,same_rule_amount,useless_rule_amount,sorted_length,gini_zero_amount #当前规则数目 规则池大小 供选择规则总数目 重复规则数目 作废规则数目 规则排序特征表长度 gini=0规则数目
global samples_not_enough, feature_offset, view_id
global cover_rule_amount, all_rules_predict, rule_coverage, rule_accuracy, rule_realsample  #重合的删去的规则数量  规则判断样本的集合 每一条规则的覆盖率 每一条规则的准确率 每一条规则的正确预测样本数量


global ruledict, rules_list, all_features_num #规则字典 item列表,使用的特征数
global RMatrix_1, RMatrix_0, ruleslist, rule1_list, rule0_list
global experiment_amount

RULE_SAMPLE=3
#删除在索引表中位置为pos的规则，主要是处理特征排序表和规则索引表，因为规则内容表中的内容会被新内容替换
#传入：pos 规则在索引表中的位置
#返回：空
def rule_delete(pos):
    global rule_index_t

    sorted_id = rule_index_t[pos][2]  # 获取特征在排序列表中的位置
    sorted_index=(int)(sorted_id-1) #获取排序特征id

    index_list = [i for i, item in enumerate(rule_index_t) if item[2] == sorted_id]  # 查找使用相同特征的规则在索引表中的位置
    #根据规则特征出现次数，采取不同的策略删除特征排序列表中的内容
    if len(index_list)==1: #该组特征只在规则池中出现一次，则可以直接删除
        sorted_index=int(sorted_index)
        sorted_features[sorted_index]=[-1,-1]
    else: #该组特征在规则池中多次出现，不能直接删除，需修改索引表中所有对应表项数值

        for index in index_list:
            rule_index_t[index][3] = rule_index_t[index][3] - 1

    return

#当规则特征重复的情况下，查看规则池中是否有重复规则
#传入：path_features 规则特征、path_thresholds规则阈值、path_symbols规则符号、sorted_index规则特征在排序列表中的索引
#返回：is_same 规则是否相同、times当前特征在规则池中出现次数
def rule_equal(path_features,path_thresholds,path_symbols,sorted_index):

    global rule_features,rule_thresholds,rule_symbols,rule_index_t,sorted_features

    is_same=True
    sorted_f=sorted_features[sorted_index] #特征排序后序列
    sorted_id=sorted_index+1 #排序表中的特征id

    index_list = [i for i, item in enumerate(rule_index_t) if item[2] == sorted_id]  # 查找使用相同特征的规则在索引表中的位置


    #遍历所有使用相同特征的规则，查看规则内容是否相同
    for i in range(len(index_list)):
        is_same=True
        index=index_list[i]

        pos = int(rule_index_t[index][1])  # 获得规则在规则内容列表的位置
        other_features,other_thresholds,other_symbols,other_predict=rule_features[pos],rule_thresholds[pos],rule_symbols[pos],rule_predict[pos] #获取规则内容

        for j in range(len(sorted_f)): #逐特征比较规则内容
            f=sorted_f[j]
            x1=path_features.index(f)
            x2=other_features.index(f)
            if path_thresholds[x1]!=other_thresholds[x2] or path_symbols[x1]!=other_symbols[x2]:
                is_same = False
                break
        if is_same == True: #规则重复

            break

    if is_same==False: #规则特征重复，但规则内容不重复，修改索引表中规则特征出现次数
        for index in index_list:
            rule_index_t[index][3] += 1

    return is_same, rule_index_t[index_list[0]][3]  # 规则是否相同、规则特征重复次数

#比较规则的重合度，去除掉重合程度较高的规则
def rule_iscover(path_features, path_thresholds, path_symbols,path_predict):
    global cover_rule_amount, all_rules_predict, x_train, y_train, rule_amount
    is_cover = False
    #记录当前规则对于所有样本的预测结果
    result = []
    is_leaf = False
    for i in range(x_train.shape[0]):
        x = x_train.iloc[[i]]
        for index in range(len(path_features)):
            if path_symbols[index] == 1: #" <= "
                if operator.le(x[str(path_features[index]+feature_offset)].values, path_thresholds[index]):
                    is_leaf = True
                    continue
                else:
                    is_leaf = False
                    break
            else:   #" > "
                if operator.gt(x[str(path_features[index]+feature_offset)].values, path_thresholds[index]):
                    is_leaf = True
                    continue
                else:
                    is_leaf = False
                    break
        #如果运行到最后一步 index增加但是break 其实不属于predict————添加is_leaf进行判断
        if (index == (len(path_features)-1)) and (is_leaf == True):
            y_hat = path_predict
        else:
            y_hat = -1 
        result.append(y_hat)

    tp_cover, tn_cover = [0], [0]
    #新添加进来的规则 与已经纳入规则集中的每一条规则比较计算出覆盖率
    for rule_index in range(rule_amount):
        Y_tp_index = np.intersect1d(np.where(np.array(all_rules_predict[rule_index]) == 1)[0], np.where(np.array(y_train) == 1)[0]) #每一条规则预测结果和实际样本
        Y_tn_index = np.intersect1d(np.where(np.array(all_rules_predict[rule_index]) == 0)[0], np.where(np.array(y_train) == 0)[0])
        add_Y_tp_index = np.intersect1d(np.where(np.array(result) == 1)[0], np.where(np.array(y_train) == 1)[0]) #正样本重合数
        add_Y_tn_index = np.intersect1d(np.where(np.array(result) == 0)[0], np.where(np.array(y_train) == 0)[0]) #负样本重合数
        tp_cover.append(np.intersect1d(add_Y_tp_index,Y_tp_index).size / (Y_tp_index.size+1)) 
        tn_cover.append(np.intersect1d(add_Y_tn_index,Y_tn_index).size / (Y_tn_index.size+1))

    if (max(tp_cover)>0.90) or (max(tn_cover)>0.90):
        is_cover = True
        cover_rule_amount += 1    
    return is_cover

#一条规则来判断样本是否为正、负 或者是-1
def one_rule_predict(rule_index):
    global rule_features,rule_thresholds,rule_symbols,rule_predict, feature_offset, view_id, y_train
   
    import operator
    y_hat = []
    is_leaf = False
    features,thresholds,symbols,predict=rule_features[rule_index],rule_thresholds[rule_index],rule_symbols[rule_index],rule_predict[rule_index] #规则内容
    for i in range(x_train.shape[0]):
        x = x_train.iloc[[i]]
        for index in range(len(features)):
            if symbols[index] == 1: #" <= "
                if operator.le(x[str(features[index]+feature_offset)].values, thresholds[index]):
                    is_leaf = True
                    continue
                else:
                    is_leaf = False
                    break
            else:   #" > "
                if operator.gt(x[str(features[index]+feature_offset)].values, thresholds[index]):
                    is_leaf = True
                    continue
                else:
                    is_leaf = False
                    break

        if (index == (len(features)-1)) and (is_leaf == True):
            y_hat.append(predict)
        else:
            y_hat.append(-1)

    y_train_tp = sum(np.array(y_train))
    y_train_tn = np.array(y_train).size - y_train_tp
    if predict == 1: #为正
        Y_tp_index = np.intersect1d(np.where(np.array(y_hat) == 1)[0], np.where(np.array(y_train) == 1)[0])
        rule_accuracy = len(Y_tp_index) / len(np.where(np.array(y_hat) == 1)[0])
        rule_coverage = len(Y_tp_index) / y_train_tp
        return y_hat, rule_coverage, rule_accuracy, len(Y_tp_index)
    else:   #为负
        Y_tn_index = np.intersect1d(np.where(np.array(y_hat) == 0)[0], np.where(np.array(y_train) == 0)[0])
        rule_accuracy = len(Y_tn_index) / len(np.where(np.array(y_hat) == 0)[0])
        rule_coverage = len(Y_tn_index) / y_train_tn
        return y_hat, rule_coverage, rule_accuracy, len(Y_tn_index)


#将规则特征按序号降序进行排序
#传入：规则特征列表
#返回：排序后的规则特征列表
def feature_sort(path_features):
    sorted_features=[]

    for i in range(len(path_features)):
        max_f=max(path_features)
        max_index=path_features.index(max_f)
        sorted_features.append(max_f)
        path_features[max_index]=-1

    return sorted_features

#获取规则内容
#传入：tree 决策树、path 规则路径
#返回：path_features 规则特征、path_thresholds 特征阈值、path_symbols 规则符号、path_predict 规则返回值、path_sample 规则样本
def get_rule_content(tree,path):
    #从决策树中获取所需结构
    children_left=tree.tree_.children_left #节点x的左孩子，如果x是叶子节点，则左孩子为-1
    children_right=tree.tree_.children_right #节点x的右孩子，如果x是叶子节点，则右孩子为-1
    features=tree.tree_.feature #节点所用特征
    thresholds=tree.tree_.threshold #节点特征阈值
    values=tree.tree_.value #节点的值
    samples=tree.tree_.n_node_samples #节点的样本数目

    path_features,path_thresholds,path_symbols,path_values=[],[],[],[] #当前路径对应内容
    path_predict=0

    #遍历路径中的节点，但不包括叶子节点
    for index in range(len(path)-1):
        node_index=path[index] #获取当前节点在决策树中的索引
        next_index=path[index+1] #获取下一个节点的索引
        if children_left[node_index]==next_index: #下一个节点是当前节点的左孩子，即当前特征值判定符号为<=，用1表示
            path_symbols.append(1)
        elif children_right[node_index]==next_index: #下一个节点是当前节点的右孩子，即当前特征值判定符号为>，用2表示
            path_symbols.append(2)

        path_features.append(features[node_index])
        path_thresholds.append(thresholds[node_index])

    #根据叶子节点判断规则输出值
    index+=1
    node_index=path[index]
    value1,value2=values[node_index][0][0],values[node_index][0][1]
    if value1>value2: #规则返回值为0
        path_predict=0
    elif value1<value2: #规则返回值为1
        path_predict=1
    else: #value1等于value2 即gini=0.5 返回-1 此规则作废
        path_predict=-1

    path_values.append(value1)
    path_values.append(value2)

    path_sample=samples[node_index]
    return path_features,path_thresholds,path_symbols,path_values,path_sample,path_predict


#当前规则与规则池中规则进行比较，判断是否将当前规则加入规则池
#传入：k 规则gini系数/样本函数、tree 决策树、path规则路径
#返回：空
def rules_compare(k, path_features, path_thresholds, path_symbols,path_values,path_predict, path_sample):

    global rule_features,rule_thresholds,rule_symbols,rule_predict,rule_index_t,sorted_features,rule_sample,rule_values
    global rule_amount,rule_pool_size,same_rule_amount,useless_rule_amount,sorted_length
    global x_train, y_train


    if path_predict==-1: #规则作废
        useless_rule_amount+=1
        return
    
    is_cover = rule_iscover(path_features, path_thresholds, path_symbols,path_predict)
    if is_cover == False:
        if rule_amount<rule_pool_size: #规则池未满
            # 规则池未满，查找是否有相同规则
            sorted_f = feature_sort(path_features.copy())  # 将规则特征按从大到小的顺序进行排序
            if sorted_f in sorted_features:  # 规则所使用特征重复，需判断规则整体是否重复

                sorted_index = sorted_features.index(sorted_f)  # 获得特征有序序列在表中的位置

                is_same, times = rule_equal(path_features, path_thresholds, path_symbols,  sorted_index)
                if is_same == True:  # 规则重复
                    same_rule_amount += 1
                    return
                else:  # 规则特征相同，但规则不重复
                    rule_index_t.append([k, rule_amount, sorted_index + 1, times])
                    rule_features.append(path_features)  # 规则特征
                    rule_thresholds.append(path_thresholds)  # 规则阈值
                    rule_symbols.append(path_symbols)  # 规则符号
                    rule_values.append(path_values) #规则返回值
                    rule_predict.append(path_predict)  # 规则返回值                
                    rule_sample.append(path_sample)
                    predict, cover, acc, realsample = one_rule_predict(rule_amount)
                    all_rules_predict.append(predict)
                    rule_coverage.append(cover)   
                    rule_accuracy.append(acc) 
                    rule_realsample.append(realsample)
                    rule_amount += 1

            else:  # 规则特征不重复
                rule_index_t.append([k, rule_amount, sorted_length + 1, 1])
                rule_features.append(path_features)  # 规则特征
                rule_thresholds.append(path_thresholds)  # 规则阈值
                rule_symbols.append(path_symbols)  # 规则符号
                rule_values.append(path_values)  # 规则返回值
                rule_predict.append(path_predict)  # 规则返回值
                rule_sample.append(path_sample) #规则样本数
                predict, cover, acc, realsample = one_rule_predict(rule_amount)
                all_rules_predict.append(predict)
                rule_coverage.append(cover)   
                rule_accuracy.append(acc) 
                rule_realsample.append(realsample)
                sorted_features.append(sorted_f)  # 规则特征排序序列
                rule_amount += 1  # 当前规则数目+1
                sorted_length += 1  # 当前规则特征排序序列+1

        else: #规则池满了
            pos=rule_amount-1

            rule_index_t=np.array(rule_index_t)
            rule_index_t = rule_index_t[np.lexsort(-rule_index_t[:, ::-1].T)]  # 按照表项第一个值gini/samples升序排序


            worst_k, worst_index, worst_sorted_index, worst_times = rule_index_t[pos][0], rule_index_t[pos][1], \
                                                                    rule_index_t[pos][2], rule_index_t[pos][3]  # 获取最差规则的索引表项

            if k>worst_k: #当前规则有资格进行替换

                sorted_f = feature_sort(path_features.copy())  # 将规则特征按从大到小的顺序进行排序

                if sorted_f in sorted_features:  # 规则所使用特征重复，需判断规则整体是否重复

                    sorted_index = sorted_features.index(sorted_f)  # 获得特征有序序列在表中的位置
                    is_same, times = rule_equal(path_features, path_thresholds, path_symbols, sorted_index) #判断规则内容是否重复，若规则内容重复，则修改规则索引表
                    if is_same==True: #规则内容重复，无需进行替换
                        same_rule_amount+=1
                        return
                    else: #规则特征重复 但规则内容未重复，需要进行替换

                        rule_delete(pos) #删除索引表中位置为pos的规则
                        rule_index_t[pos][0], rule_index_t[pos][2], rule_index_t[pos][3] = \
                            k, sorted_index + 1, times  # 用新规则的信息替换淘汰规则的信息 ginni/samples 特征排序位置 特征重复次数
                        rule_index = int(rule_index_t[pos][1])  # 获取被淘汰规则在内容列表中的位置
                        rule_features[rule_index]=path_features #替换规则特征
                        rule_thresholds[rule_index]=path_thresholds #替换特征阈值
                        rule_symbols[rule_index]=path_symbols #替换特征符号
                        rule_values[rule_index]=path_values
                        rule_predict[rule_index]=path_predict #替换规则返回值
                        rule_sample[rule_index]=path_sample
                        all_rules_predict[rule_index], rule_coverage[rule_index], rule_accuracy[rule_index], rule_realsample[rule_index]=one_rule_predict(rule_index)
                else: #规则使用的特征组从未在规则池中出现              
                    rule_delete(pos) #删除被淘汰规则
                    rule_index_t[pos][0], rule_index_t[pos][2], rule_index_t[pos][3] = k, sorted_length + 1, 1
                    rule_index = int(rule_index_t[pos][1])  # 获取淘汰规则在规则内容列表中的位置
                    rule_features[rule_index]=path_features #替换规则特征
                    rule_thresholds[rule_index]=path_thresholds #替换规则阈值
                    rule_symbols[rule_index]=path_symbols #替换规则符号
                    rule_predict[rule_index]=path_predict #替换规则预测值
                    rule_sample[rule_index]=path_sample #替换规则样本数目
                    rule_values[rule_index]=path_values #替换规则返回值
                    sorted_features.append(sorted_f) #写入排序特征
                    sorted_length+=1 #排序规则数目+1
                    all_rules_predict[rule_index], rule_coverage[rule_index], rule_accuracy[rule_index], rule_realsample[rule_index]=one_rule_predict(rule_index)
    return


#递归获得当前决策树中的路径 并将获得的规则传入规则比较函数
#传入：tree决策树、path 路径、length 当前路径长度、node_index 当前节点在树中的索引
#返回：空
def get_tree_paths(tree,path,length,node_index):
    global all_rule_amount,gini_zero_amount #所有规则数目 作废规则数目
    global samples_not_enough #gini=0 sample<11的规则数目

    children_left=tree.tree_.children_left[node_index] #节点node_index的左孩子，若左孩子为-1，则当前节点为叶子节点
    children_right=tree.tree_.children_right[node_index] #节点node_index的右孩子，若右孩子为-1，则当前节点为叶子节点
    impurity=tree.tree_.impurity[node_index] #节点node_index的gini系数

    path.append(node_index) #将当前节点压入路径path中

    if children_left==-1: #node_index为叶子节点，即当前规则已经遍历到尽头
        path_features, path_thresholds, path_symbols, path_values, path_sample, path_predict = get_rule_content(tree,path)

        if impurity==0:
            gini_zero_amount+=1
            if path_sample<RULE_SAMPLE:
                samples_not_enough+=1

        all_rule_amount+=1 #规则总数+1
        if path_sample>=RULE_SAMPLE:
            k = (float)(abs(path_values[0] - path_values[1])) / path_sample + (float)(path_sample) / 100
            rules_compare(k, path_features, path_thresholds, path_symbols,path_values,path_predict, path_sample)  # 将当前规则与规则池中的规则进行比较
    else: #当前节点为非叶子节点
        get_tree_paths(tree,path,length+1,children_left)
        get_tree_paths(tree,path,length+1,children_right)

    path.pop(length) #将当前节点
    return

#将规则以函数形式写入py文件中
#传入：空 （因为数据都在全局变量中）
#返回：空
def write_rules( ):
    global rule_features,rule_thresholds,rule_symbols,rule_predict, feature_offset, view_id
    global experiment_amount
    front_path="./ruleInformation/view"+str(view_id)
    py_f=open(front_path + "/rules"+str(view_id)+"_"+str(experiment_amount)+".py","w")
    for rule_index in range(rule_amount): #遍历所有规则
        py_f.write("def rule" + str(rule_index) + "(X):\n")  # 函数名
        features,thresholds,symbols,predict=rule_features[rule_index],rule_thresholds[rule_index],rule_symbols[rule_index],rule_predict[rule_index] #规则内容

        for index in range(len(features)):
            py_f.write("{space}"
                       "if X['{feature}'].values"
                .format(
                space=(index + 1) * "    ",
                feature=features[index]+feature_offset))
            if symbols[index] == 1:
                py_f.write(" <= ")
            else:
                py_f.write(" > ")

            py_f.write("{threshold} :"
                       "\n".format(
                threshold=thresholds[index]))
        index += 1
        py_f.write("{space}"
                   "return {v}"
                   "\n".format(
            space=(index + 1) * "    ",
            v=predict))

        while index > 0:
            py_f.write("{space}"
                       "else:"
                       "\n"
                       "{space2}"
                       "return -1"
                       "\n".format(
                space=(index) * "    ",
                space2=(index + 1) * "    "))
            index -= 1
    py_f.close()
    return

def write_xcolumns( ):
    global rule_features,rule_thresholds,rule_symbols,rule_predict, feature_offset, view_id
    global ruledict, rules_list, all_features_num
    
    #字典里存放的是 规则 以及规则对应的阈值和符号
    ruledict = defaultdict(list)

    for rule_index in range(rule_amount): #遍历所有规则  
        features,thresholds,symbols,predict=rule_features[rule_index],rule_thresholds[rule_index],rule_symbols[rule_index],rule_predict[rule_index] #规则内容
        for index in range(len(features)):
            is_fsame =  True  #判断一个规则的item是否相同
            for i in ruledict[features[index]+feature_offset]:
                if (i[0] == thresholds[index]) and (i[1] == symbols[index]):
                    is_fsame = False
            if is_fsame:
                ruledict[features[index]+feature_offset].append([thresholds[index],symbols[index]])
    
    all_features  = sorted(ruledict.keys())
    all_features_num = len(all_features) 
    rules_list = []
    py=open("./ruleInformation/view"+str(view_id)+"/"+str(experiment_amount)+"_v"+str(view_id)+"_xcolumns.txt","w")
    for i in all_features:
        for j in ruledict[i]:
            if j[1] == 1:
                sym = " <= "
                py.write(str(i) + sym + str(j[0]) + "\n")
                rules_list.append(str(i) + sym + str(j[0]))
            else:
                sym = " > "
                py.write(str(i) + sym + str(j[0]) + "\n")
                rules_list.append(str(i) + sym + str(j[0]))
    return

#处理数据集 连续特征离散化
def transform(x, neg=True):
    global ruledict, rules_list
    all_features  =  sorted(ruledict.keys()) #选取的规则中使用的特征
    df = x.loc[:, [str(i) for i in all_features]]

    df_cat = df.loc[:, (df.dtypes == object) ^ (df.dtypes == 'bool')]
    df_num = df.loc[:, (df.dtypes == 'float64') ^ (df.dtypes == 'int64')]
    # df_cat = df.loc[:, df.dtypes == 'int64']
    # df_num = df.loc[:, df.dtypes == 'float64']
    
    df_cat_columns = df_cat.columns
    for col in df_cat_columns:
        items = np.unique(df_cat[col])  #特征值按照从小到大排列
        if len(items) == 2:  #只有两种取值
            for item in items:   # eg:一列扩展为性别_男//性别_女——两列  true false              
                df_cat[col + '&' + str(item)] = df_cat[col] <= 0.5  # 为1或者0
        else:  # 有多种属性值
            for item in items:
                df_cat[col + '&' + str(item)] = df_cat[col] == item
                if neg:                # 多了一列neg(相反列)?
                    df_cat[col + '&' + str(item) + '&neg'] = df_cat[col] != item
        df_cat.drop(col, axis=1, inplace=True)  # 删除之前存在的列

    df_num_columns = df_num.columns
    for col in df_num_columns:
        cuts = [i[0] for i in ruledict[int(col)]]
        syms = [i[1] for i in ruledict[int(col)]]
        if len(cuts) == 0:
            df_num.drop(col, axis=1, inplace=True)
            continue
        for i in range(len(cuts)):
            if syms[i] == 1:
                sym = " <= "
                df_num[col + sym + str(cuts[i])] = df_num[col] <= cuts[i]
            else:
                sym = " > "
                df_num[col + sym + str(cuts[i])] = df_num[col] > cuts[i]
            
        df_num.drop(col, axis=1, inplace=True)  # 删除列，因为已经生成了新的列所以要删除
    df  = pd.concat([df_cat, df_num], axis=1) # 连接起来
    df.to_csv("./ruleInformation/view"+str(view_id)+"/"+str(experiment_amount)+"_v"+str(view_id)+"_xtrans.csv",index=False,sep=',',encoding='utf_8')
    return df  

#建立规则矩阵
def screen_rules(xtrans):
    global ruledict, RMatrix, RMatrix_1, RMatrix_0, ruleslist, rule1_list, rule0_list, feature_offset
    ruleMatrix = np.zeros((len(rule_features), len(xtrans.columns)), dtype=int)
    ruleMatrix_0 = np.zeros((len(rule_features), len(xtrans.columns)), dtype=int)
    ruleMatrix_1 = np.zeros((len(rule_features), len(xtrans.columns)), dtype=int)
    columns = xtrans.columns.to_list()
    tmp_rules_len = [len(rule) for rule in rule_features]
    ruleslist= [0 for x in range (len(rule_features))]
    rule1_list, rule0_list = [],[] #规则列表 包含特征索引
    for i, rule in enumerate(rule_features):
        rules, rule1, rule0 = [],[], []
        for j in range(len(rule)):
            if rule_symbols[i][j] == 1:
                sym = " <= "
            else:
                sym = " > "
            pre_rule = str(rule_features[i][j] + feature_offset) + sym + str(rule_thresholds[i][j])
            index = columns.index(pre_rule)
            rules.append(index)
            ruleMatrix[i][index] = 1
            #建立正、负规则矩阵
            if rule_predict[i] == 1:
                ruleMatrix_1[i][index] = 1
                rule1.append(index)
            else:
                ruleMatrix_0[i][index] = 1
                rule0.append(index)

        ruleslist[i] = rules
        rule1_list.append(rule1)
        rule0_list.append(rule0)
    rule1_list = [x for x in rule1_list if x != []]
    rule0_list = [x for x in rule0_list if x != []]
    ruleMatrix = sparse.csc_matrix(ruleMatrix.transpose())
    ruleMatrix_1 = sparse.csc_matrix(ruleMatrix_1.transpose())
    ruleMatrix_0 = sparse.csc_matrix(ruleMatrix_0.transpose())
    mat = (sparse.csc_matrix(xtrans) * ruleMatrix).todense()
    mat_1 = (sparse.csc_matrix(xtrans) * ruleMatrix_1).todense()
    mat_0 = (sparse.csc_matrix(xtrans) * ruleMatrix_0).todense()
    RMatrix_1 = (mat_1 == tmp_rules_len)
    RMatrix_0 = (mat_0 == tmp_rules_len)
    RMatrix = (mat == tmp_rules_len)
    return

# 从随机森林中抽取规则
# 传入: forest 随机森林、forest_size 森林规模、expect_amount 期望规则数目、view_id 视角编号、depth 深度、experiment_id 实验编号、f_offset特征偏移量、r_offset规则偏移量
# 返回:
def get_rule(x_train_df, y_train_df, forest,forest_size,expect_amount,v_id,f_offset, ex_amount):
    global rule_features, rule_thresholds, rule_symbols, rule_values, rule_sample, rule_predict, rule_index_t, sorted_features  # 规则特征 规则阈值 规则符号 规则返回值 规则样本数目 规则预测值 规则索引表 规则特征排序表
    global rule_amount, rule_pool_size, all_rule_amount, same_rule_amount, useless_rule_amount, sorted_length, gini_zero_amount  # 当前规则数目 规则池大小 供选择规则总数目 重复规则数目 作废规则数目 规则排序特征表长度 gini=0规则数目
    global cover_rule_amount, all_rules_predict, rule_coverage, rule_accuracy, rule_realsample
    global samples_not_enough, feature_offset, view_id  # gini=0 但samples不满足要求的规则
    global x_train, y_train
    global experiment_amount

    experiment_amount = ex_amount
    rule_features, rule_thresholds, rule_symbols, rule_values, rule_sample, rule_predict, sorted_features = [], [], [], [], [], [], []
    rule_amount, all_rule_amount, same_rule_amount, useless_rule_amount, sorted_length, gini_zero_amount, cover_rule_amount = 0, 0, 0, 0, 0, 0, 0
    rule_pool_size = expect_amount  # 规则池大小=期望的规则数目

    x_train, y_train = x_train_df, y_train_df
    all_rules_predict, rule_coverage, rule_accuracy, rule_realsample = [], [], [], []
    rule_index_t=[]  # 规则索引表，依次存放：规则权重abs(value1-value2)/sample、规则在各表中位置rule_index、规则在特征排序表中位置sorted_index、规则排序特征出现次数times

    samples_not_enough = 0
    feature_offset = f_offset
    view_id = v_id

    for tree_index in range(forest_size):
        path = []
        get_tree_paths(forest[tree_index], path, 0, 0)  # 获取树的路径

    #将规则内容保存到csv文件中，以便后续查看
    features_df=pd.DataFrame(rule_features) #规则特征list转DataFrame
    thresholds_df=pd.DataFrame(rule_thresholds) #规则阈值
    symbols_df=pd.DataFrame(rule_symbols) #规则符号
    values_df=pd.DataFrame(rule_values) #规则返回值

    r_max_len=features_df.shape[1] #阈值df的列数即为规则最大长度
    f_col,t_col,s_col=[],[],[]
    for i in range(r_max_len):
        f_col.append("fea_"+str(i+1))
        t_col.append("thre_"+str(i+1))
        s_col.append("sym_"+str(i+1))
    v_col=["v1","v2"]
    features_df.columns=f_col
    thresholds_df.columns=t_col
    symbols_df.columns=s_col
    values_df.columns=v_col

    rule_len=[]
    for feature in rule_features:
        rule_len.append(len(feature))

    df=pd.concat([features_df,thresholds_df],axis=1)
    df=pd.concat([df,symbols_df],axis=1)
    df=pd.concat([df,values_df],axis=1)
    df['sample']=rule_sample #规则样本数目
    df['predict']=rule_predict #规则预测值
    df['len']=rule_len #规则长度 用于最后可解释性
    df['coverage']=rule_coverage #规则覆盖度
    df['accuracy']=rule_accuracy
    df['realsample']=rule_realsample

    front_path1="./ruleInformation/view"+str(view_id)+"/"+str(experiment_amount)+"_v"+str(view_id)+"_"
    df.to_csv(front_path1+"rule.csv",index=False,sep=',',encoding="utf_8") #保存到csv文件中

    df2=pd.DataFrame(rule_index_t)
    front_path2="./ruleIndex/"+str(experiment_amount)+"_v"+str(view_id)+"_"
    df2.to_csv(front_path2+"rule_index_table.csv",index=False,sep=',',encoding='utf_8')

    #将规则以函数形式保存在python文件中
    write_rules( )
    write_xcolumns( )
    print("expect_amount ",expect_amount)
    print("all_rule_amount ", all_rule_amount)
    print("rule_amount", rule_amount)
    print("same_rule_amount", same_rule_amount)
    print("useless_rule_amount", useless_rule_amount)
    print("gini_zero", gini_zero_amount)
    print("samples not enough ", samples_not_enough)
    print("all features num", all_features_num)
    print("cover rule amount", cover_rule_amount)
    print(len(rules_list))
    print("\n")

    xtrans = transform(x_train_df)
    screen_rules(xtrans)

    ruleslist_df=pd.DataFrame(ruleslist)
    ruleslist_df['predict']=rule_predict
    ruleslist_df.to_csv(front_path1+"rulelist.csv",index=False,sep=',',encoding="utf_8") #保存到csv文件中
    pd.DataFrame(RMatrix).to_csv(front_path1+"RMatrix.csv",index=False,sep=',',encoding="utf_8") #保存到csv文件中
    pd.DataFrame(RMatrix_0).to_csv(front_path1+"RMatrix_0.csv",index=False,sep=',',encoding="utf_8") #保存到csv文件中
    pd.DataFrame(RMatrix_1).to_csv(front_path1+"RMatrix_1.csv",index=False,sep=',',encoding="utf_8") #保存到csv文件中
    pd.DataFrame(rule0_list).to_csv(front_path1+"rulelist_0.csv",index=False,sep=',',encoding="utf_8") #保存到csv文件中
    pd.DataFrame(rule1_list).to_csv(front_path1+"rulelist_1.csv",index=False,sep=',',encoding="utf_8") #保存到csv文件中

    #存一个txt文件
    # rule_amount 筛选出的规则数目、all_rule_amount 总规则数目、gini_zero_amount gini=0规则、
    # sample_not_enough gini=0但样本数小于阈值的股则、same_rule_amount相同规则、useless_rule_amount 作废规则
    now_time = datetime.datetime.now()
    time_str = datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
    with open("./ruleInformation/ruleAmount.txt", "a+") as f:
        f.write(time_str+"view"+str(view_id)+"---"+str(experiment_amount)+"\n")
        f.write("expect_amount"+str(expect_amount)+"\n")
        f.write("all_rule_amount "+str(all_rule_amount)+"\n")
        f.write("rule_amount"+str(rule_amount)+"\n")
        f.write("same_rule_amount"+str(same_rule_amount)+"\n")
        f.write("useless_rule_amount"+str(useless_rule_amount)+"\n")
        f.write("gini_zero"+str(gini_zero_amount)+"\n")
        f.write("samples not enough "+str(samples_not_enough)+"\n")
        f.write("all features num"+str(all_features_num)+"\n")
        f.write("cover rule amount"+str(cover_rule_amount)+"\n")
    f.close()

    return rule_amount