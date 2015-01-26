#this script is created for ----
__author__ = 'fandongyun'

from mongobase.Conn import MongodbConn
import DBSetting

class ServerStat():
    """

    1.visits per server
    2.distinct user distribution on each server
    3.client type on each server, diff client user likes diff module features.
    4.server fail times. http 400 401 500 503 505
    5.users stay on time.
    6.traffic busy time-line.
    7.
    """
    def __init__(self):
        self.setting = DBSetting.DBGlobalSettings()
        self.conn = MongodbConn(self.setting.db_name, host_name=self.setting.hostname)
        self.collection = self.conn.set_cur_col(self.setting.col_name)

        self.servers = {"sns_uuid_token": "sns_uuid_token",
                        "search_uuid_token": "search_uuid_token",
                        "gis_uuid_token": "gis_uuid_token",
                        "dpa_uuid_token": "dpa_uuid_token",
                        "direction_uuid_token": "direction_uuid_token",
                        "ctm_uuid_token": "ctm_uuid_token",
                        "auth_uuid_token": "auth_uuid_token",
                        "admin_web_uuid_token": "admin_web_uuid_token",
                        "admin_api_uuid_token": "admin_api_uuid_token",
                        "access_uuid_token": "access_uuid_token",
                        "web_uuid_token": "web_uuid_token",
                        "update_uuid_token": "update_uuid_token",
                        "traffic_uuid_token": "traffic_uuid_token",
                        "tile_uuid_token": "tile_uuid_token"
                        }


    def get_log_num_per_server(self, server_name):
        return self.collection.find({"col_name": server_name}).count()


    def visit_flow_of_servers(self):
        # TODO
        return NotImplemented

    def client_visit_dist_on_server(self, server_name):
        """
        client type distribution on specific server_name
        """
        # TODO
        return NotImplemented

    def server_fail_times_per_date(self):
        # TODO
        return NotImplemented

    def traffic_flow_in_one_day(self):
        # TODO
        return NotImplemented

    def traffic_flow_in_month(self):
        # TODO
        return NotImplemented

