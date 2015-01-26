from logfile import LogFilesTarGzGlob, LogDataLineSplit, LogDataStructure
from mongobase import Conn

__author__ = 'pset'

#To save splited log data line to mongodb.

from mongobase.Settings import DBGlobalSettings

from logfile.LogFilesExtractFromGz import GzFileInfo
from logfile.LogFilesExtractFromGz import ExtractFiles


class MongodbSave():
    """
    new connection
    """
    def __init__(self):
        col_names = DBGlobalSettings.col_names
        db_name = DBGlobalSettings.db_name

        self.conn = Conn(db_name)
        self.db = self.conn.get_db()

    """
        save data to mongodb

    """
    def save(self):
        #get one .tar.gz file

        proxy001_tarfiles = LogFilesTarGzGlob.test_glob3()
        tar_num = len(proxy001_tarfiles)

        for i in range(tar_num):
            #get 1 gzfile.
            gzfile = proxy001_tarfiles[i]

            #gzfile open.
            gzfileinfo = GzFileInfo(gzfile)
            gzfile = ExtractFiles(gzfileinfo.gzfilename)

            print "gzfileinfo: " + gzfileinfo.gzfilename

            #log file extract one by one
            for extractedfileobj in gzfile.extract_files():

                cur_file = gzfile.cur_extract_file

                print cur_file
                #db collection resetting.
                table = self.conn.set_cur_col(cur_file)

                log_data = LogDataLineSplit(extractedfileobj)

                for data in log_data.read_line():
                    #build structure
                    item = LogDataStructure(data).log_data
                    item.__setitem__("log_server", gzfileinfo.log_server)
                    item.__setitem__("log_date", gzfileinfo.log_date)
                    table.insert(item)




if __name__ == "__main__":
    MongodbSave().save()




"""
#block 0
         remote_addr
         remote_user
         time_local
         time_zone

#block 1
         requestmethod
         requesturl
         requestprotocal

#block 2
         status
         body_bytes_sent

#block 3
        http_referer

#block 4

        #block 5
        http_user_agent
        http_user_agent_version
        http_user_agent_addtionalinfo

#block 6

#block 7
         http_x_forwarded_for

#block 8
        logdataline.server_name
         proxy_host
         upstream_addr
         http_uuid
         http_session_token

"""

