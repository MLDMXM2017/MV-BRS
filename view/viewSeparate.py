import view.viewCenter as viewCenter
from ruleInformation.view0 import rules0_1, rules0_2, rules0_3, rules0_4, rules0_5
from ruleInformation.view1 import rules1_1, rules1_2, rules1_3, rules1_4, rules1_5
from ruleInformation.view2 import rules2_1, rules2_2, rules2_3, rules2_4, rules2_5
from ruleInformation.view3 import rules3_1, rules3_2, rules3_3, rules3_4, rules3_5
import pandas as pd
from collections import defaultdict
from sklearn.metrics import classification_report,roc_auc_score,average_precision_score

global x_test, y_test
global view_amount
global experiment_amount
global rule_sample_num

#计算个体对单个样本的预测结果
def f(view_id,ind,sample_index):

    global x_test
    global experiment_amount

    # 从对应数据文件中取出样本
    x = x_test.iloc[[sample_index]]

    toxic_amount, non_toxic_amount = 0, 0  # 认为有毒和无毒的规则数目

    # 遍历个体
    for i in range(len(ind)):
        if ind[i] == 1:
            rule_index = i
            rule_f = "rules"+ str(view_id)+"_"+str(experiment_amount)+".rule" + str(rule_index)
            toxic_result = eval(rule_f)(x)

            if toxic_result == 1:  # 当前规则认为有毒
                toxic_amount += 1

            elif toxic_result == 0:  # 当前规则认为无毒
                non_toxic_amount += 1


    #综合得出个体对样本的预测值
    sample_predict=-1 #个体对样本的预测值
    dogfall=2 #默认没有出现平局
    if toxic_amount>non_toxic_amount: #认为有毒次数>无毒
        sample_predict=1
    elif toxic_amount<non_toxic_amount: #认为有毒次数<无毒
        sample_predict=0 
    elif toxic_amount!=0: #平局，但是已覆盖
        dogfall=1 #出现平局
        d1, d2, d3 = viewCenter.calculate_distance(view_id, sample_index, experiment_amount)  # 计算距离两个类别中心的距离

        if d1<d2: #距离有毒中心距离<无毒
            sample_predict=1
        elif d1>d2: #距离有毒中心距离>无毒
            sample_predict=0
    else:
        sample_predict = -1

    return sample_predict,dogfall

#计算单个视角上，个体对整个数据集上样本的准确率、覆盖率和差错情况
#传入：
#返回：
def calculate(view_id,ind):
    global x_test, y_test

    #选择数据集：验证集或测试集
    sample_amount=x_test.shape[0]

    correct, error = 0, 0  # 当前个体对当前样本的预测情况
    c1, c2, e1, e2 = 0, 0, 0, 0  # 当前个体在当前个体上的错误情况
    ind_predict, ind_label = [], []  # 规则集预测结果、对应样本真实标签

    # 遍历所有样本，计算该个体在所有样本上的准确率和覆盖率
    for sample_index in range(sample_amount):
        sample_predict, dogfall = f(view_id, ind, sample_index)  #返回样本预测标签，以及是否出现平局（2 未出现；1 出现）

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

    coverage=float(len(ind_predict))/sample_amount #计算覆盖率

    print("\ncorrect: ",correct,"  error: ",error)
    print("矛盾正确",c1," 不矛盾正确",c2," 矛盾错误",e1," 不矛盾错误",e2)

    return acc, coverage, c1, c2, e1, e2, evaluate_list



#初始化 主要是规则偏移量、读入测试集、验证集等
def initial(v_amount, e_amount):
    global x_test, y_test
    global view_amount
    global experiment_amount
    global rule_sample_num

    experiment_amount=e_amount
    
    front_path = "./data/dataCrossResult"+str(experiment_amount)+"/" 
    x_test_file = front_path + "x_test.csv"  # 特征测试集文件位置
    y_test_file = front_path + "y_test.csv"  # 表现测试集文件位置

    x_test = pd.read_csv(x_test_file)  # 特征测试集
    y_test = pd.read_csv(y_test_file).loc[:, 'Y']  # 标签测试集

    view_amount=v_amount
    rule_sample_num = defaultdict(list)
    return

#计算四个视角单独acc
def seperate_acc(ind_list):
    global view_amount

    t_acc_l, t_cover_l, t_error_l = [], [], []
    evaluate_t = []

    for v in range(view_amount):
        print("\nview", v+1)

        t_acc, t_cover, t_c1, t_c2, t_e1, t_e2, evaluate_l2 = calculate(v,ind_list[v])
        print("测试集 acc", t_acc, "cover2", t_cover, " c1", t_c1, " c2", t_c2, " e1", t_e1, " e2", t_e2)

        t_acc_l.append(t_acc)
        t_cover_l.append(t_cover)
        t_error_l.append([t_c1, t_c2, t_e1, t_e2, " "])
        evaluate_t.append(evaluate_l2)

    print("\n")
    return t_acc_l, t_cover_l, t_error_l, evaluate_t
