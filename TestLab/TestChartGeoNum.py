#-*- encoding=utf-8 -*-
#this script is create for ----
__author__ = 'fandongyun'

from charts import ChartGeoNum

if __name__ == "__main__":
    city_name = [u'福冈',u'川崎',u'神户',u'名古屋',u'大阪',u'仙台',u'广岛',u'北九州',u'京都',u'冈山',u'扎幌',u'东京']
    lon = [ 33.39, 35.32, 34.41,35.1,   34.4,  38.16, 34.23,33.52,  35,    34.4,  43.05, 35.41]
    lat = [130.21, 139.43, 135.1, 136.55, 135.3, 140.52, 132.27, 130.49, 135.45, 133.54, 141.21, 139.44]
    num = [333,124,555,324,330,656,876,914,154,876,908,924]
    ChartGeoNum.plot_geo_num(lat,lon,city_name,num)
