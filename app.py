from flask import Flask, render_template, send_file, make_response, url_for, Response
import io
import random
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')

from static.covid_data import *


app = Flask(__name__)



@app.route('/')
def main():
    return render_template('main.html')


@app.route('/plot.png')
def plot_png():
    fig = male_vaccination()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/plot1.png')
def plot_png1():
    fig = female_vaccination()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/plot2.png')
def plot_png2():
    fig = transgender_vaccination()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')
    
@app.route('/plot3.png')
def plot_png3():
    fig = state_1stdose()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/plot4.png')
def plot_png4():
    fig = state_2nddose()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/plot5.png')
def plot_png5():
    fig = covishield()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/plot6.png')
def plot_png6():
    fig = covaxin()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')    
    
# app.run(debug=True)       

if __name__ == "__main__":
     app.run(debug=True)  
    #  port = int(os.environ.get('PORT', 33507))
    #  waitress.serve(app, port=port)