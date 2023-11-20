import view.viewCenter as viewCenter

from sklearn.metrics import classification_report,roc_auc_score,average_precision_score
import pandas as pd
from ruleInformation.view0 import rules0_1, rules0_2, rules0_3, rules0_4, rules0_5
from ruleInformation.view1 import rules1_1, rules1_2, rules1_3, rules1_4, rules1_5
from ruleInformation.view2 import rules2_1, rules2_2, rules2_3, rules2_4, rules2_5
from ruleInformation.view3 import rules3_1, rules3_2, rules3_3, rules3_4, rules3_5
import rulesets.csvRecord as csvRecord

global x_test, y_test
global rule_amount_list, offset_list, view_amount, ind_length
global experiment_amount

#遍历规则集，对某一样本进行预测
def f(ind,sample_index,rules_info_l, v_list):
    global x_test, y_test
    global offset_list,view_amount
    global experiment_amount
    
    #四视角结果统计
    view_toxics, view_non_toxics = [0, 0, 0, 0], [0, 0, 0, 0]  # 各视角有毒、无毒预测情况\覆盖该样本的规则数
    toxic_rules_acc, non_toxic_rules_acc = [0,0,0,0], [0,0,0,0] # 各视角 规则的平均accuracy

    # 从对应数据文件中取出样本
    x = x_test.iloc[[sample_index]]
    sample_label = y_test[sample_index]

    #遍历view1中规则
    for rule_index in range(offset_list[0],offset_list[1]):
        if ind[rule_index]==1:
            rule_f = "rules0_"+str(experiment_amount)+".rule" + str(rule_index)
            toxic_result = eval(rule_f)(x)

            if toxic_result==1: #当前规则认为有毒
                view_toxics[0]+=1
                toxic_rules_acc[0]+=rules_info_l[0][rule_index][0][0]
            elif toxic_result==0: #当前规则认为无毒
                view_non_toxics[0]+=1
                non_toxic_rules_acc[0]+=rules_info_l[0][rule_index][0][0]
    if view_toxics[0] != 0:
        toxic_rules_acc[0] = toxic_rules_acc[0] / view_toxics[0]
    if view_non_toxics[0] != 0:
        non_toxic_rules_acc[0] = non_toxic_rules_acc[0] / view_non_toxics[0] + 1


    #视角2
    for rule_index in range(offset_list[1],offset_list[2]):
        if ind[rule_index]==1:
            rule_f = "rules1_"+str(experiment_amount)+".rule" + str(rule_index-offset_list[1])
            toxic_result = eval(rule_f)(x)

            if toxic_result==1: #认为有毒
                view_toxics[1] += 1
                toxic_rules_acc[1]+=rules_info_l[1][rule_index][0][0]
            elif toxic_result==0: #认为无毒
                view_non_toxics[1] += 1
                non_toxic_rules_acc[1]+=rules_info_l[1][rule_index][0][0]
    if view_toxics[1] != 0:
        toxic_rules_acc[1] = toxic_rules_acc[1] / view_toxics[1]
    if view_non_toxics[1] != 0:
        non_toxic_rules_acc[1] = non_toxic_rules_acc[1] / view_non_toxics[1]

    #视角3
    for rule_index in range(offset_list[2],offset_list[3]):
        if ind[rule_index]==1:
            rule_f = "rules2_"+str(experiment_amount)+".rule" + str(rule_index-offset_list[2])
            toxic_result = eval(rule_f)(x)

            if toxic_result == 1:  # 认为有毒
                view_toxics[2] += 1
                toxic_rules_acc[2]+=rules_info_l[2][rule_index][0][0]
            elif toxic_result == 0:  # 认为无毒
                view_non_toxics[2] += 1
                non_toxic_rules_acc[2]+=rules_info_l[2][rule_index][0][0]
    if view_toxics[2] != 0:
        toxic_rules_acc[2] = toxic_rules_acc[2] / view_toxics[2]
    if view_non_toxics[2] != 0:
        non_toxic_rules_acc[2] = non_toxic_rules_acc[2] / view_non_toxics[2]

    #视角4
    for rule_index in range(offset_list[3],offset_list[4]):
        if ind[rule_index]==1:
            rule_f = "rules3_"+str(experiment_amount)+".rule" + str(rule_index-offset_list[3])
            toxic_result = eval(rule_f)(x)

            if toxic_result == 1:  # 认为有毒
                view_toxics[3] += 1
                toxic_rules_acc[3]+=rules_info_l[3][rule_index][0][0]
            elif toxic_result == 0:  # 认为无毒
                view_non_toxics[3] += 1
                non_toxic_rules_acc[3]+=rules_info_l[3][rule_index][0][0]
    if view_toxics[3] != 0:
        toxic_rules_acc[3] = toxic_rules_acc[3] / view_toxics[3]
    if view_non_toxics[3] != 0:
        non_toxic_rules_acc[3] = non_toxic_rules_acc[3] / view_non_toxics[3]

    #计算各视角预测结果 单个视角上 只信任非平局结果 对于平局结果不予考虑
    view_predicts = [-1, -1, -1, -1]  # 各视角的预测值
    toxic_list, non_toxic_list = [], []  # 认为有毒和无毒的视角列表
    view_weight = [0,0,0,0]  # 考虑权重 view在所有view的规则中覆盖该样本的比例
    dogfall_list=[] #平局视角
    for v in range(view_amount):
        if view_toxics[v]>view_non_toxics[v]: #认为有毒>无毒
            view_predicts[v]=1
            toxic_list.append(v) #将视角id记入list
        elif view_toxics[v]<view_non_toxics[v]: #认为有毒<无毒
            view_predicts[v]=0
            non_toxic_list.append(v)
        elif view_toxics[v]!=0: #平局，但非不覆盖, 在一个view上平局
            dogfall_list.append(v) #平局但非
        view_weight[v] = abs(view_toxics[v] * toxic_rules_acc[v] - view_non_toxics[v] * non_toxic_rules_acc[v])

    #综合四个视角
    sample_predict = -1  # 样本预测标签 样本真实标签
    dogfall=2 #平局情况（1 出现平局；2 不出现平局）
    distance_l, w_distance_l, distance_label_l = [0,0,0,0], [0,0,0,0] ,[0,0,0,0]# 距离数组、距离预测标签数组
    d_toxic_l, d_non_toxic_l = [], []  # 有毒、无毒标签统计
    d_label_index = 0
    if len(toxic_list)>len(non_toxic_list): #认为有毒视角>无毒
        sample_predict=1
    elif len(toxic_list)<len(non_toxic_list): #认为有毒视角<无毒
        sample_predict=0
    elif len(toxic_list)!=0 or len(dogfall_list)!=0: #出现平局 但覆盖
        dogfall=1 #出现平局

        for v_id in range(view_amount):
            if v_list[v_id] ==1 :
                d1, d2, d3 = viewCenter.calculate_distance(v_id, sample_index, experiment_amount)  # 计算距离两个类别中心的距离

                distance_l[v_id]= abs(d1 - d2) / d3
                w_distance_l[v_id] = (abs(d1 - d2) / d3) * view_weight[v_id]
                if d1 < d2:
                    distance_label_l[v_id] = 1
                    d_toxic_l.append(v_id)
                elif d1 > d2:
                    distance_label_l[v_id] = 0
                    d_non_toxic_l.append(v_id)

        data = distance_l
        data.extend(w_distance_l)

        if len(d_toxic_l) > len(d_non_toxic_l):  # 有毒次数>无毒次数
            sample_predict = 1
        elif len(d_toxic_l) < len(d_non_toxic_l):  # 有毒次数<无毒次数
            sample_predict = 0
        else:  # 又是杀千刀的平局
            d_label_index = w_distance_l.index(max(w_distance_l))
            sample_predict = distance_label_l[d_label_index]

    else: #len(toxic_list)=len(non_toxic_list)=0 且len(dog_fall_list)=0 即为四个视角均不覆盖 彻底没救了
        sample_predict = -1
    
    data = view_toxics
    data.extend(view_non_toxics)
    data.extend(" ")
    data.extend(view_weight)
    data.extend(" ")
    data.extend([sample_label,sample_predict])
    return sample_predict,dogfall


