# Convert xml files to Google AutoML format
In working directory (see wd structure requirements below) run converter.py

#### Parameters
*train_size*: size of training split from 0.0-1.0 (default 0.8; AutoML requires minimum of 2 splits). converter.py imports train_test_split.py to generate TRAIN and VALIDATE set labels required for Google AutoML format.

*GoogleCloud_URI*: URI for Google AutoML to access training files in Google Cloud (default 'GoogleCloudURI/' placeholder). 

## Required Directory structure:
Working directory must contain a folder 'images/', containing all *.JPEG images and *.xml labels, in which corresponding images and labels have the same name. 

This repo is an example of the correct directory structure. 
