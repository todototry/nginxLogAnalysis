#this script is create for ----
__author__ = 'fandongyun'

#calc all the global stats , number of Logs, test , real log.
# get all the statistical data from the servers.

import DBSetting
from mongobase.Conn import MongodbConn
import datetime
from datetime import timedelta

class GlobalStat():
    """
    get the global statistics for chart module and geraldo report.

    1.total visits
    2.visits per month
    3.
    """
    def __init__(self):
        self.setting = DBSetting.DBGlobalSettings()
        self.conn = MongodbConn(self.setting.db_name, host_name=self.setting.hostname)
        self.collection = self.conn.set_cur_col(self.setting.col_name)

    def total_visit_per_month(self, year, month, day):
        """
        different from the userStat module.
        this function return the HTTP requests that Nginx servers get in One month from start_date.
        """
        dates = []
        delta_one_day = timedelta(1)
        date_begin = datetime.date(year, month, day)

        for i in range(30):
            date_begin += delta_one_day
            dates.append(str(date_begin))

        visits = 0
        for i in range(len(dates)):
            visits += self.collection.find({'log_date': dates[i]}).count()

        return visits

    def total_visit(self):
        return self.collection.find().count()





