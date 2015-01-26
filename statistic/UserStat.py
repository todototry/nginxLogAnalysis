#this script is create for ----
__author__ = 'fandongyun'

from mongobase.Conn import MongodbConn
import DBSetting


class UserStat():

    def __init__(self):
        """
        analysis the IP and User & location
        """
        self.setting = DBSetting.DBGlobalSettings()
        self.conn_log = MongodbConn(self.setting.db_name, host_name="172.26.11.127")
        self.collection_log = self.conn_log.set_cur_col(self.setting.col_name)

        self.conn_ip = MongodbConn("IPLocationUserCount", host_name="172.26.178.208")
        self.collection_ip = self.conn_ip.set_cur_col("IPLocationInfo")

    """
    def update_ip_user_count(self):
        import time
        start = time.time()
        log_num = 0
        for log_data in self.collection_log.find().skip(3914916):
            self.collection_ip.update({"ip": log_data['remote_addr']}, {"$inc": {"quantity": 1}})
            log_num += 1
            if log_num % 10000 == 0:
                print log_num, "% ", log_num/32000000., time.time()-start, log_num/(time.time()-start)
    """

    def geo_global_dist(self):
        """
        find the ip distribution based on users' ip access dist.
        map - reduce :  sum(quantity)

        aggregate( { $group :
                         { _id : "$state",
                           totalPop : { $sum : "$pop" } } },
                       { $match : {totalPop : { $gte : 10*1000*1000 } } } )



        pipe = [
        {'$match':{'_Program':DBRef('Programs',p['_id']),'Duration':{'$gt':0}}},
        {'$group':{'_id':'$_Program', 'AverageDuration':{'$avg':'$Duration'}}}
        ]

        eps = db.Episodes.aggregate(pipeline=pipe)

        print eps['result']

        """
        return self.collection_ip.aggregate([
                {'$match': {'country': 1, 'log_counts': 1}},                          # the data we need .
                {'$group': {'_id': '$country', 'log_counts': {'$sum': '$quantity'}}}  # the calculation formula.
        ])

    def geo_japan_dist(self):
        """
        find out the user distribution in japan.
        """
        return self.collection_ip.aggregate([
                {'$match': {'country': {'$eq': 'japan'}, 'city': 1, 'log_counts': 1}},  # the data we need .
                {'$group': {'_id': '$city', 'log_counts': {'$sum': '$quantity'}}}       # the calculation formula.
        ])

    def daily_visit_dist(self):
        """
        find out the daily visit traffic
        """
        return self.collection_log.aggregate([
                {'$match': {'log_date': 1, 'log_counts': 1}},  # the data we need .
                {'$group': {'_id': '$log_date', 'log_counts': {'$sum': 1}}}       # the calculation formula.
        ])

    def unique_user_visit_dist(self):
        """
        find the unique user dist in each day,

        """
        return self.collection_log.aggregate([
                {'$match': {'http_uuid': 1, 'log_counts': 1}},                      # the data we need .
                {'$group': {'_id': '$log_date', 'log_counts': {'$sum': '$http_uuid'}}}       # the calculation formula.
        ])


    def unique_session_dist(self):
        return self.collection_log.aggregate([
                {'$match': {'log_date': 1, 'log_counts': 1}},                      # the data we need .
                {'$group': {'_id': '$http_uuid', 'log_counts': {'$sum': '$http_session'}}}       # the calculation formula.
        ])


    def frequency_login_dist(self):
        return self.collection_log.aggregate([
                {'$match': {'log_date': 1, 'log_counts': 1}},                      # the data we need .
                {'$group': {'_id': '$http_uuid', 'log_counts': {'$sum': 1}}}       # the calculation formula.
        ])


if __name__ == "__main__":
    #UserStat().update_ip_user_count()
    """
    num = 0

    s = UserStat()

    for x in s.collection_ip.find({}, {"quantity": 1}):
        if x.has_key('quantity'):
            num += x['quantity']

    print num
    """
