# coding=utf-8
#导入模块
from pymongo import MongoClient
#建立Mongodb数据库连接
class Conn:
    def __init__(self):
        self.client=MongoClient('localhost',12205)
        #test为数据库
        # db=client.test


    def drop(self,m):
        # m为数据库
        db = self.client.m
        # m为集合，相当于表名
        collection = db.m
        # 删除集合collection中的所有数据
        collection.remove()
        # 关闭连接
        self.client.close()


        # #插入集合数据
        # collection.insert({"title":"test"})
        #打印集合中所有数据
        #for item in collection.find():
        #     print(item)
        # #更新集合里的数据
        # collection.update({"title":"test"},{"title":"this is update test"})
        #查找集合中单条数据
        #print collection.find_one()
        #删除集合collection中的所有数据
        #collection.remove()
        #删除集合collection
        #collection.drop()

if __name__ == '__main__':
    Conn().drop("user")
