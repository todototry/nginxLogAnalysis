#this script is create for ----
from mongobase import Conn

__author__ = 'fandongyun'


from utils import IpLocation
from utils import IpLocationFetch

from mongobase.Settings import DBColNames
from pymongo import mongo_client
from requests import ConnectionError


log_conn = Conn("NginxEventLog")
log_db = log_conn.get_db()

client = mongo_client.MongoClient(host= "172.26.178.208")
ip_db = client.__getattr__("IPLocationDB")
ip_db_col_name = "IPLocationInfo"


def find_ip_from_collection(collection_name):
    distinct_ip = log_db.__getattr__(collection_name).distinct("remote_addr")
    print len(distinct_ip)
    return distinct_ip

def is_ip_resolved(ip):
    #TODO
    ip_count = ip_db.__getattr__(ip_db_col_name).find({"ip": ip}).count()
    if ip_count > 0:
        return True
    else:
        return False

def ensureindex():
    #ip_db.__getattr__(ip_db_col_name).ensure_index([("ip", pymongo.ASCENDING)])
    ip_db.__getattr__(ip_db_col_name).ensure_index("ip", unique=True)


def save_to_ip_table():
    col_names = DBColNames().col_names()
    print type(col_names)
    #for i in col names
    ipcount = 0
    stepby = 0
    x = None
    for col_name in col_names:
        print col_name
        for ip in find_ip_from_collection(collection_name= col_name):
            if is_ip_resolved(ip):
                stepby += 1
                if stepby%100 == 0:
                    print "stepby:",stepby
            else:
                try:
                    x = IpLocationFetch(ip).json_data_stream
                except ConnectionError:
                    import time
                    time.sleep(120)
                    x = IpLocationFetch(ip).json_data_stream
                dic = IpLocation(x).get_dict_data()
                ip_db.__getattr__(ip_db_col_name).insert(dic)

                ipcount += 1
                if ipcount%100 == 0:
                    print "ipcount:",ipcount


