#this script is create for ----
__author__ = 'fandongyun'


class DBGlobalSettings():
    """mongodb command line :
        > db
        LogsAllInOne
        > db.LogsAllInOne.findOne()
        {
            "_id" : ObjectId("5315cf9ccbb7040662bb6993"),
            "user_agent_ver" : "1.0.1.008",
            "remote_addr" : "117.55.68.188",
            "log_date" : "2013/11/26",
            "http_uuid" : "-",
            "col_name" : "admin_api_uuid_token",
            "http_session_token" : "-",
            "user_agent" : "13DdnAI"
        }

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
    def __init__(self, hostname = "172.26.178.208",
        db_name = "LogsAllInOne",
        col_name = "LogsAllInOne"):

        self.hostname = hostname
        self.db_name = db_name
        self.col_name = col_name
        self.ipro = "13IprAA"
        self.ddn = "13DdnAI"

