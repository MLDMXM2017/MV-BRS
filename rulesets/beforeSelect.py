# 计算筛选前规则对样本预测情况

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


import csvRecord as csvRecord #记录文件
import beforeView.beforeviewAcc as beforeviewAcc
import pandas as pd

def acc_before_selct(view_amount, rule_amount_l, file_l, write_l, e):
    print("\ncalculate view acc before selecting...",e)

    # # 从文件中读取forest的acc
    # f_acc_path = "ruleInformation/forest_acc.csv"
    # f_acc_df = pd.read_csv(f_acc_path)
    # f_v_acc_l = f_acc_df.loc[:, 'f_v_acc'].tolist()
    # f_t_acc_l = f_acc_df.loc[:, 'f_t_acc'].tolist()

    #个体为规则全集
    ind_list=[]
    for amount in rule_amount_l:
        ind=[1]*amount
        ind_list.append(ind)

    t_acc_l, t_cover_l, t_error_l, t_evaluate_l = beforeviewAcc.view_acc(ind_list)

    # 将结果记录在csv文件中
    # 创建文件
    rule_f = file_l[0]
    rule_w = write_l[0]

    # # 各视角规则情况记录
    
    csvRecord.record_line(rule_w, ["test"], e)

    print("\nrandom forest and rule situation recorded...")

    # 视角拼接情况记录

    # 测试集
    csvRecord.record_line(rule_w, ["V1", "V2", "V3", "V4", \
                                   "1+2", "1+3", "1+4", "2+3", "2+4", "3+4", \
                                   "1+2+3", "1+2+4", "1+3+4", "2+3+4", "1+2+3+4"], e)
    csvRecord.record_line(rule_w, t_acc_l, "acc")
    csvRecord.record_line(rule_w, t_cover_l, "cover")

    # 视角拼接测试集error
    csvRecord.record_line(rule_w, ["error"], " ")
    csvRecord.record_line(rule_w, ["c1", "c2", "e1", "e2", " ", \
                                   "accuracy", "f1_score", "auc", "recall_0", "recall_1", "precision_0", "precision_1"], e)

    index_list = ["v1", "v2", "v3", "v4", \
                  "1+2", "1+3", "1+4", "2+3", "2+4", "3+4", "1+2+3", "1+2+4", "1+3+4", "2+3+4", "1+2+3+4"]
    for i in range(len(index_list)):
        data = t_error_l[i]
        data.append(" ")
        data.extend(t_evaluate_l[i])
        csvRecord.record_line(rule_w, data, index_list[i])

    print("\nview concat on test recorded...")

    return


rule_amount1=500
rule_amount2=700
rule_amount3= [471, 500, 436, 500, 458]
rule_amount4=1000

view_l=[0,1,2,3] #存放需要进化的视角
view_amount=4
feature_amount_l=[881,978,1023,200] #各视角特征数目
f_offset_l=[0,881,1859,2882] #特征偏移量


#引入其他模块
# import ruleWeight #规则权重  不要了好吧
import beforeView.beforeviewCenter as viewCenter #中心距离
import beforeView.beforeviewSeparate as viewSeparate #单视角预测
import beforeView.beforeviewConcat  as viewConcat #合并视角预测


experiment_amount = 5
file_l, write_l = csvRecord.create_file(0, "before")

for e in range(experiment_amount):
    rule_amount_list=[rule_amount1,rule_amount2,rule_amount3[e],rule_amount4] #视角规则数目列表
    r_offset_list=[0,rule_amount1,rule_amount1+rule_amount2,rule_amount1+rule_amount2+rule_amount3[e],sum(rule_amount_list)] #规则偏移量列表

    #模块初始化
    viewCenter.init_center(view_amount,feature_amount_l,f_offset_l, e+1)
    viewSeparate.initial(view_amount, e+1)
    viewConcat.initial(rule_amount_list,r_offset_list, e+1)

    #计算进化前视角情况
    acc_before_selct(view_amount,rule_amount_list,file_l,write_l, e+1)


csvRecord.file_close(file_l)