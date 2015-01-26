#this script is create for ----
__author__ = 'fandongyun'


from reportlab.graphics import charts

#Chart Classes
#-------------

#The chart base class inherits from Graphic.

from geraldo.charts import BaseChart, Graphic
issubclass(BaseChart, Graphic)


#There are many chart types, but for a while we are going to support only the most
#common, below:

#- Bars (horizontal and vertical, with optional support to 3D)

from geraldo.charts import BarChart

hasattr(BarChart, 'is3d')


hasattr(BarChart, 'horizontal')


#- Line

from geraldo.charts import LineChart

#- Pie

from geraldo.charts import PieChart

#- Doughnut

from geraldo.charts import DoughnutChart

#- Spider

from geraldo.charts import SpiderChart

#Data to test
#------------

from geraldo.cross_reference import CrossReferenceMatrix, CROSS_ROWS, CROSS_COLS

holidays = [
    {'name': 'New year', 'type': 'tradition', 'month': 1, 'day': 1, 'month_name': 'jan'},
    {'name': "Sao Paulo's Birthday", 'type': 'civic', 'month': 1, 'day': 25, 'month_name': 'jan'},
    {'name': 'Carnival', 'type': 'tradition', 'month': 2, 'day': 15, 'month_name': 'feb'},
    {'name': 'Easter', 'type': 'religious', 'month': 3, 'day': 20, 'month_name': 'mar'},
    {'name': 'Discovering Day', 'type': 'civic', 'month': 4, 'day': 22, 'month_name': 'apr'},
    {'name': 'Day of Work', 'type': 'civic', 'month': 5, 'day': 1, 'month_name': 'may'},
    {'name': "Tarsila's Birthday", 'type': 'tradition', 'month': 5, 'day': 9, 'month_name': 'may'},
    {'name': 'Corpus Christi', 'type': 'religious', 'month': 6, 'day': 12, 'month_name': 'jun'},
    {'name': "Marinho's Birthday", 'type': 'tradition', 'month': 7, 'day': 10, 'month_name': 'jul'},
    {'name': "Leticia's Birthday", 'type': 'tradition', 'month': 8, 'day': 10, 'month_name': 'ago'},
    {'name': 'Independence Day', 'type': 'civic', 'month': 9, 'day': 7, 'month_name': 'sep'},
    {'name': 'Election Day', 'type': 'civic', 'month': 10, 'day': 3, 'month_name': 'oct'},
    {'name': "Santa Maria's Day", 'type': 'religious', 'month': 10, 'day': 12, 'month_name': 'oct'},
    {'name': "Goiania's Birthday", 'type': 'civic', 'month': 10, 'day': 24, 'month_name': 'oct'},
    {'name': 'Republic Day', 'type': 'civic', 'month': 11, 'day': 15, 'month_name': 'nov'},
    {'name': 'Christmas', 'type': 'religious', 'month': 12, 'day': 25, 'month_name': 'dec'},
]

cities = [
    {'city': 'New York City', 'state': 'NY', 'state_name': 'New York', 'capital': False, 'population': 8363710, 'area': 468.9, 'government': 'Mayor', 'holidays': holidays},
    {'city': 'Albany', 'state': 'NY', 'state_name': 'New York', 'capital': True, 'population': 95658, 'area': 21.8, 'government': 'Mayor', 'holidays': holidays},
    {'city': 'Austin', 'state': 'TX', 'state_name': 'Texas', 'capital': True, 'population': 757688, 'area': 296.2, 'government': 'Council-manager', 'holidays': holidays},
    {'city': 'Dallas', 'state': 'TX', 'state_name': 'Texas', 'capital': False, 'population': 1279910, 'area': 385.0, 'government': 'Council-manager', 'holidays': holidays},
    {'city': 'Houston', 'state': 'TX', 'state_name': 'Texas', 'capital': False, 'population': 2242193, 'area': 601.7, 'government': 'Mayor-council', 'holidays': holidays},
    {'city': 'San Francisco', 'state': 'CA', 'state_name': 'California', 'capital': False, 'population': 808976, 'area': 231.92, 'government': 'Mayor-council', 'holidays': holidays},
    {'city': 'Los Angeles', 'state': 'CA', 'state_name': 'California', 'capital': False, 'population': 3833995, 'area': 498.3, 'government': 'Mayor-council', 'holidays': holidays},
    {'city': 'Sacramento', 'state': 'CA', 'state_name': 'California', 'capital': True, 'population': 463794, 'area': 99.2, 'government': 'Mayor-council', 'holidays': holidays},
    {'city': 'Seattle', 'state': 'WA', 'state_name': 'Washington', 'capital': False, 'population': 602000, 'area': 142.5, 'government': 'Mayor-council', 'holidays': holidays},
    {'city': 'Washington', 'state': 'DC', 'state_name': 'DC', 'capital': True, 'population': 3602000, 'area': 242.5, 'government': 'Mayor-council', 'holidays': holidays},
]

