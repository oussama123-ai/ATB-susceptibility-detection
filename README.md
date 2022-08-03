# Atb susceptibility detection :

Antibiotic resistance has progressively developed and now concerns all pathogenic
bacteria. It results from the repeated administration of antibiotics in humans or animals,
which creates conditions, called ”selection pressure” favoring the acquisition and dissemination of antibiotic-resistant strains.
Image processing of a diffusion plate using a deep learning model allowing the processing
and measurement of antibiotic susceptibility tests by disk diffusion. It allows the analysis
of disk diffusion plate images and to measure the diameters of the inhibition zones. A
deep learning algorithm examines the input data for several features.
It identifies these features and correlates them to obtain a meaningful final result. This
project involves the use of deep learning techniques for the analysis of various diffusion
plates with different types of antibiotics to detect and classify antibiotic resistance in
bacteria.

# overview :

This can be a decision support tool for the doctor or nurse when testing on a diffusion
plate. Firstly, an improvement to the existing model ASTlib(https://mpascucci.github.io/AST-image-processing/)was given using Tensorflow
and OpenCV, based on data augmentation techniques and it resulted in
an efficiency of about 80%. Secondly, a model entitled SEGlib (https://github.com/oussama123-ai/Classification-of-antibiotic-resistance-) was created using Keras
and Mask R-CNN in order to optimize the model in terms of execution. As a result, the
evaluation of the results showed a high efficiency compared to the first model of the order
of 90.5%.

# resume :

In this project, we performed various disc diffusion tests after having
To create our application, we used “open source” tools like Flask. We
learned how to prepare and annotate a dataset, design a model
neural network and a model based on the notion of segmentation, and modify it to
improve the accuracy of parameters of different layers and adjust all data
to adapt them to our model.
In this project, we encountered several problems, starting with the collection
images since the domain of our project is very poor in terms of test data,
to improve the initial dataset. Let us add, a lack of projects allowing
detection of inhibition zone contours using OpenCV segmentations. Of
Moreover, deep learning requires high-performance training, which requires
a lot of the time.

# graphical interface:

A graphical interface is necessary to provide an easy-to-use mode of operation.
the user. We can use HTML, CSS and Java-script and deploy our model
with Flask while keeping it simple and easy to use. This graphical interface
allows you to choose a prediction model, capture and display images with all thenecessary analyzes and results.

[Capture d’écran vidéo de 09-06-2022 22:25:43.webm](https://user-images.githubusercontent.com/83811606/182249823-1d2ed317-2dc9-4c10-aa60-4a5dc501cd04.webm)

[Capture d’écran vidéo de 09-06-2022 22:23:16.webm](https://user-images.githubusercontent.com/83811606/182249778-aaa11745-52aa-425b-98d8-1f5b67d98e42.webm)

[Capture d’écran vidéo de 09-06-2022 22:23:59.webm](https://user-images.githubusercontent.com/83811606/182249803-a9d2a48f-dd1b-4abb-bdb6-11fb025bc33f.webm)

# architecture :
![Architecture-generale](https://user-images.githubusercontent.com/83811606/182250528-01caa1ac-59df-464f-b3ae-3582e27f2bcc.png)

# installation :

pip install requirement.txt
# for the packages :
pip install astimp-0.0.3-cp310-cp310-linux_x86_64.whl           

pip install SEG-0.0.1-cp310-cp310-linux_x86_64.whl
