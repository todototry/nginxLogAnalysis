# for specified files.
__author__ = 'pset'


class LogDataLineSplit(object):
    def __init__(self,log_file_obj):
        self.logfile = log_file_obj

    def read_line(self):
        while self.logfile.tell() != self.logfile.size:
            dataline = self.logfile.readline()
            data = self.__linsplit(dataline)
            yield data

    def __linsplit(self,dataline):
        """
        #data format:
        #$remote_addr - $remote_user [$time_local] "$request" $status $body_bytes_sent "$http_referer" "$http_user_agent" "$http_x_forwarded_for" $server_name $proxy_host $upstream_addr $http_uuid $http_session_token

        #data type list:

        #1:    $remote_addr
        #2:    -
        #3:    $remote_user
        #4:    [$time_local]
        #5:   "$request"
        #6:    $status
        #7:    $body_bytes_sent
        #8:   "$http_referer"
        #9:   "$http_user_agent"
        #10:  "$http_x_forwarded_for"
        #11:  $server_name
        #12:  $proxy_host
        #13:  $upstream_addr
        #14:  $http_uuid
        #15:  $http_session_token
        """

        #try to split  data line.
        splitednormal1 = dataline.rsplit('"')


        #find out if the rsplit makes the right effect, ----works well for all kinds of data: no matter random ,normal , or broken_data.
        #print len(splitednormal1)


        #print to analyze the splited data list.
        #pprint.pprint(splitednormal1)

        block0 = splitednormal1[0].split()
        block1 = splitednormal1[1].split()
        block2 = splitednormal1[2].split()
        block3 = splitednormal1[3].split()
        #block4 = splitednormal1[4].split()
        block5 = splitednormal1[5].split('/')
        #block6 = splitednormal1[6].split()
        block7 = splitednormal1[7]
        block8 = splitednormal1[8].split()


        #print block0

        #block 0
        self.remote_addr = block0[0]
        self.remote_user = block0[2]
        self.time_local = block0[3].replace('[','')
        self.time_zone = block0[4].replace(']','')

        #block 1
        if len(block1) < 2:
            self.request_method = '-'
            self.request_url = '-'
            self.request_protocol = '-'
        elif len(block1) < 3:
            self.request_method = block1[0]
            self.request_url = block1[1]
            self.request_protocol = "-"
        else:
            self.request_method = block1[0]
            self.request_url = block1[1]
            self.request_protocol = block1[2]

        #block 2
        self.response_status = block2[0]
        self.body_bytes_sent = block2[1]

        #block 3
        self.http_referer = block3[0]

        #block 4

        #block 5
        if len(block5) > 1:
            self.user_agent = block5[0]
            ver_additional = block5[1][:].split()
            if len(ver_additional) > 1:
                self.user_agent_ver = ver_additional[0]
                self.user_agent_info = ver_additional[1]
            else:
                self.user_agent_ver = '-'
                self.user_agent_info = '-'
        else:
            self.user_agent = '-'
            self.user_agent_ver = '-'
            self.user_agent_info = '-'
        #block 6



        #block 7
        self.http_x_forwarded_for = block7[0]

        #block 8
        self.server_name = block8[0]
        self.proxy_host = block8[1]
        self.upstream_addr = block8[2]
        #self.http_uuid = block8[3]
        try :
            self.http_uuid = block8[3]
        except IndexError:
            self.http_uuid = '-'
        try :
            self.http_session_token = block8[4]
        except IndexError:
            self.http_session_token = '-'

        return self


def test():
    #get specific targz file.
    from logfile.LogFilesTarGzGlob import TarGzFilesGlob
    tarfiles = TarGzFilesGlob(r"/Volumes/VMware Shared Folders/fandongyunWin7Share/Nginx data log/proxy001/*20140108.tar.gz").find_all()
    #read targz, return a unziped log_file_obj.
    from logfile.LogFilesExtractFromGz import ExtractFiles
    for fileobj in ExtractFiles(tarfiles[0]).extract_files():
        print fileobj.name
        logdataline = LogDataLineSplit(fileobj)
        for i in logdataline.read_line():
            """
            #show all info:
            #block 0
            print "addr:" + logdataline.remote_addr
            print "user:"+ logdataline.remote_user
            print "time_local: " + logdataline.time_local
            print "time_zone: " + logdataline.time_zone

            #block 1
            print "requestmethod :"  +   logdataline.request_method
            print "request_url :"  +   logdataline.request_url
            print "request_protocol: "  +   logdataline.request_protocol

            #block 2
            print "status :"  +    logdataline.response_status
            print "body_bytes_sent: "  +   logdataline.body_bytes_sent

            #block 3
            print "http_referer:"  +    logdataline.http_referer

            #block 4

            #block 5
            print "http_user_agent:"  +   logdataline.user_agent
            print "http_user_agent_version:"  +   logdataline.user_agent_ver
            print "http_user_agent_addtionalinfo:"  +   logdataline.user_agent_info

            #block 6



            #block 7
            print "http_x_forwarded_for:"  +    logdataline.http_x_forwarded_for

            #block 8
            print "server_name:"  +  logdataline.server_name
            print "proxy_host:"  +   logdataline.proxy_host
            print "upstream_addr:"  + logdataline.upstream_addr
            print "http_uuid:"  +    logdataline.http_uuid
            print "http_session_token:"  +   logdataline.http_session_token

            """


if __name__ == "__main__":
    test()

