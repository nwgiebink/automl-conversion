import os
from xml_to_automl import xml_to_automl
from train_test_split import label_split

def convert(train_size=0.8, GoogleCloud_URI='GoogleCloudURI/'):
    image_path = os.path.join(os.getcwd(), ('images/'))
    xml_df = xml_to_automl(image_path)
    labeled_df = label_split(xml_df, train_size)
    labeled_df.to_csv(('output/automl_labels.csv'), index=None)
    print('Successfully converted xml to automl csv format') 

convert()