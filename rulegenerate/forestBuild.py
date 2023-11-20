# Description：构建随机森林
import pandas as pd
import datetime

from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from sklearn.metrics import classification_report

# 创建随机森林模型：对于同一数据五次构建随机森林模型，并选取其中acc最好的模型，返回结果
# 传入:
# 返回: 随机森林、测试集上acc
def build_forest(forest_size,depth,view_id,experiment_amount):
    # 读入数据
    front_path = "./data/dataCrossResult"+str(experiment_amount)+"/"
    view_str = str(view_id)  # 视角编号

    x_train_path = front_path + "x" + view_str + "_train.csv"
    y_train_path = front_path + "y_train.csv"
    x_test_path = front_path + "x" + view_str + "_test.csv"
    y_test_path = front_path + "y_test.csv"

    x_train_df = pd.read_csv(x_train_path)
    y_train_df = pd.read_csv(y_train_path).loc[:, 'Y']
    x_test_df = pd.read_csv(x_test_path)
    y_test_df = pd.read_csv(y_test_path).loc[:, 'Y']

    # for i in range(5):
    #     v_max_acc = 0
    #     # forest = RandomForestClassifier(n_estimators=forest_size, max_depth=depth)
    #     forest = ExtraTreesClassifier(n_estimators=forest_size, max_depth=depth)
    #     forest.fit(x_train_df, y_train_df)
    #     y_v_predict = forest.predict(x_valid_df)
    #     v_report = classification_report(y_valid_df, y_v_predict, output_dict=True)
    #     v_acc=v_report['accuracy']
    #     if v_acc > v_max_acc:       
    #         v_max_acc = v_acc
    #         max_forest = forest

    # y_t_predict = max_forest.predict(x_test_df)
    # t_report = classification_report(y_test_df, y_t_predict, output_dict=True)
    # t_acc = t_report['accuracy']

    
    forest = RandomForestClassifier(n_estimators=forest_size, max_depth=depth)
    # forest = ExtraTreesClassifier(n_estimators=forest_size, max_depth=depth)
    forest.fit(x_train_df, y_train_df)

    max_forest=forest
    y_t_predict = max_forest.predict(x_test_df)
    t_report = classification_report(y_test_df, y_t_predict, output_dict=True)
    t_acc = t_report['accuracy']

    return x_train_df, y_train_df, max_forest, t_acc