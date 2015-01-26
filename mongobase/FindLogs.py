
__author__ = 'fandongyun'

#this script is created for read data from mongodb.

import pymongo
from mongobase.Settings import DBGlobalSettings as settings
from mongobase import Conn

class FindSpecLog():
    """

    """
    def __init__(self):
        self.conn = Conn.MongodbConn(db_name=settings().db_name)
        self.db = self.conn.get_db()

    def find_count_of_total_col(self, col_name):
        """
        return a dic that stores the (col_name: logNum).
        """
        return self.conn.set_cur_col(col_name).find().count()

    def find_count_of_test_case(self,col_name):
        """
            find the test data.

            distinct_clients:
                "-",
                "13DdnAI",
                "13IprAA",
                "Java",
                "LG",
                "Mozilla",
                "Python-urllib",
                "TEST_13IprAA",
                "Wget",
                "curl"
        """
        distinct_clients = self.conn.set_cur_col(col_name).distinct("user_agent")
        distinct_clients.remove("13DdnAI")
        distinct_clients.remove("13IprAA")
        test_data_num = 0

        for item in range(len(distinct_clients)):
            test_data_num += self.conn.set_cur_col(col_name).find({"user_agent": item}).count()

        return test_data_num

    def stats_of_col(self, col_name):
        all = self.find_count_of_total_col(self, col_name)
        test = self.find_count_of_test(self,col_name)
        return all, test, all-test


    def distinct_count_of_uuid(self, col_name):
        """
        find the distinct count of uuid.
        """
        self.conn.set_cur_col(col_name).distinct().length


    def distinct_of_uuid(self, col_name):
        """
        find the distinct count of uuid.
        """
        pass

    def uuid_frequency(self, col_name):
        """
        frequency of dayly login uuid number .
        data structure:
        uuid: number of login times.
        """
        pass


    def distinct_count_of_session(self, col_name):
        """

        """
        pass


    def distinct_count_of_ip(self, col_name):
        """

        """
        pass

    def find_all(self, col_name):
        return self.conn.set_cur_col(col_name).find()


    def find_ip_date_uuid_session_agent_ver(self, col_name):
        """
        the original data structure !

        {
         "_id" : ObjectId("5315d031cbb7040662bde988"),
         "user_agent_ver" : "-",
         "http_uuid" : "-",
         "user_agent_info" : "-",
         "remote_user" : "-",
         "server_name" : "-",
         "remote_addr" : "10.20.30.250",
         "response_status" : "400",
         "request_method" : "-",
         "body_bytes_sent" : "0",
         "http_x_forwarded_for" : "-",
         "log_server" : "pxy001",
         "http_session_token" : "-",
         "request_url" : "-",
         "http_referer" : "-",
         "log_date" : "2013/11/26",
         "proxy_host" : "-",
         "time_zone" : "+0900",
         "user_agent" : "-",
         "time_local" : "25/Nov/2013:03:28:51",
         "upstream_addr" : "-",
         "request_protocol" : "-"
         }
        """

        return self.conn.set_cur_col(col_name).find({}, {'remote_addr':1, 'log_date':1, 'http_uuid':1, 'http_session_token':1, 'user_agent':1, 'user_agent_ver':1 })
