from flask import Flask, render_template, send_file, make_response, url_for, Response
import io
import random
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
app = Flask(__name__)

# @app.route("/output")
# def output():
#     output = execute('./static/covid_data.py')
#     return render_template('template_name.html',output=output)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
# def execute():
#     actual_data=pd.read_csv('C:/Users/Nabeel/Desktop/udemy/Python flask/static/covid_19_data.csv', encoding='utf-8')
#     strformat = '<span class="significant">%f</span>'
#     significant = lambda x: strformat % x if x<0.05 else str(x)
#     formatters = {'p_value': significant}
#     x=actual_data.to_html(formatters=formatters, escape=False)
    # print(x)

# @app.route("/")
# def hello_world():
#     actual_data=pd.read_csv('C:/Users/Nabeel/Desktop/udemy/Python flask/static/covid_19_data.csv', encoding='utf-8')
#     return actual_data.info().to_html()

@app.route("/")
def hello():
    return "<p>Hello,asdadasd Nabeel2323!</p>"    

actual_data=pd.read_csv('C:/Users/Nabeel/Desktop/udemy/Python flask/static/covid_19_data.csv', encoding='utf-8')
#dropping_the_column_of_province/state
clean_data=actual_data.drop(['Province/State'],axis=1) #if_deleting_row_give_axis=0
required_data=clean_data.groupby(by=["Country/Region"]).sum()
clean_data['ObservationDate']=pd.to_datetime(clean_data['ObservationDate'])
cases_overtime=clean_data.groupby(by=["ObservationDate"]).sum()
def create_figure():
    fig=plt.figure()
    plt.xlabel("Observation Date")
    plt.ylabel("Deaths")
    cases_overtime.loc['2020-01':'2020-03','Deaths'].plot(figsize=(10, 10))
    return fig

def piechart():
    total_conf=required_data["Confirmed"].sum()
    total_recov=required_data["Recovered"].sum()
    total_deaths=required_data["Deaths"].sum()
    total_active=total_conf-total_recov-total_deaths
    y = [total_active, total_deaths, total_recov]
    fig=plt.figure()
    label = ['total_active', 'total_deaths', 'total_recov']
    plt.pie(y,labels=label,autopct='%1.1f%%')
    plt.title("World Cases")
    return fig


@app.route('/plot.png')
def plot_png():
    fig = piechart()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')
    
# app.run() 
app.run(debug=True)   