import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_automl(path, GoogleCloud_URI):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            set = 'UNASSIGNED'
            filename = root.find('filename').text
            full_URI = GoogleCloud_URI+filename
            width = int(root.find('size')[0].text)
            height = int(root.find('size')[1].text)
            label = member[0].text
            xmin = int(member[4][0].text)/width
            ymin = int(member[4][1].text)/height
            xmax = int(member[4][2].text)/width
            ymax = int(member[4][3].text)/height
            xml_list.append((set,full_URI,label,
                            xmin,ymin,
                            xmax,ymin,
                            xmax,ymax,
                            xmin,ymax))
    column_names = ['set','Google Cloud URI', 'label',
                    'x_relative_min', 'y_relative_min',
                    'x_relative_max', 'y_relative_min',
                    'x_relative_max', 'y_relative_max',
                    'x_relative_min', 'y_relative_max']
    xml_df = pd.DataFrame(xml_list, columns=column_names)
    return xml_df