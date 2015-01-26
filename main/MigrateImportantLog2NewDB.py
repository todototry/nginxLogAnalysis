#this script is create for ----
__author__ = 'fandongyun'

from mongobase import FindLogs
from mongobase import Settings
from mongobase import Conn


class MigrateImportantAttribute2NewDB():
    """
    new connection
    """
    def __init__(self):
        col_names = Settings.DBGlobalSettings.col_names
        db_name = "LogsAllInOne"

        self.conn = Conn.MongodbConn(db_name)
        self.db = self.conn.get_db()

    def save(self):
        log_num = 0
        for col_name in Settings.DBColNames().col_names():
            for data in FindLogs.FindSpecLog().find_ip_date_uuid_session_agent_ver(col_name):
                log_num += 1
                if log_num % 1000 == 0:
                    print col_name, log_num
                data.__setitem__("col_name", col_name)
                self.conn.set_cur_col("LogsAllInOne").insert(data)


if __name__ == "__main__":
    MigrateImportantAttribute2NewDB().save()