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
# pickle files
font = font = cv2.FONT_HERSHEY_SIMPLEX
def pipeline_model(path,filename,color='bgr'):
    # step-1: read image in cv2
    img = cv2.imread(path)
    # step-2: convert into gray scale
    if color == 'bgr':
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    else:
        gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    
     # step-3: crop the face (using haar cascase classifier)
    petri = astimp.getPetriDish(img)
    crop = petri.img
    circles = astimp.find_atb_pellets(crop)
    pellets = [astimp.cutOnePelletInImage(crop, circle) for circle in circles]
    preproc = astimp.inhib_diam_preprocessing(petri, circles)
    disks = astimp.measureDiameters(preproc)
    plt.figure(figsize=(7,7))
    ast = astimp.AST(img)
    
def pipelineMod1(path,filename,color='bgr'):
    img = cv2.imread(path)
    petri = astimp.getPetriDish(img)
    crop = petri.img
    circles = astimp.find_atb_pellets(crop)
    pellets = [astimp.cutOnePelletInImage(crop, circle) for circle in circles]
    preproc = astimp.inhib_diam_preprocessing(petri, circles)
    disks = astimp.measureDiameters(preproc) 
    labels = [astimp.getOnePelletText(pellet) for pellet in pellets]
    ch= []
    for label in labels:
        ch.append(str(label.text))
    return ch
def pipelineMod2(path,filename,color='bgr'):
    img = cv2.imread(path)
    petri = SEG.getPetriDish(img)
    crop = petri.img
    circles = SEG.find_atb_pellets(crop)
    pellets = [SEG.cutOnePelletInImage(crop, circle) for circle in circles]
    preproc = SEG.inhib_diam_preprocessing(petri, circles)
    disks = SEG.measureDiameters(preproc) 
    labels = [SEG.getOnePelletText(pellet) for pellet in pellets]
    ch= []
    i=0;
    for label in labels:
        ch.append(str(i))
        i=i+1
    return ch
def pipeline(path,filename,color='bgr'):
    img = cv2.imread(path)
    petri = astimp.getPetriDish(img)
    crop = petri.img
    circles = astimp.find_atb_pellets(crop)
    pellets = [astimp.cutOnePelletInImage(crop, circle) for circle in circles]
    preproc = astimp.inhib_diam_preprocessing(petri, circles)
    disks = astimp.measureDiameters(preproc) 
    labels = [astimp.getOnePelletText(pellet) for pellet in pellets]
    ch= []
    for disk in disks:
        ch.append(str(int(disk.diameter)))
    return ch
def dessMod1(path,filename,color='bgr'):
    img = cv2.imread(path)
    ast = astimp.AST(img)
    petri = astimp.getPetriDish(img) 
    crop = petri.img
    circles = astimp.find_atb_pellets(crop)
    preproc = astimp.inhib_diam_preprocessing(petri, circles)
    disks = astimp.measureDiameters(preproc)
    pellets = [astimp.cutOnePelletInImage(crop, circle) for circle in circles]
    labels = [astimp.getOnePelletText(pellet) for pellet in pellets]
    draw(ast, atb_labels='atb')
    plt.savefig("/home/PFA/suit/static/predictMod1/"+filename)

def dessMod2(path,filename,color='bgr'):
    img = cv2.imread(path)
    ast = SEG.AST(img)
    petri = SEG.getPetriDish(img) 
    crop = petri.img
    circles = SEG.find_atb_pellets(crop)
    preproc = SEG.inhib_diam_preprocessing(petri, circles)
    disks = SEG.measureDiameters(preproc)
    pellets = [SEG.cutOnePelletInImage(crop, circle) for circle in circles]
    labels = [SEG.getOnePelletText(pellet) for pellet in pellets]
    dess(ast, atb_labels='number')
    plt.savefig("/home/PFA/suit/static/predictMod2/"+filename)
    

def filesMod1(path,filename,color='bgr'):
    img = cv2.imread(path)
    ast = astimp.AST(img)
    petri = astimp.getPetriDish(img) 
    crop = petri.img
    circles = astimp.find_atb_pellets(crop)
    preproc = astimp.inhib_diam_preprocessing(petri, circles)
    disks = astimp.measureDiameters(preproc)
    pellets = [astimp.cutOnePelletInImage(crop, circle) for circle in circles]
    labels = [astimp.getOnePelletText(pellet) for pellet in pellets]
    ch=filename[0:len(filename)-3]+'csv'
    with open("/home/PFA/suit/static/filesMod1/"+ch, 'w', newline='') as csvfile:
    	fieldnames = ['index_anti','Name', 'diametre']
    	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    	writer.writeheader()
    	i=0;
    	for label, disk in zip(labels,disks):
        	writer.writerow({'index_anti':i,'Name':label.text,'diametre':disk.diameter})
        	i=i+1;
    return ch

