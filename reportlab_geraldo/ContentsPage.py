#coding:utf-8
#this script is create for ----
__author__ = 'fandongyun'

import os

cur_dir = os.path.dirname(os.path.abspath(__file__))

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import red, green, black, white
from reportlab.lib.enums import TA_CENTER,TA_JUSTIFY,TA_LEFT,TA_RIGHT

from geraldo import Report
from geraldo import ReportBand
from geraldo import SystemField
from geraldo import BAND_WIDTH
from geraldo import Label
from geraldo import Line
from geraldo import Image
from geraldo import ObjectValue
from geraldo.generators import PDFGenerator, ReportGenerator

class ContentsPageReport(Report):
    additional_fonts = {
        'wqy': '/Users/pset/Downloads/wqy-microhei/wqy-microhei.ttc'
    }

    default_style = {'fontName': 'wqy'}

    title = u'Global Statistics(数据全局概况)'

    class band_page_header(ReportBand):
        height = 1.5*cm
        elements = [
            SystemField(expression='%(report_title)s', top=0*cm,
                left=0, width=BAND_WIDTH, style={'fontName': 'wqy',
                'fontSize': 14, 'alignment': TA_CENTER}),
            # .本文档主要内容包括-全局用户访问统计，用户地理位置分布，用户活跃度图表，客户端分布，客户端版本分布，服务器访问量分布。
            Label(text=u'本文档主要内容包括: 全局用户访问统计， 用户地理位置分布，客户端分布分析，服务器访问量分布。', top=0.9*cm, left=0, width=BAND_WIDTH),
        ]
        borders = {'bottom': False}

    class band_begin(ReportBand):
        height = 4.0*cm
        elements = [
            # Write the contents outline of this document.
            Label(text=u"目录", top=1.2*cm, left=0*cm, width=BAND_WIDTH, style={"alignment": TA_CENTER, "fontSize": 14}),

            Line(left=0*cm, top=1.9*cm, bottom=1.9*cm, right=19*cm),

            Label(text=u"I: 全局基本概况.............................................................................................................................................................1", top=2.0*cm, left=0.5*cm, width=BAND_WIDTH, style={"fontName":'wqy'}),
            Label(text=u"II: 服务器访问状况........................................................................................................................................................2", top=2.6*cm, left=0.5*cm, width=BAND_WIDTH),
            Label(text=u"III: 用户分布状况..........................................................................................................................................................3", top=3.2*cm, left=0.5*cm, width=BAND_WIDTH),
            Label(text=u"VI: 客户端分布状况.......................................................................................................................................................4", top=3.8*cm, left=0.5*cm, width=BAND_WIDTH),
            Label(text=u"V: 用户-服务器访问流分析............................................................................................................................................5", top=4.4*cm, left=0.5*cm, width=BAND_WIDTH),

            # Line Separator.
            #Line(left=0*cm, top=4.1*cm, bottom=4.1*cm, right=19*cm),
        ]
        borders = {'bottom': False}


    class band_detail(ReportBand):
        height = 0.5*cm
        elements = [
            #Label(text=u"每日访问量、各服务器访问状况 、客户端分布状况：", top=2.5*cm, left=0, width=BAND_WIDTH),
            #Image(left=0*cm, top=0.3*cm, width=25*cm, filename=os.path.join(cur_dir, '../charts/output/DateNum_wave.jpg')),
            #Image(left=0*cm, top=6.6*cm, width=19*cm, filename=os.path.join(cur_dir, '../charts/output/DateNum_hist.jpg')),
            #Label(text=u"用户访问时序流图： Not Implemented! ", top=14*cm, left=0*cm, width=BAND_WIDTH),
            #Image(left=0*cm, top=11.6*cm, width=25*cm,  filename=os.path.join(cur_dir, '../charts/output/DateNum_hist.jpg')),
        ]

    class band_summary(ReportBand):
        height = 0.5*cm
        elements = [
        ]

    class band_page_footer(ReportBand):
        height = 0.5*cm
        elements = [
            Label(text='Automatically Created by Tools from Map-Team Suntec !', top=0.1*cm, left=0),
            Label(text='Confidential Document, DO NOT SPREAD !', top=0.1*cm,
                  width=BAND_WIDTH, style={'alignment': TA_CENTER, 'textColor': red}),
            SystemField(expression='Page  %(page_number)d / %(page_count)d',
                top=0.1*cm, width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
        ]
        borders = {'top': True}


if __name__ == "__main__":
    ContentsPageReport(queryset={"T": "T"}).generate_under_process_by(PDFGenerator, filename= os.path.join(cur_dir,"output/ContentsPage.pdf"), first_page_num=1)
