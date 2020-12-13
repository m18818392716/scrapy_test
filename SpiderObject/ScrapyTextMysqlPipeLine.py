#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/13 13:16
# @Author  : Susanna
# @Email   : m18818392716@163.com
# @File    : ScrapyTextMysqlPipeLine.py
# @Software: PyCharm

import pymysql

class ScrapyTextMysqlPipeLine(object):
    #__init__函数里面初始化就是连接数据库，便于实现增删改查
    def __init__(self):
        # connection database
        self.connect = pymysql.connect('localhost', 'root', '', 'test')# 后面三个依次是数据库连接名、数据库密码、数据库名称
        # get cursor
        self.cursor = self.connect.cursor()
        print("连接数据库成功")

    def process_item(self, item, spider):
        print("开始输入数据")
        print(item['申报要素'])
        try:
            self.cursor.execute("insert into test(申报要素, hscode, 申报名称, 参考均价, 参考最高价, 参考最低价) values (%s, %s, %s, %s, %s, %s)", (item['申报要素'], item['hscode'], item['申报名称'], item['参考均价'], item['参考最高价'], item['参考最低价']))
            self.connect.commit()
        except Exception as error:
            #print error
            print(error)
        return item