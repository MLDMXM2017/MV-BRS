import view.viewSeparate as viewSeparate
import view.viewConcat as viewConcat
import view.viewMetric as viewMetric 
def view_acc(ind_list):
    # 分别在单独和拼接情况下，计算各视角情况

    t_rules_info_l = viewMetric.rules_acc(ind_list)
    weight_info = t_rules_info_l

    t_acc_l1, t_cover_l1, t_error_l1, t_evaluate_l1 = viewSeparate.seperate_acc(ind_list)  # 单视角
    t_acc_l2, t_cover_l2, t_error_l2, t_evaluate_l2 = viewConcat.concat_acc(ind_list, weight_info)  # 视角拼接
    
    t_acc_l, t_cover_l, t_error_l, t_evaluate_l = t_acc_l1, t_cover_l1, t_error_l1, t_evaluate_l1

    t_acc_l.extend(t_acc_l2)
    t_cover_l.extend(t_cover_l2)
    t_error_l.extend(t_error_l2)
    t_evaluate_l.extend(t_evaluate_l2)

    return t_acc_l, t_cover_l, t_error_l, t_evaluate_l
