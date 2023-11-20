rule_amount1=500
rule_amount2=700
rule_amount3= [471, 500, 436, 500, 458]
rule_amount4=1000

view_l=[0,1,2,3] #存放需要进化的视角
view_amount=4
feature_amount_l=[881,978,1023,200] #各视角特征数目
f_offset_l=[0,881,1859,2882] #特征偏移量

experiment_amount=5
#引入其他模块
# import ruleWeight #规则权重
import view.viewCenter as viewCenter #中心距离
import view.viewSeparate as viewSeparate #单视角预测
import view.viewConcat  as viewConcat #合并视角预测
import view.viewMetric as viewMetric #规则相关信息
#import ruleset.beforeSelect as beforeSelect #规则全集
import rulesets.csvRecord as csvRecord #记录文件
import rulesets as rs
import view.viewAcc as viewAcc #多视图
import pandas as pd
import rulesets.ruleinfo as ruleinfo

#创建记录文件
file_l,write_l=csvRecord.create_file(0,"result")
acc_f,acc_w=file_l[0],write_l[0]  
error_f,error_w=file_l[1],write_l[1]
param_list = {'alpha_1': [2000, 3000, 1000, 3000], 'alpha_2': [1000, 500, 1500, 500]}

for e in range(experiment_amount):
    
    rule_amount_list=[rule_amount1,rule_amount2,rule_amount3[e],rule_amount4] #视角规则数目列表
    r_offset_list=[0,rule_amount1,rule_amount1+rule_amount2,rule_amount1+rule_amount2+rule_amount3[e],sum(rule_amount_list)] #规则偏移量列表
    csvRecord.set_e_id(e+1)  # 设置实验id 
   # mainRule(e+1)

    # ruleinfo.rules_acc(view_amount, rule_amount_list, r_offset_list, e+1)

    #模块初始化
    viewCenter.init_center(view_amount,feature_amount_l,f_offset_l, e+1)
    viewMetric.initial(view_amount,r_offset_list, e+1)
    viewSeparate.initial(view_amount, e+1)
    viewConcat.initial(rule_amount_list,r_offset_list, e+1)

    #计算进化前视角情况
    #beforeSelect.acc_before_selct(view_amount,rule_amount_list)

    best_ind_list = []
    best_ind_len, best_inds, best_rules_len = [], [], []
    for v in view_l:
        print("\n\n@@@@@@@@@@@@---e", e, "view", v, "---@@@@@@@@@@@@")
        print("\n\n@@@@@@@@@@@@---alpha-1", param_list['alpha_1'][v], "alpha-2", param_list['alpha_2'][v], "---@@@@@@@@@@@@")
        front_path = "./data/dataCrossResult"+str(e+1)+"/" 
        view_str = str(v)  # 视角编号

        x_train_path = front_path + "x" + view_str + "_train.csv"
        y_train_path = front_path + "y_train.csv"

        x_train_df = pd.read_csv(x_train_path)
        y_train_df = pd.read_csv(y_train_path).loc[:, 'Y']

        model = rs.BayesianRuleSet(view_id=v, experiment_amount=e+1,alpha_1=param_list['alpha_1'][v], alpha_2=param_list['alpha_2'][v])
        best_ind = model.fit(x_train_df, y_train_df)
        
        best_rules = [1 if i in best_ind else 0 for i in range(rule_amount_list[v])]
        best_ind_list.append(best_rules)  

        best_ind_len.append(len(best_ind))
        best_inds.append(sorted(best_ind))
        best_rules_len.append(len(best_rules))

    concat_t_acc_l, concat_t_cover_l, concat_t_error_l, concat_t_evaluate_l = viewAcc.view_acc(best_ind_list)

    # 将结果记录在文件中
    #csvRecord.set_index(e)

    # 测试集acc和cover
    data = concat_t_acc_l
    data.append(" ")
    data.extend(concat_t_cover_l)
    data.extend(best_ind_len)
    data.extend(best_inds)
    data.extend(best_rules_len)
    csvRecord.record_line(acc_w, data, e)

    # 测试集error结果
    csvRecord.record_line(error_w, " ", e)
    index_list = ["v1", "v2", "v3", "v4", \
                "1+2", "1+3", "1+4", "2+3", "2+4", "3+4", "1+2+3", "1+2+4", "1+3+4", "2+3+4", "1+2+3+4"]
    
    csvRecord.record_line(error_w, ["test"], " ")
    for i in range(len(index_list)):
        #csvRecord.set_index(index_list[i])

        data = concat_t_error_l[i]
        data.append(" ")
        data.extend(concat_t_evaluate_l[i])
        csvRecord.record_line(error_w, data, index_list[i])


    csvRecord.record_line(error_w, " ", " ")
    csvRecord.file_flush(file_l)