#cities = CrossReferenceMatrix(cities, 'capital', 'state')
#holidays = CrossReferenceMatrix(holidays, 'type', 'month')

#Report class
#------------

from geraldo import Report, ObjectValue, DetailBand
from geraldo.utils import cm


class MatrixChartsReport(Report):
    title = 'Rendering Matrix Charts'
    borders = {'all': True}

    class band_begin(DetailBand):
        height=12*cm
        elements = [
            PieChart(top=1.3*cm, left=1*cm, height=3*cm, width=5*cm,
                cols_attribute='state', rows_attribute='government',
                cell_attribute='population', action='sum', legend_labels=True,
                slice_popout=2),
            DoughnutChart(top=1.3*cm, left=13*cm, height=3*cm, width=5*cm,
                cols_attribute='state', rows_attribute='government',
                cell_attribute='population', action='sum', summarize_by=CROSS_COLS,
                slice_popout=True),
            LineChart(top=7*cm, left=1*cm, height=3*cm, width=5*cm,
                cols_attribute='state', rows_attribute='government',
                cell_attribute='population', action='sum', legend_labels=True),
            SpiderChart(top=7*cm, left=12*cm, height=3*cm, width=5*cm,
                rows_attribute='capital', cols_attribute='state',
                cell_attribute='area', action='sum'),
        ]

    class band_detail(DetailBand):
        height=12*cm
        elements = [
            ObjectValue(attribute_name='city', left=0.2*cm, style={'fontSize': 12}),
            LineChart(top=1.3*cm, left=3*cm, height=3*cm, width=5*cm,
                data='holidays', cols_attribute='type', rows_attribute='month',
                cell_attribute='day', action='count', summarize_by=CROSS_COLS),
            BarChart(top=1.3*cm, left=10*cm, height=3*cm, width=8*cm,
                data='holidays', rows_attribute='type', cols_attribute='month',
                cell_attribute='day', action='count'),
            BarChart(top=6.3*cm, left=0.5*cm, height=3*cm, width=8*cm,
                data='holidays', rows_attribute='type', cols_attribute='month',
                cell_attribute='day', action='count', horizontal=True,
                axis_labels=True, axis_labels_angle=-20, summarize_by=CROSS_ROWS),
            BarChart(top=8.3*cm, left=12*cm, height=3*cm, width=5*cm,
                data='holidays', rows_attribute='type', cols_attribute='month',
                cell_attribute='day', action='count', is3d=True, axis_labels=True,
                axis_labels_angle=80, summarize_by=CROSS_ROWS),
        ]
        borders = {'top': True}

#Generating the result report

report = MatrixChartsReport(queryset=cities)

#PDF generation

import os
cur_dir = os.path.dirname(os.path.abspath(__file__))

from geraldo.generators import PDFGenerator
report.generate_by(PDFGenerator, filename=os.path.join(cur_dir, 'output/report-with-charts.pdf'))

#Other important elements on this topic
#--------------------------------------

#- Axis, Legends, Title and Colors

#All of above are supported by the following attributes:

hasattr(BaseChart, 'axis_labels')


hasattr(BaseChart, 'axis_labels_angle')


hasattr(BaseChart, 'legend_labels')


hasattr(BaseChart, 'title')


hasattr(BaseChart, 'colors')


#About Colors, it should supports color sets (TODO)

#- Grid (TODO)

#Not yet supported

#- Transparecy (TODO: enhance)

#The transparency is made with colors, like this:

from reportlab.lib.colors import Color, red
red_transparent = Color(red.red, red.green, red.blue, alpha=0.7)

