#-*- encoding=utf-8 -*-
#this script is created for ----
__author__ = 'fandongyun'

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np


def plot_geo_num(lat=None, lon=None, city_name=None, num=None, title = u"Users Dist In Japan", file_name ="distribution_of_users_in_japan.jpg"):
    """
    return the ploted jpg based on the city location and users nums.

    *params*
    lat : list of latitude
    lon : list of longitude
    city_name : list of city name (remember to filter the cities outside of Japan)
    num : list of user num
    """

    #緯度北緯20°～46°，經度東經122°～154°。

    plt.figure(figsize=(8, 8), dpi=100)

    #plt.subplots_adjust(left=0,  top=0)

    plt.subplots_adjust(left=0, right=1, top=1, bottom=0, wspace=0, hspace=0)

    map = Basemap(llcrnrlon=128, llcrnrlat=30, urcrnrlon=148, urcrnrlat=46)
    map.bluemarble()

    #draw dots on the map to represent the user_num of that region.
    size_factor = 580.0
    y_offset = -0.7
    rotation = 3

    for x, y, city, n in zip(lat, lon, city_name, num):
        size = size_factor*n/sum(num)
        cs = map.scatter(x, y, s=size, marker='o',color='#FF5600')
        plt.text(x, y+y_offset, city+":"+str(n), rotation=rotation, fontsize=10)

    plt.title(title)
    #plt.tight_layout()

    plt.savefig("./output/"+file_name)
    if __name__ == "__main__":
        plt.show()

def plot_global_geo_num(lat=None, lon=None, city_name=None, num=None, title = u"日本用户分布图", file_name ="distribution_of_users_in_japan.jpg"):
    """
    return the ploted jpg based on the city location and users nums.

    *params*
    lat : list of latitude
    lon : list of longitude
    city_name : list of city name (remember to filter the cities outside of Japan)
    num : list of user num
    """

    #TODO red

    return NotImplemented


if __name__ == "__main__":
    city_name = [u'福冈',u'川崎',u'神户',u'名古屋',u'大阪',u'仙台',u'广岛',u'北九州',u'京都',u'冈山',u'扎幌',u'东京']
    lon = [33.39, 35.32, 34.41, 35.1, 34.4, 38.16, 34.23, 33.52,  35, 34.4,  43.05, 35.41]
    lat = [130.21, 139.43, 135.1, 136.55, 135.3, 140.52, 132.27, 130.49, 135.45, 133.54, 141.21, 139.44]
    num = [333, 124, 555, 324, 330, 656, 876, 914, 154, 876, 908, 924]
    plot_geo_num(lat, lon, city_name, num)
