from ruleInformation.view0 import rules0_1, rules0_2, rules0_3, rules0_4, rules0_5
from ruleInformation.view1 import rules1_1, rules1_2, rules1_3, rules1_4, rules1_5
from ruleInformation.view2 import rules2_1, rules2_2, rules2_3, rules2_4, rules2_5
from ruleInformation.view3 import rules3_1, rules3_2, rules3_3, rules3_4, rules3_5
import pandas as pd
from sklearn.metrics import classification_report,roc_auc_score, f1_score, accuracy_score
import rulesets.csvRecord as csvRecord #记录文件
from collections import defaultdict

global x_train, y_train
global rule_weight, rule_offset_l
global view_amount
global experiment_amount
global rule_sample_num
global file_l, write_l

#计算每一个view里的规则的精度和覆盖率
def calculate(view_id,ind):
    global x_train, y_train
    global file_l, write_l
    global experiment_amount,rule_offset_l

    #选择数据集：验证集或测试集
    sample_amount=x_train.shape[0]
    
    all_sample = []
    rules_info = defaultdict(lambda: defaultdict(list))
    for i in range(len(ind)):
        if ind[i] == 1:        
            predict_list, sample_list, sample_index_l= [], [], []
            view_toxics, view_non_toxics = 0,0
            rule_index = i            
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

            # report = classification_report(sample_list, predict_list, output_dict=True)
            acc = accuracy_score(sample_list, predict_list)
            f1 = f1_score(sample_list, predict_list, average='macro')
            # auc = roc_auc_score(sample_list, predict_list)
            evaluate_list = [acc, f1]
            coverage = float(len(sample_list))/sample_amount
            data = [i]
            data.extend(evaluate_list)
            data.extend([coverage, view_toxics, view_non_toxics, sample_amount])
            data.extend(sample_index_l)

            rules_info[view_id][i+rule_offset_l[view_id]].append([acc, coverage])
            csvRecord.record_line(write_l, data, experiment_amount) 
    csvRecord.record_line(write_l, [len(all_sample),all_sample], experiment_amount)             
    return rules_info

def rules_acc(ind_list):
    global view_amount, rule_f
    t_rules_info_l = defaultdict(lambda: defaultdict(list))
    for v in range(view_amount):
        csvRecord.record_line(write_l, ["train"], v)  
        t_rules_info = calculate(v,ind_list[v])
        t_rules_info_l.update(t_rules_info)
        csvRecord.file_flush(rule_f)
    return t_rules_info_l

#初始化 主要是规则偏移量、读入测试集、验证集等
def initial(v_amount, r_offset_list, e_amount):
    global x_train, y_train
    global rule_offset_l,view_amount,experiment_amount
    global file_l, write_l, rule_f
    
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

    rule_f, rule_w = csvRecord.create_file(0, "weight") #创建文件
    file_l = rule_f[0]
    write_l = rule_w[0]
    return