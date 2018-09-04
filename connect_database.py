# -*- coding: utf-8 -*-
# @Time    : 2018/8/21 下午4:25
# @Author  : shijie luan
# @Email   : lsjfy0411@163.com
# @File    : connect_database.py
# @Software: PyCharm

'''
为了标准化，在设计初始阶段，主要分三个模块用来测试；
这是第一个模块，即，与数据库交互的功能部分；
数据库名：fanuc
表名：session
用户名：fanuc
密码：fanuc123
请尽量按照此标准进行
'''

import pymysql



#host=self.hostname, user=self.user,
# passwd=self.password, db=self.db,
#  port=self.port, connect_timeout=conf.timeout,
# use_unicode=True

# host = 'loaclhost'
# user = 'fanuc'
# passwd = 'fanuc123'
# DB = 'fanuc_test'
# port = 3306
config = {
    'host': '127.0.0.1',
    'port': 3306,
    'db':'fanuc',
    'user': 'fanuc',
    'passwd': 'fanuc123',
    'charset':'utf8',
    'cursorclass':pymysql.cursors.DictCursor
    }


def remakeResquest(request_data):
    return '\"' + request_data + '\"'
#测试
# print(remakeResquest('dasaasdasad'))
def createSql(request,flag=1):
    if flag == 1:
        sql = 'select * from session WHERE request_data='
        sql=sql+request+';'
    if flag == 2:
        sql = 'select * from session WHERE functions = '
        sql = sql+request+';'
    return sql

def connectDB(config):
    return pymysql.connect(**config)



def searchData(db,sql_clause):
    # db = connectDB(config)
    cursor = db.cursor()
    #此处应当考虑对符号的转义
    # request = remakeResquest(request_data)
    # sql_clause = createSql(request)
    cursor.execute(sql_clause)
    results = cursor.fetchall()
    return results

# db = connectDB(config)
# def connectDB(config,sql='select * from session;'):
#     db = pymysql.connect(**config)
#     cursor = db.cursor()
#     cursor.execute(sql)
#     results = cursor.fetchall()
#     return db,cursor,results[0]['response_data']
'''
测试代码
sql_test = createSql('\"a0a0a0a00001010100020001\"')
db = pymysql.connect(**config)
cursor = db.cursor()

cursor.execute(sql_test)
results = cursor.fetchall()
print(results[0]['response_data'])
'''
if __name__ =="__main__":
    # db = pymysql.connect("loaclhost", "root",
    #                      "lsj940411", "fanuc")
    # sql_test = createSql('\"a0a0a0a00001010100020001\"')
    # print(sql_test)
    # db,cursor,response_data = connectDB(config,sql=sql_test)
    # sql_test = createSql('\"a0a0a0a00001010100020001\"')
    data = "a0a0a0a00001010100020001"
    #第一步：构建sql语句
    request = remakeResquest(data)
    sql_clause = createSql(request)
    #第二步：连接数据库
    db = connectDB(config)
    # cursor = db.cursor()
    # cursor.execute(sql_test)
    # results = cursor.fetchall()
    #第三步：查询返回数据
    results = searchData(db,sql_clause)
    # print(results)
    print(results[0]['response_data'])
    # print(response_data)
#
#     cursor = db.cursor()
#     cursor.execute(sql_test)
#     result = cursor.fetchall()
#     response_data = result[0][0]
#     print(response_data)
