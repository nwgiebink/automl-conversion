import os
from xml_to_automl import xml_to_automl
from train_test_split import label_split
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--train_size', default=0.8, type=int, help = 'proportional size of training set')
parser.add_argument('--google_uri', default='GoogleCloudURI/', type=str, help = 'Google Cloud URI for image paths')

opt = parser.parse_args()

def convert(train_size=opt.train_size, GoogleCloud_URI=opt.google_uri):
    image_path = os.path.join(os.getcwd(), ('images/'))
    xml_df = xml_to_automl(image_path, GoogleCloud_URI)
    labeled_df = label_split(xml_df, train_size)
    labeled_df.to_csv(('output/automl_labels.csv'), index=None)
    print('Successfully converted xml to automl csv format') 

convert()