def calculate(ind,rules_info_l, concat, v_list):
    global x_test,y_test
    global experiment_amount

    #选择数据集
    sample_amount = x_test.shape[0]
    csvRecord.record_line(write_l, ["test"], [concat,experiment_amount])

    correct, error = 0, 0  # 当前个体对当前样本的预测情况
    c1, c2, e1, e2 = 0, 0, 0, 0  # 当前个体在当前个体上的错误情况
    ind_predict, ind_label = [], []  # 规则集预测结果、对应样本真实标签

    # 遍历所有样本，计算该个体在所有样本上的准确率和覆盖率
    for sample_index in range(sample_amount):
        sample_predict, dogfall = f(ind, sample_index, rules_info_l, v_list)  #返回样本预测标签，以及是否出现平局（2 未出现；1 出现）

        if sample_predict==-1: #当前样本不被规则集覆盖
            continue

        # 获取样本真实标签
        sample_label = y_test[sample_index]

        ind_predict.append(sample_predict)  # 预测标签加入列表
        ind_label.append(sample_label)  # 真实标签加入列表

        if sample_predict==sample_label: #样本预测值和真实标签相同
            correct+=1
            if dogfall==1:
                c1+=1
            elif dogfall==2:
                c2+=1
        elif sample_predict!=sample_label: #样本预测值和真实标签不相同
            error+=1
            if dogfall==1:
                e1+=1
            elif dogfall==2:
                e2+=1

    report = classification_report(ind_label, ind_predict, output_dict=True)
    acc = report['accuracy']
    f1 = report['macro avg']['f1-score']
    auc = roc_auc_score(ind_label, ind_predict)
    aupr = average_precision_score(ind_label, ind_predict)
    recall_0 = report["0"]['recall']
    recall_1 = report["1"]['recall']
    precision_0 = report["0"]['precision']
    precision_1 = report["1"]['precision']
    evaluate_list = [acc, f1, auc, aupr, recall_0, recall_1, precision_0, precision_1]

    coverage = float(len(ind_predict)) / sample_amount  # 计算覆盖率

    print("\ncorrect: ", correct, "  error: ", error)
    print("矛盾正确", c1, " 不矛盾正确", c2, " 矛盾错误", e1, " 不矛盾错误", e2)
  
    percentage = 0
    if (c1+e1) != 0:
        percentage = c1 / (c1+e1)

    return acc, coverage, c1, c2, e1, e2, percentage,evaluate_list

