# VIDEO LIGHTNING

## 1.  Description

This project is an endpoint API whose purpose is to return the metric between a given image and an enhaced one.
The technologies used for this project can be found in the requirements.txt file, and docker.
### 1.1 Article the project is based on
This project uses enhancement exposure methods based on Dual Illumination Estimation for Robust Exposure Correction,
which at the same time uses Machine Learning algorithms to proccess images and enhance them.
### 1.2 Methodology
1.  The use of machine learning, as well as image processing algorithms to proccess images.
2.  Python as programming language because of its support to these algorithm.
3.  Observing results and reporting them, to test its reliability
4.  Implement it as a endpoint API to make it available for other to use in a easy way, abstracting its proccess.  


## 2.  How to install and run the project?
The intention of this project is to be executed along with docker, therefore assuming that docker is successfully 
install in your machine up and running, these are the neccesary commands to run it.

### Commands
                docker build -t video_lightning .
                docker run -p port from the outside : port from the inside video_lightning 

#### Example: 
                docker run -p 8000:8000 video_lightning 

## 3.  How to try it?
####  3.1 Paste the following in your browser
                127.0.0.0.1:8000/docs
##  4. Use the API














