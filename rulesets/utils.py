import numpy as np
import math
import itertools
from itertools import chain, combinations
from bisect import bisect_left
from random import sample
import time
import operator
import multiprocessing as mp
from multiprocessing import Pool
from tkinter import X
from scipy.stats.distributions import poisson, gamma, beta, bernoulli, binom
from sklearn.utils import resample

# beta计算
def log_betabin(k, n, alpha, beta):
    try:
        c = math.lgamma(alpha + beta) - math.lgamma(alpha) - math.lgamma(beta)
    except:
        print('alpha = {}, beta = {}'.format(alpha, beta))

    if isinstance(k, (list, np.ndarray)):  # 是这两种元组中的一个
        if len(k) != len(n):
            print('length of k in %d and length of n is %d' % (len(k), len(n)))
            raise ValueError
        lbeta = []
        for ki, ni in zip(k, n):
            lbeta.append(math.lgamma(ki + alpha) + math.lgamma(ni - ki + beta) - math.lgamma(ni + alpha + beta) + c)
        return np.array(lbeta)
    else:
        res = (math.lgamma(k + alpha) + math.lgamma(n - k + beta) - math.lgamma(n + alpha + beta) + c)
        return res


def get_confusion(yhat, y):
    if len(yhat) != len(y):
        raise NameError('yhat has different length')
    TP = sum(np.array(yhat) & np.array(y))
    predict_pos = np.sum(yhat)
    FP = predict_pos - TP
    TN = len(y) - np.sum(y) - FP
    FN = len(yhat) - predict_pos - TN
    return TP, FP, TN, FN

def t_get_confusion(yhat, y):
    if len(yhat) != len(y):
        raise NameError('yhat has different length')
    TP = len(np.where((np.array(y) == 1) & (np.array(yhat) == 1))[0])
    FP = len(np.where((np.array(y) == 0) & (np.array(yhat) == 1))[0])
    TN = len(np.where((np.array(y) == 0) & (np.array(yhat) == 0))[0])
    FN = len(np.where((np.array(y) == 1) & (np.array(yhat) == 0))[0])
    un_pos = len(np.where((np.array(y) == 1) & (np.array(yhat) == -1))[0])
    un_neg = len(np.where((np.array(y) == 0) & (np.array(yhat) == -1))[0])
    return TP, FP, TN, FN, un_pos, un_neg

def extract_rules(tree, feature_names):
    left = tree.tree_.children_left
    if left[0] == -1:
        return [sample(list(feature_names), 1)]
    right = tree.tree_.children_right
    features = [feature_names[i] for i in tree.tree_.feature]
    idx = np.where(left == -1)[0]

    def recurse(left, right, child, lineage=None):
        if lineage is None:
            lineage = []
        if child in left:
            parent = np.where(left == child)[0].item()
        else:
            parent = np.where(right == child)[0].item()
        lineage.append(features[parent])
        if parent == 0:
            lineage.reverse()
            return lineage
        else:
            return recurse(left, right, parent, lineage)

    rules = []
    for child in idx:
        rule = []
        # in case the tree is empty
        if len(left) > 1:
            for node in recurse(left, right, child):
                rule.append(node)
            rules.append(rule)
        else:
            pass
    return rules


def accumulate(iterable, func=operator.add):
    it = iter(iterable)
    total = next(it)
    yield total
    for element in it:
        total = func(total, element)
        yield total


def find_lt(a, x):
    # 合适的插入点索引，使得数组有序
    i = bisect_left(a, x)
    if i:
        return int(i - 1)
    else:
        return 0


def remove_duplicates(l):
    elements = {}
    for element in l:
        elements[element] = 1
    return list(elements.keys())


def find_interval(idx1, l2):
    '''This function takes a index
    of the list of all the elements,
    and a list of length
    of each type of elements.
    returns a idx2 for the list of length
    '''
    idx2 = 0
    tmp_sum = 0
    for i in l2:
        tmp_sum += i
        if tmp_sum >= idx1 + 1:
            return idx2
        else:
            idx2 += 1


# 根据字典的值value获得该值对应的key
def get_dict_key(tp_difference, tn_difference, tp_lens, tn_lens):
    tp_keys = list(tp_difference.keys())
    tn_keys = list(tn_difference.keys())
    idx = []
    tn_idx = []
    if tp_lens != [] and tn_lens != []:
        tp_idx = np.where(np.array(tp_lens) >= (np.nanmax(tp_lens) * 0.7))[0]
        tn_idx = np.where(np.array(tn_lens) >= (np.nanmax(tn_lens) * 0.7))[0]
        idx = np.intersect1d(tp_idx, tn_idx, assume_unique=True).tolist()
    elif tp_lens != [] and tn_lens == []:
        idx = np.where(np.array(tp_lens) >= (np.nanmax(tp_lens) * 0.7))[0].tolist()
    elif tp_lens == [] and tn_lens != []:
        tn_idx = np.where(np.array(tn_lens) >= (np.nanmax(tn_lens) * 0.7))[0].tolist()
    key = []
    if idx == 0:
        for i in idx:
            key.append(tp_keys[i])
    else:
        for i in tn_idx:
            key.append(tn_keys[i])
    return key
