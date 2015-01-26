#this script is created for ----
__author__ = 'fandongyun'

#  return the data for report charts with proper data schema and data type
#  especially for the 'charts' package.
from mongobase.Conn import MongodbConn
import DBSetting


class ClientStat():
    """

    1.client type distribution
    2.the ddn and ipro distribution
    3.ddn client version distribution
    4.ipro client version distribution

    """
    def __init__(self):
        self.setting = DBSetting.DBGlobalSettings()
        self.conn = MongodbConn(self.setting.db_name, host_name=self.setting.hostname)
        self.collection = self.conn.set_cur_col(self.setting.col_name)

    def client_types(self):
        return self.collection.distinct("user_agent")

    def client_dist(self):
        agent_list = self.client_types()
        client_num_dict = {}
        for i in agent_list:
            n = self.collection.find({"user_agent": i}).count()
            client_num_dict.__setitem__(i, n)
        return client_num_dict

    def client_version(self, client_type):
        return self.collection.find({"user_agent": client_type}).distinct("user_agent_ver")

    def client_version_dist(self, client_type):
        client_type_num = {}
        client_versions = self.client_version(client_type)
        for i in client_versions:
            n = self.collection.find({"user_agent": client_type, "user_agent_ver": i}).count()
            client_type_num.__setitem__(i,n)

        return client_type_num

    def ipro_ddn_dist(self):
        client_distribution = self.client_dist()
        ipro_ddn_num = {}
        ipro_ddn_num.__setitem__("total", sum(client_distribution.values()))
        ipro_ddn_num.__setitem__(self.setting.ipro, client_distribution[self.setting.ipro])
        ipro_ddn_num.__setitem__(self.setting.ddn, client_distribution[self.setting.ddn])

        return ipro_ddn_num

    def ipro_ver_dist(self):
        return self.client_version_dist(self.setting.ipro)

    def ddn_ver_dist(self):
        return self.client_version_dist(self.setting.ddn)

