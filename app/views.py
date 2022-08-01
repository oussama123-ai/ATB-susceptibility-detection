from flask import render_template, request
from flask import redirect, url_for
import os
# Import the necessary modules
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d  import Axes3D
import pandas as pd
import numpy as np 
from scipy.stats import norm
import statistics 
import seaborn as sns
from PIL import Image
from app.utils import pipeline_model
from app.utils import pipeline
from app.utils import pipelineMod1
from app.utils import pipelineMod2
from app.utils import dessMod1
from app.utils import dessMod2
from app.utils import filesMod1
from app.utils import filesMod2
from app.utils import statist1Mod1
from app.utils import statist2Mod1
from app.utils import statist3Mod1
from app.utils import statist4Mod1
from app.utils import statist5Mod1
from app.utils import statist6Mod1
from app.utils import statist1Mod2
from app.utils import statist2Mod2
from app.utils import statist3Mod2
from app.utils import statist4Mod2
from app.utils import statist5Mod2
from app.utils import statist6Mod2
import astimp
import astimp_tools
draw = astimp_tools.draw
import csv
import cv2
UPLOAD_FLODER = 'static/uploads'
SAVE_FOLDER = 'static/files'

def index():
    return render_template('index.html')

def about():
    return render_template('about.html')

def contact():
    return render_template('contact.html')

def upload():
    return render_template('upload.html')
    
    
def getwidth(path):
    img = Image.open(path)
    size = img.size # width and height
    aspect = size[0]/size[1] # width / height
    w = 300 * aspect
    return int(w)

def predct():
 
    if request.method == "POST":
        f = request.files['image']
        filename=  f.filename
        path = os.path.join(UPLOAD_FLODER,filename)
        f.save(path)
        w = getwidth(path)
        # prediction (pass to pipeline model)
        pipeline_model(path,filename,color='bgr')
        stra= pipelineMod1(path,filename,color='bgr')
        stra1= pipeline(path,filename,color='bgr')
        dessMod1(path,filename,color='bgr')
        ch=filesMod1(path,filename,color='bgr')
        ch1=statist1Mod1(ch)
        ch2=statist2Mod1(ch)
        ch3=statist3Mod1(ch)
        ch4=statist4Mod1(ch)
        ch5=statist5Mod1(ch)
        ch6=statist6Mod1(ch)
        ff=filename
        filename=""
        plt.close()
        return render_template('predct.html',fileupload=True,img_name=ff, w=w,message=stra,mess1=stra1,file_name=ch,img_name1=ch1,img_name2=ch2,img_name3=ch3,img_name4=ch4,img_name5=ch5,img_name6=ch6)

    return render_template('predct.html',fileupload=False,img_name="freeai.png")
    
def predct1():
 
    if request.method == "POST":
        f1 = request.files['image']
        filename=  f1.filename
        path = os.path.join(UPLOAD_FLODER,filename)
        f1.save(path)
        w = getwidth(path)
        # prediction (pass to pipeline model)
        pipeline_model(path,filename,color='bgr')
        stra= pipelineMod2(path,filename,color='bgr')
        stra1= pipeline(path,filename,color='bgr')
        dessMod2(path,filename,color='bgr')
        ch=filesMod2(path,filename,color='bgr')
        ch1=statist1Mod2(ch)
        ch2=statist2Mod2(ch)
        ch3=statist3Mod2(ch)
        ch4=statist4Mod2(ch)
        ch5=statist5Mod2(ch)
        ch6=statist6Mod2(ch)
        ff=filename
        filename=""
        plt.close()
        return render_template('predct1.html',fileupload1=True,img_name=ff, w=w,message=stra,mess1=stra1,file_name=ch,img_name1=ch1,img_name2=ch2,img_name3=ch3,img_name4=ch4,img_name5=ch5,img_name6=ch6)

    return render_template('predct1.html',fileupload1=False,img_name="freeai.png")
