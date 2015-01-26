#-*-encoding=utf-8-*-
#this script is create for ----
__author__ = 'fandongyun'


"""
A SIMPLE REPORT
===============

This is just a simple report, that uses the Geraldo API to format a report with
the begin, summary, page header, page footer and detail bands.
"""


import os

cur_dir = os.path.dirname(os.path.abspath(__file__))

#from django.contrib.auth.models import Permission

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER, TA_RIGHT

from geraldo import Report, ReportBand, Label, ObjectValue, SystemField,\
    FIELD_ACTION_COUNT, BAND_WIDTH


class PermissionsReport(Report):
    additional_fonts = {
        'wqy': '/Users/pset/Downloads/wqy-microhei/wqy-microhei.ttc'
    }
    default_style = {'fontName': 'wqy'}

    title = u'Permissions list(中文)'


    class band_begin(ReportBand):
        height = 1*cm
        elements = [
            Label(text='Look those permissions please', top=0.1*cm,
                left=8*cm),
        ]

    class band_summary(ReportBand):
        height = 0.7*cm
        elements = [
            Label(text="That's all", top=0.1*cm, left=0),
            ObjectValue(attribute_name='name', top=0.1*cm, left=3*cm,
                action=FIELD_ACTION_COUNT,
                display_format='%s permissions found'),
        ]
        borders = {'all': True}

    class band_page_header(ReportBand):
        height = 1.3*cm
        elements = [
            SystemField(expression='%(report_title)s', top=0.1*cm,
                left=0, width=BAND_WIDTH, style={'fontName': 'Helvetica-Bold',
                'fontSize': 14, 'alignment': TA_CENTER}),
            Label(text="ID", top=0.8*cm, left=0),
            Label(text="Name", top=0.8*cm, left=3*cm),
            Label(text="Longitude", top=0.8*cm, left=6*cm),
            Label(text="Latitude", top=0.8*cm, left=9*cm),
            Label(text="Number", top=0.8*cm, left=12*cm),
        ]
        borders = {'bottom': True}

    class band_page_footer(ReportBand):
        height = 0.5*cm
        elements = [
            Label(text='Created with Geraldo Reports', top=0.1*cm, left=0),
            SystemField(expression='Page # %(page_number)d (%(first_page_number)d ~ %(last_page_number)d, total: %(page_count)d)',
                top=0.1*cm, width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
        ]
        borders = {'top': True}

    class band_detail(ReportBand):
        height = 0.5*cm
        elements = [
            ObjectValue(attribute_name='id', top=0, left=0),
            ObjectValue(attribute_name='name', top=0, left=3*cm, width=10*cm),
            ObjectValue(attribute_name='lon', top=0, left=6*cm, width=10*cm),
            ObjectValue(attribute_name='lat', top=0, left=9*cm, width=10*cm),
            ObjectValue(attribute_name='num', top=0, left=12*cm, width=10*cm),
        ]


id = range(12)
city_name = [u'福冈', u'川崎', u'神户', u'名古屋', u'大阪', u'仙台', u'广岛', u'北九州', u'京都', u'冈山', u'扎幌', u'东京']
lon = [ 33.39, 35.32, 34.41, 35.1, 34.4, 38.16, 34.23, 33.52,  35, 34.4,  43.05, 35.41]
lat = [130.21, 139.43, 135.1, 136.55, 135.3, 140.52, 132.27, 130.49, 135.45, 133.54, 141.21, 139.44]
num = [333, 124, 555, 324, 330, 656, 876, 914, 154, 876, 908, 924]


class MyObj():
    def __init__(self,ids= 1,name= 2,lon= 3,lat= 4,num= 5):
        self.id = ids
        self.name = name
        self.lon = lon
        self.lat = lat
        self.num = num

dataset = []

for i,j,k,l,m in zip(id,city_name,lon,lat,num):
    dataset.append(MyObj(i, j, k, l, m))

print dataset

report = PermissionsReport(queryset= dataset)

#PDF generation

from geraldo.generators import PDFGenerator

report.generate_by(PDFGenerator,
                   filename=os.path.join(cur_dir, 'output/simple-report.pdf'),
                   encode_to="utf-8",
                   first_page_number=5)

#Text generation

from geraldo.generators import TextGenerator

report.generate_by(
    TextGenerator,
    filename=os.path.join(cur_dir, 'output/simple-report.txt'),
    to_printer=False,
    encode_to='utf-8',
    first_page_number=5,
)

#Page with half height (starting page number from default: 1)

report.page_size = (A4[0], A4[1] / 2)

report.generate_by(PDFGenerator, filename=os.path.join(cur_dir, 'output/simple-report-half-height.pdf'))

