from __future__ import print_function
from __future__ import division


from bisect import bisect_left
from random import sample

from collections import Counter, defaultdict
from multiprocessing import Pool
from tkinter import X
from sklearn.metrics import classification_report, precision_score, accuracy_score, f1_score, recall_score

import pandas as pd
import numpy as np
from numpy.random import random

from rulesets.utils import *
from ruleInformation.view0 import rules0_1, rules0_2, rules0_3, rules0_4, rules0_5
from ruleInformation.view1 import rules1_1, rules1_2, rules1_3, rules1_4, rules1_5
from ruleInformation.view2 import rules2_1, rules2_2, rules2_3, rules2_4, rules2_5
from ruleInformation.view3 import rules3_1, rules3_2, rules3_3, rules3_4, rules3_5
import view.viewCenter as viewCenter

TREE_DEPTH=[7,4,15,10]
global RMatrix_0, RMatrix_1, rules, rules_0, rules_1, supp_0, supp_1, ruleslen_0, ruleslen_1
global actionset, actionprob, pb_cut, pb_add
global x_train

class BayesianRuleSet(object):
    '''Find the rule set from the data

        X needs to be a pandas DataFrame,
        y needs to be a nd.array as integer or boolean

        Note
        ----------
        (Sometimes, there will be open range. This is because the
        cutoffs in the range is empty.)

        Parameters
        ----------
        max_rules : int, default 5000
            Maximum number of rules when generating rules

        max_iter : int, default 200
            Maximun number of iteratations to find the rule set

        chians : int, default 1
            Number of chains that run in parallel

        support : int, default 5
            The support is the percentile threshold for the itemset
            to be selected.

        maxlen : int, default 3
            The maximum number of items in a rule

        #note need to replace all the alpha_1 to alpha_+
        alpha_1 : float, default 100
            alpha_+

        beta_1 : float, default 1
            beta_+

        alpha_2 : float, default 100
            alpha_-

        beta_2 : float, default 1
            beta_-

        alpha_l : float array, shape (maxlen+1,)
            default all elements to be 1

        beta_l : float array, shape (maxlen+1,)
            default corresponding patternSpace

        level : int, default 4
            Number of intervals to deal with numerical continous features

        neg : boolean, default True
            Negate the features

        add_rules : list, default empty
            User defined rules to add
            it needs user to add numerical version of the rules

        criteria : str, default 'precision'
            When there are rules more than max_rules,
            the criteria used to filter rules

        greedy_initilization : boolean, default False
            Wether start the rule set using a greedy
            initilization (according to accuracy)

        greedy_threshold : float, default 0.05
            Threshold for the greedy algorithm
            to find the starting rule set

        propose_threshold : float, default 0.1
            Threshold for a proposal to be accepted

        rule_adjust : boolean, default True
            If the numerical rules need to be adjusted
            according to the cutoffs.
'''

    def __init__(self, max_iter=500, chains=1,
                 alpha_1=3000, beta_1=1,
                 alpha_2=1500, beta_2=1,
                 alpha_l=None,beta_l=None,  neg=True,
                 add_rules=[], 
                 greedy_initilization=False, greedy_threshold=0.05,
                 propose_threshold=0.1,rule_adjust=True, view_id=None, experiment_amount=None):
        self.max_iter = max_iter  
        self.chains = chains  
        self.alpha_1 = alpha_1 
        self.beta_1 = beta_1  
        self.alpha_2 = alpha_2 
        self.beta_2 = beta_2  
        self.alpha_l = alpha_l 
        self.beta_l = beta_l  
        self.neg = neg
        self.add_rules = add_rules
        self.greedy_initilization = greedy_initilization
        self.greedy_threshold = greedy_threshold
        self.propose_threshold = propose_threshold
        self.rule_adjust = rule_adjust
        self.view_id = view_id  
        self.e_amount = experiment_amount  

        self.predicted_rules = []

        self.iter_gradient = []  
        self.gradient_std = []
        # self.last_iter = 0

    def initialize(self):
        global RMatrix, RMatrix_0, RMatrix_1, rules_0, rules_1, supp_0, supp_1, ruleslen_0, ruleslen_1
        global non_cover
 
        rules, rules_0, rules_1, supp = [], [], [], []
        front_path_r="./ruleInformation/view"+str(self.view_id)+"/"+str(self.e_amount)+"_v"+str(self.view_id)+"_"
        RMatrix = np.array(pd.read_csv(front_path_r+"RMatrix.csv"))
        RMatrix_0 = np.array(pd.read_csv(front_path_r+"RMatrix_0.csv"))
        RMatrix_1 = np.array(pd.read_csv(front_path_r+"RMatrix_1.csv"))
        rulelist_0 = pd.read_csv(front_path_r+"rulelist_0.csv")
        rulelist_1 = pd.read_csv(front_path_r+"rulelist_1.csv")
        rulelist = pd.read_csv(front_path_r+"rulelist.csv").iloc[:,:-1]
        rule_predict = pd.read_csv(front_path_r+"rulelist.csv").iloc[:, -1]
        for i in range(rulelist_0.shape[0]):
            rules_0.append([int(m) for m in rulelist_0.loc[i,:] if np.isnan(m)==False])
        for i in range(rulelist_1.shape[0]):
            rules_1.append([int(m) for m in rulelist_1.loc[i,:] if np.isnan(m)==False])
        for i in range(rulelist.shape[0]):
            rules.append([int(m) for m in rulelist.loc[i,:] if np.isnan(m)==False])
        supp = np.asarray([i for i in np.sum(RMatrix, axis=0)])
        supp_0 = np.asarray([i for i in np.sum(RMatrix_0, axis=0) if i != 0])
        supp_1 = np.asarray([i for i in np.sum(RMatrix_1, axis=0) if i != 0])
        ruleslen_0 = np.asarray([len(rule) for rule in rules_0])
        ruleslen_1 = np.asarray([len(rule) for rule in rules_1])
        ruleslens = np.asarray([len(rule) for rule in rules])
        self.rules = rules
        self.rules_len = ruleslens
        self.maxlen = TREE_DEPTH[self.view_id]
        self.supp = np.asarray(supp) 
        self.rule_predict = rule_predict   

        front_path="./result/rules/view"+str(self.view_id)+"/"+str(self.e_amount)+"_view"+str(self.view_id)+"_"
        self.rules_info = pd.read_csv(front_path+"rule_info.csv")

        non_cover = []
        return

    # 设置先验参数
    def set_parameters(self):
        self.patternSpace = np.ones(self.maxlen + 1) 

        for i in range(1, self.maxlen + 1):
            self.patternSpace[i] = list(np.bincount([i for i in self.rules_len], minlength=self.maxlen + 1))[i]
        if self.alpha_l == None:
            self.alpha_l = [1 for i in range(self.maxlen + 1)] 
        if self.beta_l == None: 
            self.beta_l = [(self.patternSpace[i] * 100 + 1) for i in range(self.maxlen + 1)]
    
    #最佳状况下的likelihood和prior
    def precompute(self, y):
        TP, FP, TN, FN = sum(y), 0, len(y) - sum(y), 0

        self.Lup = (log_betabin(TP, TP + FP, self.alpha_1, self.beta_1)  # ρ+ positive precision
                    + log_betabin(TN, FN + TN, self.alpha_2, self.beta_2))  # ρ- negative precision

        self.const_denominator = [np.log((self.patternSpace[i] + self.beta_l[i] - 1)
                                         / (self.patternSpace[i] + self.alpha_l[i] - 1))
                                  for i in range(self.maxlen + 1)]

        Kn_count = np.zeros(self.maxlen + 1, dtype=int) 

        self.P0 = sum([log_betabin(Kn_count[i], self.patternSpace[i], self.alpha_l[i],
                                   self.beta_l[i]) for i in range(1, self.maxlen + 1)])

    #贪心初始化规则集
    def greedy_init(self, RMatrix):
        global RMatrix_1
        greedy_rules = []
        stop_condition = max(int(RMatrix.shape[0] * self.greedy_threshold), 100)

        idx = np.arange(RMatrix.shape[0])
        while True:
            TP = np.sum(RMatrix_1[idx], axis=0)  # 每一条规则能覆盖多少个正样本
            rule = sample(np.where(TP == TP.max())[0].tolist(), 1)
            greedy_rules.extend(rule)
            Z = self.find_rules_Z(greedy_rules)
            idx = np.where(Z == False)
            if np.sum(RMatrix[idx], axis=0).max() < stop_condition:
                return greedy_rules

    def normalize(self, rules_new):
        try:
            rules_len = [len(self.rules[index]) for index in rules_new]
            rules = [rules_new[i] for i in np.argsort(rules_len)[::-1][:len(rules_len)]]
            p1 = 0
            while p1 < len(rules):
                for p2 in range(p1 + 1, len(rules), 1):
                    if set(self.rules[rules[p2]]).issubset(set(self.rules[rules[p1]])):
                        rules.remove(rules[p1])
                        p1 -= 1
                        break
                p1 += 1
            return rules[:]
        except:
            return rules_new[:]


    def find_rules_Z(self, rules):  # 返回yhat
        global  RMatrix, RMatrix_0, RMatrix_1, non_cover
        Z = []
        non_cover = []
        if len(rules) == 0:
            return np.zeros(RMatrix.shape[0], dtype=int)
        Z_0 = np.zeros(RMatrix_0.shape[0], dtype=int)
        Z_1 = np.zeros(RMatrix_1.shape[0], dtype=int)
        for rule in rules:
            Z_0 = RMatrix_0[:, rule] + Z_0
            Z_1 = RMatrix_1[:, rule] + Z_1 
        Z_0 = Z_0 .astype(int) 
        Z_1 = Z_1 .astype(int)

        sample_index = 0
        for z1, z0 in zip(Z_1, Z_0):
            if z1 > z0:
                Z.append(1)
            elif z1 < z0:
                Z.append(0)
            elif z1 != 0:
                d1, d2, d3 = viewCenter.t_calculate_distance(self.view_id, sample_index, self.e_amount)
                if d1<d2: #距离有毒中心距离<无毒
                    Z.append(1)
                elif d1>d2: #距离有毒中心距离>无毒
                    Z.append(0)
            else:
                # Z.append(1)
                t = random()
                if t < 0.5:
                    Z.append(1)
                else:
                    Z.append(0)
                non_cover.append(sample_index)
            sample_index += 1
        return np.asarray(Z) 

    def t_find_rules_Z(self, rules):
        global  RMatrix, RMatrix_0, RMatrix_1
        Z = []
        if len(rules) == 0:
            return np.full(RMatrix.shape[0], -1), 0
        Z_0 = np.zeros(RMatrix_0.shape[0], dtype=int)
        Z_1 = np.zeros(RMatrix_1.shape[0], dtype=int)
        for rule in rules:
            Z_0 = RMatrix_0[:, rule] + Z_0
            Z_1 = RMatrix_1[:, rule] + Z_1 
        Z_0 = Z_0 .astype(int) 
        Z_1 = Z_1 .astype(int)

        non_cover_yhat = 0

        sample_index = 0
        for z1, z0 in zip(Z_1, Z_0):
            if z1 > z0:
                Z.append(1)
            elif z1 < z0:
                Z.append(0)
            elif z1 != 0:
                d1, d2, d3 = viewCenter.t_calculate_distance(self.view_id, sample_index, self.e_amount)
                if d1<d2: #距离有毒中心距离<无毒
                    Z.append(1)
                elif d1>d2: #距离有毒中心距离>无毒
                    Z.append(0)
            else:
                Z.append(-1)
                non_cover_yhat += 1
            sample_index += 1
        return np.asarray(Z),non_cover_yhat

    # 对规则集进行，添加或者删除规则
    def propose(self, rules_curr, rules_norm, y, iter):
        global RMatrix, actionset, actionprob, pb_add, pb_cut
        actionset, actionprob = [], [] #动作集合 动作概率
        pb_add, pb_cut = 0.0, 0.0
        
        yhat, num = self.t_find_rules_Z(rules_curr)

        incorr_pos = np.where((y != yhat) & (yhat == 1))[0] #实际为负 被预测为正 FP
        incorr_neg = np.where((y != yhat) & (yhat == 0))[0] #实际为正 被预测为负 FN
        incorr = np.where(y != yhat)[0]
        uncover_pos = np.where((y == 1) & (yhat == -1))[0]
        uncover_neg = np.where((y == 0) & (yhat == -1))[0]
        rules_curr_len = len(rules_curr)

        rules_poslen, rules_neglen = 0,0 #正规则、负规则的数量
        rules_pos, rules_neg = [], [] #正规则、负规则的集合
        for rule in rules_curr:
            if self.rule_predict[rule] == 0:
                rules_neglen += 1
                rules_neg.append(rule)
            if self.rule_predict[rule] == 1:
                rules_poslen += 1
                rules_pos.append(rule)

        if len(incorr) == 0:
            clean = True
            move = ['clean']
        else:
            clean = False
            t = random()
            if len(incorr_neg) >= len(incorr_pos) or len(uncover_pos) >= len(uncover_neg): 
                if t < 1.0 / 2  or rules_poslen == 0  or  rules_neglen <= 1:
                    move = ['add-pos']  # add正规则
                    actionset.append('add-pos')
                elif  t > 1.0 / 2 and t < 2.0 / 3:
                    move = ['cut-neg']  # cut负规则
                    actionset.append('cut-neg')
                else:
                    move = ['cut-neg', 'add-pos']  # add-explicit
                    actionset.append('cut-neg+add-pos')
            else: 
                if t < 1.0 / 2 or  rules_neglen == 0 or rules_poslen <= 1:
                    move = ['add-neg']  # add负规则
                    actionset.append('add-neg')
                elif  t > 1.0 / 2 and t < 2.0 / 3 :
                    move = ['cut-pos']  # cut正规则
                    actionset.append('cut-pos')
                else:
                    move = ['cut-pos', 'add-neg']
                    actionset.append('cut-pos+add-neg')

        if len(move) > 0 and move[0] == 'cut-neg': 
            try:
                if random() < self.propose_threshold:
                    candidate = []
                    ex = sample(list(incorr_neg), 1)[0] 
                    for rule in rules_neg:
                        if RMatrix_0[ex, rule]:
                            candidate.append(rule)
                    if len(candidate) == 0:
                        candidate = rules_neg
                    cut_rule = sample(candidate, 1)[0] 
                else:
                    p = []
                    all_sum = np.zeros(RMatrix.shape[0], dtype=int)
                    for rule in rules_neg:
                        all_sum = all_sum + RMatrix_0[:, rule]
                    for rule in rules_neg:
                        original_yhat = (all_sum - RMatrix_0[:, rule]) > 0
                        yhat = [0 if num == 1 else 1 for num in original_yhat]
                        TP, FP, TN, FN = get_confusion(yhat, y)
                        p.append(TN.astype(float) / (TN + FN + 1))
                    p = [x - min(p) for x in p]
                    p = np.exp(p)
                    p = np.insert(p, 0, 0)
                    p = np.array(list(accumulate(p)))
                    if p[-1] == 0:
                        index = sample(list(range(len(rules_neg))), 1)[0]
                    else:
                        p = p / p[-1]
                        index = find_lt(p, random())
                    cut_rule = rules_neg[index]
                rules_curr.remove(cut_rule)
                rules_norm = self.normalize(rules_curr)
                move.remove('cut-neg')
                rules_neglen -= 1
            except:
                move.remove('cut-neg')
        
        if len(move) > 0 and move[0] == 'cut-pos':
            try:
                if random() < self.propose_threshold:
                    candidate = []
                    ex = sample(list(incorr_pos), 1)[0] 
                    for rule in rules_pos:
                        if RMatrix_1[ex, rule]:
                            candidate.append(rule)
                    if len(candidate) == 0:
                        candidate = rules_pos
                    cut_rule = sample(candidate, 1)[0] 
                else:
                    p = []
                    all_sum = np.zeros(RMatrix.shape[0], dtype=int)
                    for rule in rules_pos:
                        all_sum = all_sum + RMatrix_1[:, rule]
                    for rule in rules_pos:
                        yhat = (all_sum - RMatrix_1[:, rule]) > 0
                        TP, FP, TN, FN = get_confusion(yhat, y)
                        p.append(TP.astype(float) / (TP + FP + 1))
                    p = [x - min(p) for x in p]
                    p = np.exp(p)
                    p = np.insert(p, 0, 0)
                    p = np.array(list(accumulate(p)))
                    if p[-1] == 0:
                        index = sample(list(range(len(rules_pos))), 1)[0]
                    else:
                        p = p / p[-1]
                        index = find_lt(p, random())
                    cut_rule = rules_pos[index]
                rules_curr.remove(cut_rule)
                rules_norm = self.normalize(rules_curr)
                move.remove('cut-pos')
                rules_poslen -= 1
            except:
                move.remove('cut-pos')

        # 'add' a pos-rule
        if len(move) > 0 and move[0] == 'add-pos':
            select = []
            for ex in incorr_neg:
                select = list(set(select + list(np.where((self.supp > self.C[-1]) & RMatrix_1[ex] > 0)[0])))
            for ex in uncover_pos:
                select = list(set(select + list(np.where((self.supp > self.C[-1]) & RMatrix_1[ex] > 0)[0])))
            select = np.setdiff1d(np.array(select), np.array(rules_curr))
            if len(select) > 0:
                # covers = np.zeros(len(select), dtype=int)
                for i in range(self.rules_info.shape[0]):
                    rule_index = self.rules_info.loc[i,"index"]
                    if rule_index in select:
                        add_rule = rule_index
                        break
                try:
                    if add_rule not in rules_curr:
                        rules_curr.append(add_rule)
                        rules_poslen += 1
                except:
                    1
     
        # 'add' a neg-rule
        if len(move) > 0 and move[0] == 'add-neg':
            select = [] 
            for ex in incorr_pos:
                select = list(set(select + list(np.where((self.supp > self.C[-1]) & RMatrix_0[ex] > 0)[0])))
            for ex in incorr_neg:
                select = list(set(select + list(np.where((self.supp > self.C[-1]) & RMatrix_0[ex] > 0)[0])))
            select = np.setdiff1d(np.array(select), np.array(rules_curr))
            if len(select) > 0:
                for i in range(self.rules_info.shape[0]):
                    rule_index = self.rules_info.loc[i,"index"]
                    if rule_index in select:
                        add_rule = rule_index
                        break
                try:
                    if add_rule not in rules_curr:
                        rules_curr.append(add_rule)
                        rules_neglen += 1
                except:
                    1

        if len(move) > 0 and move[0] == 'clean':
            remove = []
            for i, rule in enumerate(rules_norm):
                yhat = np.zeros(RMatrix.shape[0], dtype=int)
                for j, rule_j in enumerate(rules_norm):
                    if (j != i and j not in remove):
                        yhat = yhat + RMatrix[:, rule_j]
                yhat = yhat > 0
                TP, FP, TN, FN = get_confusion(yhat, y)
                if TP + FP == 0:
                    remove.append(i)
            for x in remove:
                rules_norm.remove(x)
            return rules_curr, rules_norm
        
        return rules_curr, rules_norm

    def compute_prob(self, y, rules):
        yhat = self.find_rules_Z(rules)
        true_yhat, non_cover_yhat= self.t_find_rules_Z(rules)
        TP, FP, TN, FN, un_pos, un_neg = t_get_confusion(true_yhat, y)

        f1 = f1_score(y, yhat, average='macro')
        acc = accuracy_score(y, yhat)
        precision = precision_score(y, yhat)
        recall = recall_score(y, yhat)

        Kn_count = list(np.bincount([self.rules_len[x] for x in rules], minlength=self.maxlen + 1))
        prior_ChsRules = sum([log_betabin(Kn_count[i], self.patternSpace[i], self.alpha_l[i], self.beta_l[i]) for i in range(1, len(Kn_count), 1)])
        likelihood_1 = log_betabin(TP, TP + FP + un_pos, self.alpha_1, self.beta_1)
        likelihood_2 = log_betabin(TN, FN + TN + un_neg, self.alpha_2, self.beta_2)
        return [TP, FP, TN, FN], [acc, f1, precision, recall], [prior_ChsRules, likelihood_1, likelihood_2, non_cover_yhat]

    def print_rules(self, rules):
        front_path="./ruleInformation/view"+str(self.view_id)+"/"+str(self.e_amount)+"_v"+str(self.view_id)+"_"
        all_rules = np.array(pd.read_csv(front_path+"rule.csv"))
        all_reformatted_rules = []
        for rule in rules: 
            rules_list = [item for item in all_rules[rule]]
            reformatted_rules = self.rewrite_rules(rules_list)
            print(reformatted_rules)
            all_reformatted_rules.append(reformatted_rules)
        return all_reformatted_rules

    def rewrite_rules(self, rules_list):
        rewritten_rules = [] 
        depth = TREE_DEPTH[self.view_id]
        for i in range(depth):
            symbol = rules_list[i+depth*2]
            if np.isnan(symbol)==False:
                if symbol == 1:
                    rewritten_rules.append(str(rules_list[i])+' <= '+ str(rules_list[i+depth*1]))
                else:
                    rewritten_rules.append(str(rules_list[i])+' > '+ str(rules_list[i+depth*1]))
        rewritten_rules.append(rules_list[i+depth*2+4])
        return rewritten_rules

    def Bayesian_patternbased(self, x, y, init_rules):
        global x_train
        self.Asize = [[min(self.patternSpace[l] / 2, 
                           0.5 * (self.patternSpace[l] + self.beta_l[l] - self.alpha_l[l])) for l in range(self.maxlen + 1)]]
        # support threshold
        self.C = [1]
        y = y.values
        x_train = x
        nRules = len(self.rules)
        self.maps = defaultdict(list)
        T0 = 1000

        rules_curr = init_rules
        rules_curr_norm = self.normalize(rules_curr)
        pt_curr = -1000000000
        self.maps[0].append([-1, pt_curr, rules_curr, [self.rules[i] for i in rules_curr], []])


        ith_iter = 0
        # for ith_iter in range(self.max_iter):
        while True:
            rules_new, rules_norm = self.propose(rules_curr, rules_curr_norm, y, ith_iter)
            cfmatrix, metricmatrix, prob = self.compute_prob(y, rules_new)

            prob[0] = prob[0] * len(rules_new) / 100 
            pt_new = prob[0] + prob[1] +prob[2] - prob[3] 
                      
            T = T0 ** (1 - ith_iter / self.max_iter)
            alpha = np.exp(float(pt_new - pt_curr) / T)

            if pt_new > self.maps[0][-1][1]:
                acc = (cfmatrix[0] + cfmatrix[2] + 0.0) / len(y)
                print('\n** chain = {}, max at iter = {} ** \n accuracy = {}, TP = {},FP = {}, TN = {}, FN = {}\n old is {},pt_new is {}, prior_ChsRules={}, likelihood_1 = {}, likelihood_2 = {}\n '.format(
                        self.chains, ith_iter, acc, cfmatrix[0], cfmatrix[1],
                        cfmatrix[2], cfmatrix[3], self.maps[0][-1][1], pt_new, prob[0], prob[1], prob[2]))

                rules_new = self.clean_rules(rules_new)
                self.final_print_rules = self.print_rules(rules_new)
                print(rules_new)


                self.Asize.append([np.floor(min(self.Asize[-1][l],
                                                (-pt_new + self.Lup + self.P0) / self.const_denominator[l]))
                                   for l in range(self.maxlen + 1)])   #当前每种长度的最大规则数(因为最小支持度的限制) 原本的跟新的进行对比
                self.const_denominator = [np.log(np.true_divide(self.patternSpace[l] + self.beta_l[l] - 1,
                                                                max(1, self.Asize[-1][l] + self.alpha_l[l] - 1)))  #分母会实时更新
                                          for l in range(self.maxlen + 1)]
                self.maps[0].append([ith_iter, pt_new, rules_new,
                                     [self.rules[i] for i in rules_new],
                                     cfmatrix])
                new_supp = np.ceil(np.log(max([np.true_divide(self.patternSpace[l] - self.Asize[-1][l] + self.beta_l[l],
                                                              max(1, self.Asize[-1][l] + self.alpha_l[l] - 1 ))
                                               for l in range(1, self.maxlen + 1, 1)])))
                self.C.append(new_supp)

            t = random()
            if t <= alpha:  
                rules_curr_norm, rules_curr, pt_curr = rules_norm[:].copy(), rules_new[:].copy(), pt_new
            
            self.predicted_rules = rules_curr.copy()
            ith_iter += 1

            if ith_iter > 500:
                print("迭代到达")
                break
        
        return self.maps[0]
        
    def clean_rules(self, rules):
        # If the rules are not
        # modified then there is no
        # need to check the rules
        global RMatrix
        cleaned = []
        for rule in rules:
            if sum(RMatrix[:, rule]) != 0:
                cleaned.append(rule)
        return cleaned

    def fit(self, x, y):
        global x_train
        
        self.initialize()
        self.set_parameters()
        self.precompute(y)

        x_train = x

        if self.greedy_initilization:
            init = self.greedy_init(RMatrix)
        else:
            init = []
        self.Bayesian_patternbased(x, y, init)

        rule_lengths = []
        for rule in self.predicted_rules:
            rule_lengths.append(len(self.rules[rule]))
       
        return self.predicted_rules  #[self.final_print_rules, rule_lengths, self.predicted_rules, len(self.predicted_rules)]

    #return detailed infomation
    def return_paramter(self): 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        return self.curr_matrix
       
    