def filesMod2(path,filename,color='bgr'):
    img = cv2.imread(path)
    ast = SEG.AST(img)
    petri = SEG.getPetriDish(img) 
    crop = petri.img
    circles = SEG.find_atb_pellets(crop)
    preproc = SEG.inhib_diam_preprocessing(petri, circles)
    disks = SEG.measureDiameters(preproc)
    pellets = [SEG.cutOnePelletInImage(crop, circle) for circle in circles]
    labels = [SEG.getOnePelletText(pellet) for pellet in pellets]
    ch=filename[0:len(filename)-3]+'csv'
    with open("/home/PFA/suit/static/filesMod2/"+ch, 'w', newline='') as csvfile:
    	fieldnames = ['index_anti','Name', 'diametre']
    	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    	writer.writeheader()
    	i=0;
    	for label, disk in zip(labels,disks):
        	writer.writerow({'index_anti':i,'Name':label.text,'diametre':disk.diameter})
        	i=i+1;
    return ch
def statist1Mod1(files):  
    plt.close() 
    data = pd.read_csv('/home/PFA/suit/static/filesMod1/'+files)
    df = pd.DataFrame(data)
    X = list(df.iloc[:, 0])
    Y = list(df.iloc[:, 2])
    #diagramme de bar 
    plt.title("Diagramme à bar resumer de zone d'inhibition")
    plt.xlabel("index de l'antibio")
    plt.ylabel("diametres des zones ")
    plt.bar(X, Y, color='g')
    ch1=files[0:len(files)-3]+'png'	
    plt.savefig("/home/PFA/suit/static/FigureStat1/"+ch1)
    return ch1
def statist2Mod1(files):  
    plt.close() 
    data = pd.read_csv('/home/PFA/suit/static/filesMod1/'+files)
    df = pd.DataFrame(data)
    X = list(df.iloc[:, 0])
    Y = list(df.iloc[:, 2])
    #diagramme de statistique  
    mean = statistics.mean(Y)
    sd = statistics.stdev(Y)
    plt.title("Statistique de zone d'inhibition")
    plt.xlabel("index de l'antibio")
    plt.ylabel("densité de probabilité des diametres")
    plt.plot(X, norm.pdf(Y, mean, sd))
    ch1='1'+files[0:len(files)-3]+'png'	
    plt.savefig("/home/PFA/suit/static/FigureStat1/"+ch1)
    return ch1
def statist3Mod1(files):  
    plt.close() 
    data = pd.read_csv('/home/PFA/suit/static/filesMod1/'+files)
    df = pd.DataFrame(data)
    X = list(df.iloc[:, 0])
    Y = list(df.iloc[:, 2])
    #diagramme de flux
    plt.title("Diagramme flux des points de zone d'inhibition")
    plt.xlabel("index de l'antibio")
    plt.ylabel("diametres d'inhibition ")
    plt.scatter(X, Y) 
    ch1='2'+files[0:len(files)-3]+'png'	
    plt.savefig("/home/PFA/suit/static/FigureStat1/"+ch1)
    return ch1
def statist4Mod1(files):  
    plt.close() 
    data = pd.read_csv('/home/PFA/suit/static/filesMod1/'+files)
    df = pd.DataFrame(data)
    X = list(df.iloc[:, 0])
    Y = list(df.iloc[:, 2])
    #diagramme lineaire 
    plt.title("Diagramme lineaire ajuster les zones d'inhibition")
    plt.xlabel("index de l'antibio")
    plt.ylabel("diametres d'inhibition ")  
    plt.plot(X,Y)
    ch1='3'+files[0:len(files)-3]+'png'	
    plt.savefig("/home/PFA/suit/static/FigureStat1/"+ch1)
    return ch1

def statist5Mod1(files):  
    plt.close() 
    data = pd.read_csv('/home/PFA/suit/static/filesMod1/'+files)
    df = pd.DataFrame(data)
    X = list(df.iloc[:, 0])
    Y = list(df.iloc[:, 2])
    #diagramme cercle 
    #cercle diagramme
    plt.title("Diagramme cercle illustrant les zones d'inhibition") 
    explode = []  
    name =list(df.iloc[:, 1])

    for i in range(len(X)):
    	explode.append(0.1)

    plt.pie(Y, explode=explode, labels=name, autopct='%1.1f%%', startangle=90, shadow=True)
    plt.axis('equal')
    ch1='4'+files[0:len(files)-3]+'png'	
    plt.savefig("/home/PFA/suit/static/FigureStat1/"+ch1)
    return ch1
def statist6Mod1(files):  
    plt.close() 
    data = pd.read_csv('/home/PFA/suit/static/filesMod1/'+files)
    df = pd.DataFrame(data)
    X = list(df.iloc[:, 0])
    Y = list(df.iloc[:, 0])
    Z = list(df.iloc[:, 2])
    #diagramme cercle 
    #cercle diagramme
    fig = plt.figure(1, figsize=(8,8))
    ax= Axes3D(fig ,elev=-150 ,azim=110)
    ax.scatter(X,Y,Z,c=Y,cmap=plt.cm.Paired)
    ax.set_title("Diagramme 3D modeliser les zones d'inhibition")    
    ax.set_xlabel("number")
    ax.w_xaxis.set_ticklabels([])
    ax.set_ylabel("index_in Disk")
    ax.w_yaxis.set_ticklabels([])
    ax.set_zlabel("diamtre")
    ax.w_zaxis.set_ticklabels([])
    ch1='5'+files[0:len(files)-3]+'png'	
    plt.savefig("/home/PFA/suit/static/FigureStat1/"+ch1)
    return ch1
