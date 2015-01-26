from logfile import LogFilesTarGzGlob

__author__ = 'fandongyun'

#To read Nginx log files which are created by different servers.

import tarfile


class GzFileInfo(object):
    def __init__(self,gzfilename):
        """
        @gzfilename : filename of a targz file.
        """
        self.gzfilename = gzfilename
        self.log_date = self.getlogdate()
        self.log_server = self.getlogserver()


    def getlogserver(self):
        #TODO------ mac or windows.
        #server , date , log type.
        # pxy001-accesslog-20131126.tar.gz

        #on mac platform
        #if platform.system() ==
        return self.gzfilename.split('-')[0].split('/')[-1]
        #else:
        #    return

    def getlogdate(self):
        #server , date , log type.
        # pxy001-accesslog-20131126.tar.gz
        date_no_sep = self.gzfilename.split('-')[2].split('.')[0]
        return date_no_sep[0:4]+"/"+date_no_sep[4:6]+"/"+date_no_sep[6:]



class ExtractFiles(object):
    def __init__(self,targzfile):
        self.gz_file_name = targzfile
        self.cur_extract_file = None


    def extract_files(self):
        """

        @return self.log_date, log_server, cur_extract_file,  and logfile obj.
        """
        gz_file = tarfile.open(name=self.gz_file_name,mode="r:gz")
        n = len(gz_file.getmembers())
        for i in range(n):
            log_file_obj = gz_file.extractfile(gz_file.members[i])
            if gz_file.members[i].name.__contains__("access_"):
                self.cur_extract_file = gz_file.members[i].name.split('.')[1].split('/')[1]
            else:
                print gz_file.members[i].name
                self.cur_extract_file = "_".join(gz_file.members[i].name.split('.')[1].split('/')[1].split('-')[1:])
            yield log_file_obj




def test():
    #get one .tar.gz file
    files = LogFilesTarGzGlob.test_glob()
    gzfile = files[0]


    gzfileinfo = GzFileInfo(gzfile)
    gzfile = ExtractFiles(gzfileinfo.gzfilename)
    extractedfileobj = None

    for i in gzfile.extract_files():
        extractedfileobj = i
        print extractedfileobj.name
        print gzfile.cur_extract_file
        #print gzfile.cur_extract_file.split('.')[1].split('/')[1]


    print "gzfileinfo: " + gzfileinfo.log_server + gzfileinfo.log_date

    return extractedfileobj


if __name__ == "__main__":
    test()