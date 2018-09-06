# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 上午10:52
# @Author  : shijie luan
# @Email   : lsjfy0411@163.com
# @File    : docker_mysql.py
# @Software: PyCharm
'''
为了标准化，在设计初始阶段，主要分三个模块用来测试；
这是第一个模块，即，与数据库交互的功能部分；
数据库名：fanuc
表名：session
用户名：fanuc
密码：fanuc123
session表的结构为：
请尽量按照此标准进行
'''

import pymysql
import copy
#配置信息]
config = {
    'host': '127.0.0.1',
    'port': 3306,
    # 'db':'fanuc_docker',
    'user': 'root',
    'passwd': '',
    #这是我自己的密码，就是不给你，皮一下很开心
    'charset':'utf8mb4',
    'cursorclass':pymysql.cursors.DictCursor
    }
def changeConfig(config,dbName):
    ConfigForInsert = copy.deepcopy(config)
    ConfigForInsert['db'] = dbName
    return ConfigForInsert


#sql语句构建
def createSql():
    sql = "CREATE DATABASE IF NOT EXISTS "

#连接

def connectMysql(config):
    '''
    这里连接，给个config就行，不管是创建数据库还是数据表
    :param config:
    :return:
    '''
    return pymysql.connect(**config)


#新建数据库
def createDB(con,DBname):
    '''

    :param con: 这是针对连接的，不是针对数据表的
    :param DBname: 字符串，要建的数据库名
    :return:
    '''
    sql = "CREATE DATABASE IF NOT EXISTS " + DBname
    cur = con.cursor()
    try:
        cur.execute(sql)
        print("数据库%s创建成功"%DBname)
    except:
        print("已存在")

#新建数据表
def createTable(db,TableName):
    '''
    传入新的db类和表名
    :param db:
    :param TableName:
    :return:
    '''
    sql = """CREATE TABLE %s(
                 request_data  VARCHAR(3000) NOT NULL,
                 response_data  VARCHAR(3000),
                 functions VARCHAR(45),  
                 session_id INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
                 data DATE)"""%TableName
    # print(sql)
    cur = db.cursor()
    try:
        cur.execute(sql)
        print("数据表%s插入成功"%TableName)
    except:
        print("失败，可能%s该表已存在"%TableName)
#插入数据


def insertDB(DB):
    cur = DB.cursor()
    cur.execute("")
#查询数据


#删除数据库
def dropDB(con,DBname):
    sql = "DROP DATABASE IF EXISTS " + DBname
    cur = con.cursor()
    try:
        cur.execute(sql)
        print("数据库%s删除成功"%DBname)
    except :
        print("已删除")

#删除数据表
def dropTable(db,TableName):
    sql = "DROP TABLE IF EXISTS " + TableName
    cur = db.cursor()
    try:
        cur.execute(sql)
        print("数据表%s删除成功"%TableName)
    except :
        print("该表已删除")

#
if __name__ == '__main__':



    con = connectMysql(config)
    createDB(con,"fanucdocker")

    dbconfig = changeConfig(config, 'fanucdocker')
    db = connectMysql(dbconfig)

    createTable(db,'sessionNew')
    dropTable(db,'sessionNew')
    dropTable(db,'session')
    # dropDB(con,"docker")
    # dropDB(con,"fanucdocker")
    # sql =

