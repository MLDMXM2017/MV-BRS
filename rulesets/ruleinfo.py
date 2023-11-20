from ruleInformation.view0 import rules0_1, rules0_2, rules0_3, rules0_4, rules0_5
from ruleInformation.view1 import rules1_1, rules1_2, rules1_3, rules1_4, rules1_5
from ruleInformation.view2 import rules2_1, rules2_2, rules2_3, rules2_4, rules2_5
from ruleInformation.view3 import rules3_1, rules3_2, rules3_3, rules3_4, rules3_5
import pandas as pd
from sklearn.metrics import classification_report,roc_auc_score, f1_score, accuracy_score
from collections import defaultdict
import numpy as np
global x_train, y_train
global experiment_amount

#计算每一个view里的规则的精度和覆盖率
def calculate(view_id, ind):
    global x_train, y_train
    global experiment_amount,rule_offset_l

    #选择数据集：验证集或测试集
    sample_amount=x_train.shape[0]
    
    rule_info = []
    all_sample = []
    print("view-------", view_id, "e_id-------", experiment_amount, "ind---",ind)
    for rule_index in range(ind):     
        predict_list, sample_list, sample_index_l= [], [], []
        view_toxics, view_non_toxics = 0,0     
        for sample_index in range(sample_amount):
            x = x_train.iloc[[sample_index]]
            sample_label = y_train[sample_index]
            rule_f = "rules"+ str(view_id)+"_"+str(experiment_amount)+".rule" + str(rule_index)
            toxic_result = eval(rule_f)(x)
            if toxic_result != -1:
                if toxic_result == 1:
                    view_toxics += 1
                elif toxic_result == 0:
                    view_non_toxics += 1
                predict_list.append(toxic_result)
                sample_list.append(sample_label)
                sample_index_l.append(sample_index)
        
        all_sample=list(set(sample_index_l + all_sample))

        predict = 0
        if view_toxics > view_non_toxics:
            predict = 1
        # report = classification_report(sample_list, predict_list, output_dict=True)
        acc = accuracy_score(sample_list, predict_list)
        # f1 = f1_score(sample_list, predict_list, average='macro')
        coverage = float(len(sample_list))/sample_amount
        info_weight = acc * coverage
        data = [rule_index, acc, coverage, info_weight]
        data.extend([predict, (view_toxics + view_non_toxics)])
        data.extend([sample_index_l])     
        rule_info.append(data)

    rule_info=np.array(rule_info)       
    # sorted_rule_info = rule_info[rule_info[:, 2].argsort()[::-1]] 
    clm = ["index", "acc", "coverage", "weight", "predict", "sample", "sample_index"]
    df_rule_info = pd.DataFrame(rule_info, columns=clm)
    df_rule_info.sort_values(by=['weight', 'sample'], inplace=True, ascending=[False, False])
    return df_rule_info

def rules_acc(v_amount, ind_list, r_offset_list, e_amount):
    global x_train, y_train
    global rule_offset_l,experiment_amount
    
    experiment_amount=e_amount
    
    front_path = "./data/dataCrossResult"+str(experiment_amount)+"/" 
    x_train_file = front_path + "x_train.csv"  # 特征验证集文件位置
    y_train_file = front_path + "y_train.csv"  # 标签验证集文件位置
    x_test_file = front_path + "x_test.csv"  # 特征测试集文件位置
    y_test_file = front_path + "y_test.csv"  # 表现测试集文件位置

    x_train = pd.read_csv(x_train_file)  # 特征验证集
    y_train = pd.read_csv(y_train_file).loc[:, 'Y']  # 标签验证集
    x_test = pd.read_csv(x_test_file)  # 特征测试集
    y_test = pd.read_csv(y_test_file).loc[:, 'Y']  # 标签测试集
   
    rule_offset_l= r_offset_list
    view_amount=v_amount

    for v in range(view_amount):
        sorted_rule_info = calculate(v, ind_list[v])
        front_path2="./result/rules/view"+str(v)+"/"+str(experiment_amount)+"_view"+str(v)+"_"
        sorted_rule_info.to_csv(front_path2+"rule_info.csv",index=False,sep=',',encoding='utf_8')