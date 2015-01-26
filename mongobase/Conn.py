#this script is create for ----
__author__ = 'fandongyun'

from pymongo import mongo_client

from mongobase.Settings import DBColNames as DBCol
from mongobase.Settings import DBGlobalSettings as settings

class MongodbConn(object):
    def __init__(self, db_name, host_name=settings.hostname):
        """
        init the common db connection transactions.
        """
        self.client = mongo_client.MongoClient(host=host_name)
        self.db = self.client.__getattr__(db_name)

        #init all the collections
        #set attr self.colname = db.col
        self.col_name_dict = DBCol().__dict__

        for i in range(len(self.col_name_dict)):
            self.__setattr__(self.col_name_dict.keys()[i],self.db.__getattr__(self.col_name_dict.values()[i]))

    def get_db(self):
        return self.db

    def close_con(self):
        """
        close the db connection.
        """
        self.client.close()

    def set_cur_col(self,file_name):
        self.cur_col = self.db.__getattr__(file_name)
        return self.cur_col

    def get_next_col(self):
        for col_name in self.col_name_dict:
            yield self.set_cur_col(col_name)

