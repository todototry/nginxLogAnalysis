__author__ = 'pset'

#To save data from DataSplit.py Module.


from pymongo import MongoClient

from DataSplit import SplitLogData
from ExtractLogFilesFromGz import GzFileInfo
from ExtractLogFilesFromGz import ExtractFiles


#connection settings
client = MongoClient(host="localhost", port=27017)
db = client.originaldata

#get one .tar.gz file
import TarGzFiles
proxy001_tarfiles = TarGzFiles.test_glob()

#get 1 gzfile.
gzfile = proxy001_tarfiles[0]

#gzfile open.
gzfileinfo = GzFileInfo(gzfile)
gzfile = ExtractFiles(gzfileinfo.gzfilename)

#gzfile extract
for extractedfileobj in gzfile.extract_files():

    cur_file = gzfile.extract_files

    #db table resetting.
    table = db.logtable

    logdataline = SplitLogData(extractedfileobj)

    for i in logdataline.readline():
        #save to mongo
        item = {"remote_addr":i.remote_addr,
                "remote_user":i.remote_user
        }

        table.insert(item)


print "gzfileinfo: " + gzfileinfo.log_server + gzfileinfo.log_date




#data location
'''
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

'''

