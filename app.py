from flask import Flask
from flask.templating import render_template
import pygal
from pygal.style import Style
import pandas as pd


app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("welcome.html")


@app.route("/line_graph")
def line_graph():
    # Variables
    source = 'metrics.xlsx'
    x_label = "Month"
    y_label = "SLA % Made"
    title_label = "Monthly SLA's"

    # Import from an excel file
    metrics = pd.read_excel(source, sheet_name='line_graph')

    # Get the data from the sheet
    months = list(metrics['month'])
    response = list(metrics['response'])
    resolution = list(metrics['resolution'])

    # Create artificial data for details
    target = [None]*len(months)
    minimum = [None]*len(months)
    target[0] = .95
    target[-1] = .95
    minimum[0] = .90
    minimum[-1] = .90

    # Set the chart options and colors
    CustomStyle = Style(colors=['#3352ff', '#9E23FF', '#E5E21A', "#F8492D"])
    line_chart = pygal.Line(style=CustomStyle, x_title=x_label,
                            y_title=y_label, x_label_rotation=-40)

    # Generate the chart
    line_chart.title = title_label
    line_chart.x_labels = map(str, months)
    line_chart.add('Response', response)
    line_chart.add('Resolution', resolution)
    line_chart.add('Target', target, show_dots=False)
    line_chart.add('Minimum', minimum, show_dots=False)
    line_chart.range = [.5, 1]
    graph_data = line_chart.render_data_uri()
    return render_template("graphing.html", graph_data=graph_data)

if __name__ == "__main__":
    app.run(debug=True, port=5050, host="127.0.0.1")