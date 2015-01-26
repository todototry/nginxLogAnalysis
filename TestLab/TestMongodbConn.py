#this script is create for ----
__author__ = 'fandongyun'


from pymongo import mongo_client


class MongoCon(object):
    def __init__(self):
        '''
        init the common db connection transactions.
        '''
        self.client = mongo_client.MongoClient()
        self.db = self.client.testnginxlog
        self.data_user = None

    @property
    def data(self):
        """
        data() -> dict

        return dict
        """

        self.data_user = {
            "name":"fan",
            "times":12,
            "date":2013/03/05,
            "utc":'25/Nov/2013:18:43:17',
            "xserver":'pxy001'}

        return self.data_user

    def close_con(self):
        """
        close the db connection.
        """
        self.client.close()

    def test_connect(self):
        """
        test_connection and insert action.
        """
        testtable = self.db.testtable

        testtable.insert(self.data)

        print self.client.database_names()
        print self.db.name
        print testtable.name
        print testtable.count()


    def test_flush_data_connect(self):
        """
        test_connection and insert action.
        """
        testtable = self.db.testtable

        for i in xrange(1000000000):
            data_user = {
                "name":"fan"+str(i),
                "times":i,
                "date":2013/03/05,
                "utc":'25/Nov/2013:18:43:17',
                "xserver":'pxy001'}

            testtable.insert(data_user)

        print self.client.database_names()
        print self.db.name
        print testtable.name
        print testtable.count()





    #TODO :
    # use dynamic program style to get collection refer  and store the refers of diff collections.
    #such as db.__getattr__("collection_name")
    # in this way, we can avoid using the dangerous eval() method.
    def test_connect_dynamic_collection(self,col_name):
        """
        test_dynamic_collection_con
        """

        #TODO ------------------------
        #try to use safe coding way instead of the eval() method.
        #TODO end----------------------

        testtable = eval("self.db."+col_name)
        testtable.insert(self.data)

        print testtable.name
        print testtable.count()


if __name__ == "__main__":

    mc = MongoCon()
    mc.test_flush_data_connect()

    mc.close_con()