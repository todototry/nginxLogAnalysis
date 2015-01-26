#coding:utf-8
#this script is created for ----
__author__ = 'fandongyun'


import os

cur_dir = os.path.dirname(os.path.abspath(__file__))

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.lib.colors import red, black, blue, white

from geraldo import Report, ReportBand, Label, ObjectValue, SystemField,\
    FIELD_ACTION_COUNT, BAND_WIDTH, Image, Line, SubReport

# TODO : change the value in the main function.

global_stat = ['1200', '400', '800']

#

class GlobalReport(Report):
    #additional_fonts = {'wqy': '/Users/pset/Downloads/wqy-microhei/wqy-microhei.ttc'}
    default_style = {'fontName': 'wqy'}

    title = u'Global Statistics(数据全局概况)'

    print Widget().page

    class band_page_header(ReportBand):
        height = 1.5*cm
        elements = [
            SystemField(expression='%(report_title)s', top=0*cm,
                left=0, width=BAND_WIDTH, style={'fontName': 'wqy',
                'fontSize': 14, 'alignment': TA_CENTER}),
            # .本文档主要内容包括-全局用户访问统计，用户地理位置分布，用户活跃度图表，客户端分布，客户端版本分布，服务器访问量分布。
            Label(text=u'本文档主要内容包括: 全局用户访问统计， 用户地理位置分布，客户端分布分析，服务器访问量分布。', top=0.9*cm, left=0, width=BAND_WIDTH),
        ]
        borders = {'bottom': True}

    class band_begin(ReportBand):
        height = 20.1*cm
        elements = [

            # Write the outline for this whole document.
            Label(text=u"目录", top=0.2*cm, left=0*cm, width=BAND_WIDTH, style={"alignment": TA_CENTER, "fontSize": 14}),
            Label(text=u"I: 全局基本概况.............................................................................................................................................................1", top=1.0*cm, left=0.5*cm, width=BAND_WIDTH, style={"fontName":'wqy'}),
            Label(text=u"II: 服务器访问状况........................................................................................................................................................2", top=1.6*cm, left=0.5*cm, width=BAND_WIDTH ),
            Label(text=u"III: 用户分布状况..........................................................................................................................................................3", top=2.2*cm, left=0.5*cm, width=BAND_WIDTH ),
            Label(text=u"VI: 客户端分布状况.......................................................................................................................................................4", top=2.8*cm, left=0.5*cm, width=BAND_WIDTH ),
            Label(text=u"V: 用户-服务器访问流分析............................................................................................................................................5", top=3.4*cm, left=0.5*cm, width=BAND_WIDTH ),

             # Draw the User Dist in Japan.
            Image(left=0*cm, top=4.0*cm,  filename=os.path.join(cur_dir, '../charts/output/distribution_of_users_in_japan.jpg')),

            # Line Separator.
            Line(left=0*cm, top=4.1*cm, bottom=4.1*cm, right=19*cm),

            # Data structure
            Label(text="Total visit", top=4.2*cm, left=0),
            Label(text="Test visit", top=4.2*cm, left=3*cm),
            Label(text="Real visit", top=4.2*cm, left=6*cm),

            # Write the Global Data.
            Label(text=global_stat[0], top=4.7*cm, left=0),
            Label(text=global_stat[1], top=4.7*cm, left=3*cm),
            Label(text=global_stat[2], top=4.7*cm, left=6*cm),

        ]
        borders = {'bottom': True}


    class band_detail(ReportBand):
        height = 0.5*cm
        elements = [
            ObjectValue(attribute_name='id', top=0, left=0),
            ObjectValue(attribute_name='name', top=0, left=3*cm, width=10*cm),
            ObjectValue(attribute_name='lon', top=0, left=6*cm, width=10*cm),
            ObjectValue(attribute_name='lat', top=0, left=9*cm, width=10*cm),
            ObjectValue(attribute_name='num', top=0, left=12*cm, width=10*cm),
        ]

    class band_summary(ReportBand):
        height = 0.5*cm
        elements = [
            Label(text=u"每日访问量、各服务器访问状况 、客户端分布状况：", top=2.5*cm, left=0, width=BAND_WIDTH),
            Image(left=0*cm, top=0.3*cm, width=25*cm, filename=os.path.join(cur_dir, '../charts/output/DateNum_wave.jpg')),
            #Image(left=0*cm, top=6.6*cm, width=19*cm,  filename=os.path.join(cur_dir, '../charts/output/DateNum_hist.jpg')),
            Label(text=u"用户访问时序流图： Not Implemented! ", top=14*cm, left=0*cm, width=BAND_WIDTH),
            Image(left=0*cm, top=11.6*cm, width=25*cm,  filename=os.path.join(cur_dir, '../charts/output/DateNum_hist.jpg')),
        ]


    class band_page_footer(ReportBand):
        height = 0.5*cm
        elements = [
            Label(text='Automatically Created by Tools from Map-Team Suntec !', top=0.1*cm, left=0),
            Label(text='Confidential Document, DO NOT SPREAD !', top=0.1*cm, width=BAND_WIDTH, style={'alignment':TA_CENTER, 'textColor': red}),
            SystemField(expression='Page  %(page_number)d / %(page_count)d',
                top=0.1*cm, width=BAND_WIDTH, style={'alignment': TA_RIGHT}),

        ]
        borders = {'top': True}








id = range(12)
city_name = [u'福冈', u'川崎', u'神户', u'名古屋', u'大阪', u'仙台', u'广岛', u'北九州', u'京都', u'冈山',  u'东京']
lon = [33.39, 35.32, 34.41, 35.1, 34.4, 38.16, 34.23, 33.52,  35, 34.4,  35.41]
lat = [130.21, 139.43, 135.1, 136.55, 135.3, 140.52, 132.27, 130.49, 135.45, 133.54,  139.44]
num = [333, 124, 555, 324, 330, 656, 876, 914, 154, 876,  924]


class MyObj():
    def __init__(self, ids=1, name=2, lon=3, lat= 4, num= 5):
        self.id = ids
        self.name = name
        self.lon = lon
        self.lat = lat
        self.num = num

dataset = []

for i,j,k,l,m in zip(id,city_name,lon,lat,num):
    dataset.append(MyObj(i, j, k, l, m))

print dataset

report = GlobalReport(queryset=dataset)

#PDF generation

from geraldo.generators import PDFGenerator

import ContentsPage

canvas = ContentsPage.ContentsPageReport(queryset={"T": "T"}).generate_by(PDFGenerator, filename=os.path.join(cur_dir, 'output/simple-report.pdf'),
                   encode_to="utf-8",
                   first_page_number=1,
                   return_canvas=True)

#systemfield widget  page_number
# custom first_page_number & self.generator.get_page_count()
report.generate_by(PDFGenerator, canvas=canvas)