def statist1Mod2(files):  
    plt.close() 
    data = pd.read_csv('/home/PFA/suit/static/filesMod2/'+files)
    df = pd.DataFrame(data)
    X = list(df.iloc[:, 0])
    Y = list(df.iloc[:, 2])
    #diagramme de bar 
    plt.title("Diagramme à bar resumer de zone d'inhibition")
    plt.xlabel("index de l'antibio")
    plt.ylabel("diametres des zones ")
    plt.bar(X, Y, color='g')
    ch1=files[0:len(files)-3]+'png'	
    plt.savefig("/home/PFA/suit/static/FigureStat2/"+ch1)
    return ch1
def statist2Mod2(files):  
    plt.close() 
    data = pd.read_csv('/home/PFA/suit/static/filesMod2/'+files)
    df = pd.DataFrame(data)
    X = list(df.iloc[:, 0])
    Y = list(df.iloc[:, 2])
    #diagramme de statistique  
    mean = statistics.mean(Y)
    sd = statistics.stdev(Y)
    plt.title("Statistique de zone d'inhibition")
    plt.xlabel("index de l'antibio")
    plt.ylabel("densité de probabilité des diametres")
    plt.plot(X, norm.pdf(Y, mean, sd))
    ch1='1'+files[0:len(files)-3]+'png'	
    plt.savefig("/home/PFA/suit/static/FigureStat2/"+ch1)
    return ch1
def statist3Mod2(files):  
    plt.close() 
    data = pd.read_csv('/home/PFA/suit/static/filesMod2/'+files)
    df = pd.DataFrame(data)
    X = list(df.iloc[:, 0])
    Y = list(df.iloc[:, 2])
    #diagramme de flux
    plt.title("Diagramme flux des points de zone d'inhibition")
    plt.xlabel("index de l'antibio")
    plt.ylabel("diametres d'inhibition ")
    plt.scatter(X, Y) 
    ch1='2'+files[0:len(files)-3]+'png'	
    plt.savefig("/home/PFA/suit/static/FigureStat2/"+ch1)
    return ch1
def statist4Mod2(files):  
    plt.close() 
    data = pd.read_csv('/home/PFA/suit/static/filesMod2/'+files)
    df = pd.DataFrame(data)
    X = list(df.iloc[:, 0])
    Y = list(df.iloc[:, 2])
    #diagramme lineaire 
    plt.title("Diagramme lineaire ajuster les zones d'inhibition")
    plt.xlabel("index de l'antibio")
    plt.ylabel("diametres d'inhibition ")  
    plt.plot(X,Y)
    ch1='3'+files[0:len(files)-3]+'png'	
    plt.savefig("/home/PFA/suit/static/FigureStat2/"+ch1)
    return ch1

def statist5Mod2(files):  
    plt.close() 
    data = pd.read_csv('/home/PFA/suit/static/filesMod2/'+files)
    df = pd.DataFrame(data)
    X = list(df.iloc[:, 0])
    Y = list(df.iloc[:, 2])
    #diagramme cercle 
    #cercle diagramme
    plt.title("Diagramme cercle illustrant les zones d'inhibition") 
    explode = []  
    name =list(df.iloc[:, 1])

    for i in range(len(X)):
    	explode.append(0.1)

    plt.pie(Y, explode=explode, labels=X, autopct='%1.1f%%', startangle=90, shadow=True)
    plt.axis('equal')
    ch1='4'+files[0:len(files)-3]+'png'	
    plt.savefig("/home/PFA/suit/static/FigureStat2/"+ch1)
    return ch1
def statist6Mod2(files):  
    plt.close() 
    data = pd.read_csv('/home/PFA/suit/static/filesMod2/'+files)
    df = pd.DataFrame(data)
    X = list(df.iloc[:, 0])
    Y = list(df.iloc[:, 0])
    Z = list(df.iloc[:, 2])
    #diagramme cercle 
    #cercle diagramme
    fig = plt.figure(1, figsize=(8,8))
    ax= Axes3D(fig ,elev=-150 ,azim=110)
    ax.scatter(X,Y,Z,c=Y,cmap=plt.cm.Paired)
    ax.set_title("Diagramme 3D modeliser les zones d'inhibition")    
    ax.set_xlabel("number")
    ax.w_xaxis.set_ticklabels([])
    ax.set_ylabel("index_in Disk")
    ax.w_yaxis.set_ticklabels([])
    ax.set_zlabel("diamtre")
    ax.w_zaxis.set_ticklabels([])
    ch1='5'+files[0:len(files)-3]+'png'	
    plt.savefig("/home/PFA/suit/static/FigureStat2/"+ch1)
    return ch1
