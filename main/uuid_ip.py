#this script is create for ----
__author__ = 'fandongyun'

from mongobase.Conn import MongodbConn
from statistic import DBSetting


class User_id_ip_Stat():

    def __init__(self):
        """
        analysis the IP and User & location
        """
        self.setting = DBSetting.DBGlobalSettings()
        self.conn_log = MongodbConn(self.setting.db_name, host_name="172.26.11.127")
        self.collection_log = self.conn_log.set_cur_col(self.setting.col_name)

        self.conn_uuid_ip = MongodbConn("uuid_ip", host_name="172.26.178.208")
        self.collection_uuid_ip = self.conn_uuid_ip.set_cur_col("uuid_ip")

    def update_ip_user_count(self):
        import time
        start = time.time()
        log_num = 0
        #log_db.__getattr__(collection_name).distinct("remote_addr")
        for log_data in self.collection_log.find({"user_agent": {"$in": ["13DdnAI","13IprAA"]}}, {"remote_addr": 1, "http_uuid": 1}).distinct("http_uuid"):
            print log_data
            #self.collection_uuid_ip.insert(log_data)
            log_num += 1
            if log_num % 10000 == 0:
                print log_num, "% ", log_num/32000000., time.time()-start, log_num/(time.time()-start)


if __name__ == "__main__":
    User_id_ip_Stat().update_ip_user_count()