#初始化
def initial(r_amount_l,r_offset_l,e_amount):
    global x_test,y_test
    global rule_amount_list,offset_list, view_amount,ind_length
    global experiment_amount

    experiment_amount = e_amount
    # 初始化全局变量
    front_path = "./data/dataCrossResult"+str(experiment_amount)+"/" 
    x_test_file = front_path + "x_test.csv"  # 特征测试集文件位置
    y_test_file = front_path + "y_test.csv"  # 表现测试集文件位置

    # 初始化全局变量
    x_test = pd.read_csv(x_test_file)  # 特征测试集
    y_test = pd.read_csv(y_test_file).loc[:, 'Y']  # 标签测试集

    rule_amount_list=r_amount_l
    offset_list = r_offset_l  # 视角规则偏移量

    view_amount = len(rule_amount_list)
    ind_length = sum(rule_amount_list)  # 个体长度

    return

def concat_acc(ind_list, weight_info):
    global rule_amount_list

    concat_list = ["1+2", "1+3", "1+4", "2+3", "2+4", "3+4", \
                   "1+2+3", "1+2+4", "1+3+4", "2+3+4", "1+2+3+4"]

    t_acc_l,t_cover_l,t_error_l=[],[],[]
    evaluate_t=[]
    t_rules_info_l = weight_info

    for c in concat_list:
        v_list=[0,0,0,0] #视角列表

        c_list=c.split('+')
        for x in c_list:
            v=int(x)
            v_list[v-1]=1

        ind=[]
        for v in range(view_amount):
            if v_list[v]==1:
                ind.extend(ind_list[v])
            else:
                sub_ind=[0]*rule_amount_list[v]
                ind.extend(sub_ind)

        print("\nview concat", c)
        t_acc, t_cover, t_c1, t_c2, t_e1, t_e2, t_percentage, evaluate_l2 = calculate(ind, t_rules_info_l, c, v_list)
        print("测试集 acc", t_acc, "cover2", t_cover, " c1", t_c1, " c2", t_c2, " e1", t_e1, " e2", t_e2)

        t_acc_l.append(t_acc)
        t_cover_l.append(t_cover)
        t_error_l.append([t_c1, t_c2, t_e1, t_e2, t_percentage])
        evaluate_t.append(evaluate_l2)

    print("\n")

    return t_acc_l, t_cover_l, t_error_l, evaluate_t

