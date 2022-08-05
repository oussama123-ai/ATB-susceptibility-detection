import glob
import cv2
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from imageio import imread, imwrite
import SEG
import SEG_tools
dess = SEG_tools.dess
dessiner = SEG_tools.dess
import csv
from csv import writer
from PIL import Image
entet=["Name","0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]
ch='global.csv'
with open("/home/PFA/"+ch, 'w', newline='') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(entet)
    f_object.close()
for file in glob.glob("/home/oussama/Bureau/Test/*.JPG"):
    img=cv2.imread(file) 
    ast = SEG.AST(img)
    petri = SEG.getPetriDish(img) 
    crop = petri.img
    circles = SEG.find_atb_pellets(crop)
    preproc = SEG.inhib_diam_preprocessing(petri, circles)
    disks = SEG.measureDiameters(preproc)
    pellets = [SEG.cutOnePelletInImage(crop, circle) for circle in circles]
    labels = [SEG.getOnePelletText(pellet) for pellet in pellets]
    data=[];
    data.append(file)
    for label, disk in zip(labels,disks):
    	data.append(disk.diameter)
    ch='global.csv'
    with open("/home/oussama/Bureau/Result/"+ch, 'a', newline='') as f_object:
    	 writer_object = writer(f_object)
    	 writer_object.writerow(data)
    	 f_object.close()
        

