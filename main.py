from flask import Flask
from app import views
from flask import render_template, request
from flask import redirect, url_for
import os
import matplotlib
from PIL import Image
from imageio import imread, imwrite
import matplotlib.pyplot as plt
import astimp
import SEG
import astimp_tools
import SEG_tools
dess = SEG_tools.dess
draw = astimp_tools.draw
import csv
import cv2
# Import the necessary modules
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d  import Axes3D
import pandas as pd
import numpy as np 
from scipy.stats import norm
import statistics 
import seaborn as sns
app = Flask(__name__, static_url_path="/static")
UPLOAD_FOLDER ='static/uploads/'
# APP CONFIGURATIONS
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# url

app.add_url_rule('/', 'index', views.index)
app.add_url_rule('/about', 'about', views.about)
app.add_url_rule('/contact', 'contact', views.contact , methods=['GET', 'POST'])
app.add_url_rule('/upload', 'upload', views.upload)
app.add_url_rule('/upload/predct', 'predct', views.predct, methods=['GET', 'POST'])
app.add_url_rule('/upload/predct1', 'predct1', views.predct1, methods=['GET', 'POST'])
if __name__ == "__main__":
    app.run(threaded=True)
