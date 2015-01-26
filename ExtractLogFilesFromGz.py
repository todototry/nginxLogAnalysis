__author__ = 'fandongyun'

#To read Nginx log files which are created by different servers.

import tarfile
import platform

class GzFileInfo(object):
    def __init__(self,gzfilename):
        """
        @gzfilename : filename of a targz file.
        """
        self.gzfilename = gzfilename
        self.log_date = self.getlogdate(self.gzfilename)
        self.log_server = self.getlogserver(self.gzfilename)
        self.cur_extract_file = None

    def getlogserver(self,filename):
        #TODO------ mac or windows.
        #server , date , log type.
        # pxy001-accesslog-20131126.tar.gz

        #on mac platform
        #if platform.system() ==
        return filename.split('-')[0].split('/')[-1]
        #else:
        #    return

    def getlogdate(self,filename):
        #server , date , log type.
        # pxy001-accesslog-20131126.tar.gz
        date_no_sep = filename.split('-')[2].split('.')[0]
        return date_no_sep[0:4]+"/"+date_no_sep[4:6]+"/"+date_no_sep[6:]



class ExtractFiles(object):
    def __init__(self,targzfile):
        self.gzfilename = targzfile
        self.cur_extract_file = None


    def extract_files(self):
        '''

        @return self.log_date, log_server, cur_extract_file,  and logfile obj.
        '''
        gzfile = tarfile.open(name=self.gzfilename,mode="r:gz")
        n = len(gzfile.getmembers())
        for i in range(n):
            logfileobj = gzfile.extractfile(gzfile.members[i])
            self.cur_extract_file = gzfile.members[i].name.split('.')[1].split('/')[1]
            yield logfileobj




def test():
    #get one .tar.gz file
    import TarGzFiles
    files = TarGzFiles.test_glob()
    gzfile = files[0]


    gzfileinfo = GzFileInfo(gzfile)
    gzfile = ExtractFiles(gzfileinfo.gzfilename)
    extractedfileobj = None

    for i in gzfile.extract_files():
        extractedfileobj = i
        print extractedfileobj.name
        print gzfile.cur_extract_file
        print gzfile.cur_extract_file.split('.')[1].split('/')[1]


    print "gzfileinfo: " + gzfileinfo.log_server + gzfileinfo.log_date

    return extractedfileobj


if __name__ == "__main__":
    test()