class ScrapyTextManyMysqlPipeLine(object):
    def __init__(self):

        from SpiderObject.db.DBHelper import TestDBHelper
        self.db = TestDBHelper()

    def process_item(self, item, spider):

        self.db.testInsert(item)
        return item