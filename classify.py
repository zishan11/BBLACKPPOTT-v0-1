# -*- coding: utf-8 -*-
# @Time    : 2018/8/27 上午11:07
# @Author  : shijie luan
# @Email   : lsjfy0411@163.com
# @File    : classify.py
# @Software: PyCharm
import Levenshtein

#基本的类别有17种，需要识别为其中的一种匹配
#大类有很多小类
#小类在交互时，不同的交互阶段也不一样

#应当三种都识别，但是从低到高的顺序做
#采用levenshtein距离的方式进行判别    --->也可用神经网络进行分类，
                                    # 或是用聚类算法，或决策树，这样做的目的是为了不深度解析协议
'''
本模块用的分类方法为字符串相似性度量，而非用机器学习方法
'''
#第一步：准备每类的请求报文,算是模版吧
#模版的格式就按我给的这种，换了就不行了
request_template = [{'request_data':
    'a0a0a0a000012101001e0001001c0001000100030000000100000000000000000000000000000000',
 'response_data': 'a0a0a0a0000421020012000100100001000100030000000200000000',
 'function': 'search'},
{'request_data': ' a0a0a0a000012101001e0001001c0001000100050000000500000000000000000000000000000000',
 'response_data': ' a0a0a0a0000421020012000100100001000100050000000000000000',
 'function': 'delete'},
{'request_data':'a0a0a0a00001010100020001',
 'response_data':'a0a0a0a000040102016800060005000100200008000a00030003000200020000000100010000000100000000000000000000204d000100000002000200000001000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
'function':'connect'},
{'request_data': 'a0a0a0a000012101001e0001001c0001000100180000000000000000000000000000000000000000',
 'response_data': 'a0a0a0a0000421020024000100220001000100180000000000000012040200202030204d4435463331312e303032',
 'function': 'connect1'},
{'request_data': 'a0a0a0a000012101001e0001001c0001000100030000000100000000000000000000000000000000',
 'response_data': 'a0a0a0a0000421020012000100100001000100030000000200000000',
 'function': 'search',
 }]

#第二步：算距离
#加权算法
# def sum_D(D):


def calculateD(example):
    '''
    计算各种距离
    :param example:
    :param request_template:
    :return: 返回跟每个模版比较的加权距离，此处加权较为简单，平均做的
    '''
    # sim = {'hamming':0,'distance':0,'Leven':0,..}
    sim_all = []
    # if example in request_template:
    #     return
    for request_M in request_template:
        if example != request_M['request_data']:
            sim = {'hamming': 0, 'distance': 0, 'Leven': 0,'jaro':0,'jaro_winkler':0,'function':request_M['function'],'sum':0}
            sim['distance'] = 1/Levenshtein.distance(example, request_M['request_data'])
            sim['Leven'] = Levenshtein.ratio(example, request_M['request_data'])
            sim['jaro'] = Levenshtein.jaro(example,request_M['request_data'])
            sim['jaro_winkler'] = Levenshtein.jaro_winkler(example,request_M['request_data'])
            try:
                sim['hamming'] = 1/Levenshtein.hamming(example, request_M['request_data'])
            except ValueError:
                sim['hamming'] = 0

            sim['sum'] = (sim['hamming']+sim['distance']+sim['Leven']+sim['jaro']+sim['jaro_winkler'])/5
            sim_all.append(sim)
        else:
            return [{'hamming': 1, 'distance': 1, 'Leven': 1,'jaro':1,'jaro_winkler':1,'function':request_M['function'],'sum':1}]
        # print(sim)
    return sim_all



# origin_D = calculateD(example,request_template)
# print(origin_D)
'''
测试：

#1)编辑距离
sim = Levenshtein.distance(example,request_template[0]['request_data'])
print(sim)
#2）莱文斯坦比
sim1 = Levenshtein.ratio(example,request_template[0]['request_data'])
print(sim1)
#3)jaro距离
sim2 = Levenshtein.jaro(example,request_template[0]['request_data'])
print(sim2)
#4)jaro-winkler距离
sim3 = Levenshtein.jaro_winkler(example,request_template[0]['request_data'])
print(sim3)
#5)hamming距离
try:
    sim4 = Levenshtein.hamming(example,request_template[1]['request_data'])
    print(sim4)
except ValueError:
    print(0)
# 6)余弦相似性
# sim5 = Levenshtein.
'''
#第三步：加权得距离，返回
def GetFunction(origin_D):
    '''
    计算最接近1的function，并返回
    :param origin_D:
    :return:
    '''
    # for D in origin_D:
    # max()
    max = 0
    func = ''
    for D in origin_D:
        if D['sum']>max:
            max = D['sum']
            func = D['function']
        else:
            pass
    return func


if __name__ == '__main__':
    example = 'a0a0a0a00001010100020002'
    origin_D = calculateD(example)
    print(origin_D)
    function = GetFunction(origin_D)
    print(function)
# calculateD(example,request_template)
# def classify():
