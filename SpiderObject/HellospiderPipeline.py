import pymysql.cursors
class HellospiderPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='127.0.0.1',  # 数据库地址
            port=3306,  # 数据库端口
            db='spider',  # 数据库名
            user='root',  # 数据库用户名
            passwd='123456',  # 数据库密码
            charset='utf8',  # 编码方式
            use_unicode=True)
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        # self.cursor.execute("USE tieba")
        #插入数据库
        sql = "insert into articles(title, author, reply) value (%s,%s,%s)"
        try:
            self.cursor.execute(sql, (item['title'], item['author'], item['reply']))
            self.cursor.connection.commit()
        except BaseException as e:
            print("错误在这里>>>>>>>>>>>>>", e, "<<<<<<<<<<<<<错误在这里")
            self.cursor.connection.rollback()
        return item