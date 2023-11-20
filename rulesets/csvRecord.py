# Description：结果记录文件

import csv

#规则提取部分记录文件
before_name_l=["acc_before_bayesian.csv"]
before_header_l=[]


#最终结果记录文件
result_name_l=["acc_after_bayesian.csv","error_after_bayesian.csv"]
result_h1=["e_id","V1","V2","V3","V4",\
            "1+2", "1+3", "1+4", "2+3", "2+4", "3+4", \
            "1+2+3", "1+2+4", "1+3+4", "2+3+4", "1+2+3+4","cover", \
           "V1", "V2", "V3", "V4",  \
           "1+2", "1+3", "1+4", "2+3", "2+4", "3+4", \
           "1+2+3", "1+2+4", "1+3+4", "2+3+4", "1+2+3+4"]

result_h2=[["view","c1","c2","e1","e2", "percentage"," ", "acc", "f1", "auc", "aupr", "recall_0", "recall_1", "precision_0", "precision_1"]]
result_header_l=[result_h1,result_h2]


rules_name_l = ["rules_info.csv"]
rules_header_l = [["index", "acc", "coverage", "weight", "toxic", "non_toxic", "sample", "sample_index"]]

global experiment_time


def set_e_id(e_time):
    global experiment_time

    experiment_time=e_time

    return

#创建文件
def create_file(view_id,module):
    file_l,write_l=[],[]

    if module=="before":
        name_l = before_name_l
        header_l = before_header_l
        front_path="./result/"
    elif module=="result":
        name_l = result_name_l
        header_l = result_header_l
        front_path ="./result/" 
    elif module=="rules":
        name_l = rules_name_l
        header_l = rules_header_l
        front_path ="./result/rules/view"+str(view_id)+"/"+str(experiment_time)+"_view"+str(view_id)+"_"

    for i in range(len(name_l)):
        name=name_l[i]
        file_path=front_path+name
        if module=="before" :
            f = open(file_path, 'a+', newline='')
        elif module=="result":
            f = open(file_path, 'a+', newline='') 
        elif module=="rules":
            f=open(file_path,'w',newline='')

        write = csv.writer(f)
        if module=="result" or module=="rules":
            write.writerow(header_l[i])

        file_l.append(f)
        write_l.append(write)

    return file_l,write_l


#向文件写入一行信息
def record_line(write,data,index):
   
    row=[index]
    row.extend(data)

    write.writerow(row)

    return


#将缓存中的数据立即写入文件
def file_flush(file_list):
    for f in file_list:
        f.flush()

    return

#关闭文件
def file_close(file_list):
    for f in file_list:
        f.close()

    return
