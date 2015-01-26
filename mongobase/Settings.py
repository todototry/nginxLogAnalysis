#this script is create for ----
__author__ = 'fandongyun'


class DBColNames():
    def __init__(self):
        self.__dict__ = {
            "sns_uuid_token": "sns_uuid_token",
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

    def col_names(self):
        return self.__dict__.keys()


class DBGlobalSettings():
    hostname = "172.26.178.208"
    db_name = "NginxEventLog"
    col_names = DBColNames().col_names()


if __name__ == "__main__":
    import pprint
    pprint.pprint(DBColNames().__dict__)