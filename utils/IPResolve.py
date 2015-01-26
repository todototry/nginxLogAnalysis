#-*- encoding=utf-8 -*-
#this script is create for ----
__author__ = 'fandongyun'

import pycurl
import urllib2
import requests
import json

"""
License code:	LCNSZE46789Z
Service:	IP-GeoLoc™ Geolocation Online Service, Professional Edition
License period:	30 days
Time left:	29 days, 23 hours and 59 minutes
Service access key:	SAK36B8C2K3ZD275E3AZ
url: GET http://api.ipaddresslabs.com/iplocation/v1.7/locateip?key=demo&ip=210.22.109.134&format=XML
"""



class IpLocation():
    def __init__(self, json_data_stream):
        self.resolve_ip_json_data(json_data_stream)


    def get_dict_data(self):

        return self.__dict__

    def resolve_ip_json_data(self, json_data_stream):
        """ resolve the json_data_stream to self property.
        """
        json_data = json.loads(json_data_stream)

        self.ip = json_data['ip_address']

        if json_data['query_status']['query_status_code'] == u'OK':
            self.org = json_data['geolocation_data']['organization']
            self.region = json_data['geolocation_data']['region_name']
            self.city = json_data['geolocation_data']['city']
            self.country = json_data['geolocation_data']['country_name']
            self.latitude = json_data['geolocation_data']['latitude']
            self.longitude = json_data['geolocation_data']['longitude']
            self.isp = json_data['geolocation_data']['isp']
        else:
            self.org = '-'
            self.region = '-'
            self.nation = '-'
            self.latitude = '-'
            self.longitude = '-'
            self.isp = '-'


class IpLocationFetch():
    def __init__(self, ip):
        self.ip = ip
        self.json_data_stream = self.get_ip_location_json()

    def get_ip_location_json(self):
        """ fetch the physical location of 'ip' with the 'auth_key' from website: api.ipaddresslabs.com
        Unicode encoded.
        """

        auth_key = "SAK36B8C2K3ZD275E3AZ"

        #build url
        base_url = self.build_str(auth_key, "json")

        #request
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36"}
        r = requests.get(base_url, headers= headers)

        #fetch data
        json_data_stream = r.text

        #print json_data_stream

        return json_data_stream

    def get_ip_location_xml(self):
        """ fetch the physical location of 'ip' with the 'auth_key' from website: api.ipaddresslabs.com
        Unicode encoded.
        """
        auth_key = "SAK36B8C2K3ZD275E3AZ"

        #build url
        base_url = self.build_str(auth_key, "XML")

        #request
        resp = urllib2.urlopen(base_url)

        #fetch data
        json_data_stream = resp.read()

        return json_data_stream

    def build_str(self, auth_key,data_type):
        """ build the request url for ip to physical location resolution, by the power of ipaddresslabs.com """

        base_url = "http://api.ipaddresslabs.com/iplocation/v1.7/locateip?"

        params = ["key","ip", "format=json"]
        params[0] = "key=" + auth_key
        params[1] = "ip=" + self.ip
        params[2] = "format=" + data_type

        base_url += "&".join(params)
        #print base_url
        return base_url





import json
import pprint

if __name__ == "__main__":
    #x = IpLocationFetch("49.106.192.198").json_data_stream
    x = IpLocationFetch("59.78.181.184").json_data_stream

    dic = IpLocation(x).get_dict_data()

    pprint.pprint(dic)
