#this script is create for ----
__author__ = 'fandongyun'

from mongobase import FindLogs
from mongobase import Settings
from mongobase import Conn


class IntegrateLogWithIPLocation():
    """
    new connection
    """
    def __init__(self):

        logs_db_name = "LogsAllInOne"
        self.conn_logs_all_in_one = Conn.MongodbConn(logs_db_name, host_name= "172.26.11.127")

        ip_db = "IPLocationDB"
        self.conn_ip_location = Conn.MongodbConn(ip_db, host_name="172.26.178.208")
        self.ip_db_col_name = "IPLocationInfo"



        logs_with_ip_db = "LogsWithIPLocation"
        self.conn_log_with_ip = Conn.MongodbConn(logs_with_ip_db, host_name="127.0.0.1")

        #self.db = self.conn.get_db()

    def save(self):
        """
        > db.IPLocationInfo.findOne()
        {
            "_id" : ObjectId("531f0553cbb70408c92d8f8d"),
            "city" : "-",
            "ip" : "1.114.138.80",
            "region" : "-",
            "isp" : "eMobile",
            "longitude" : 139.69,
            "country" : "Japan",
            "latitude" : 35.69,
            "org" : "eAccess Ltd."
        }

        426884
        596959

        """
        import time

        start = time.time()
        log_num = 0
        for data in self.conn_logs_all_in_one.set_cur_col("LogsAllInOne").find().skip(426885):
            log_num += 1
            if log_num % 10000 == 0:
                print log_num, "% ", log_num/32000000. , time.time()-start, log_num/(time.time()-start)

            ip_info = self.conn_ip_location.set_cur_col(self.ip_db_col_name).find_one({"ip": data["remote_addr"]})

            if ip_info != None:
                if ip_info.has_key("city"):
                    data.__setitem__("city", ip_info["city"])
                    data.__setitem__("region", ip_info["region"])
                    data.__setitem__("isp", ip_info["isp"])
                    data.__setitem__("longitude", ip_info["longitude"])
                    data.__setitem__("country", ip_info["country"])
                    data.__setitem__("latitude", ip_info["latitude"])
                    data.__setitem__("org", ip_info["org"])
                    data.__delitem__("_id")
                else:
                    pass
            self.conn_log_with_ip.set_cur_col("LogsWithIPLocation").insert(data)


if __name__ == "__main__":
    IntegrateLogWithIPLocation().save()