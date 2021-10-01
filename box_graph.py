# Basic line graph with python and pygal
# Requirements pygal, pandas, openpyxm
import pygal
from pygal.style import Style
import pandas as pd

# Variables
source = 'metrics.xlsx'
x_label = "Month"
y_label = "SLA % Made"
title_label = "Monthly SLA's"

# Import from an excel file
metrics = pd.read_excel(source, sheet_name='box')

# Get the data from the sheet
january = list(metrics['January'])
february = list(metrics['February'])
march = list(metrics['March'])

# Box Plot Graph modes
# 1.5 interquartile range - box_plot = pygal.Box(box_mode="1.5IQR")
# Tukey = box_plot = pygal.Box(box_mode="tukey")
# Standard deviation - box_plot = pygal.Box(box_mode="stdev")
# Population standard deviation - box_plot = pygal.Box(box_mode="pstdev")

# Graph parameters
box_plot = pygal.Box(box_mode="stdev")
box_plot.title = 'Q1 Metrics Results'
box_plot.add('January', january)
box_plot.add('February', february)
box_plot.add('March', march)

# box_plot.render()
box_plot.render_to_file('box_graph_image.svg')
