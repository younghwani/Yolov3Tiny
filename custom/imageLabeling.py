import os
from PIL import Image
import xml.etree.ElementTree as ET
from os import getcwd

data_dir = '/data/YoloTrainSet'
new_path = '/data/NewYoloTrainSet'

category = [c for c in os.listdir(data_dir) if c != '.DS_Store']
print('Category : \n', category)

directory_list = [os.path.join(data_dir, c) for c in category]
print('Directory List : \n', directory_list)

new_path = '/data/NewYoloTrainSet'
new_path_list = [os.path.join(new_path, c) for c in category]
print('New Path List : \n', new_path_list)

# xml file list
label_list = []
for i in range(len(category)):
    temp2 = os.listdir(directory_list[i])
    temp2 = [file for file in temp2 if file.split('.')[1] == 'xml']
    label_list.append(temp2)
print('label List : \n', label_list)

# Make class text file
classes = []
for i in range(len(directory_list)):
    temp_xml = os.path.join(directory_list[i], label_list[i][0])

    tree = ET.parse(temp_xml)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text

    classes.append(cls)
classes = list(set(classes))
print('Classes : \n', classes)

class_file = open('/classes.txt', 'w')
for clas in classes:
    class_file.write(clas)
    class_file.write('\n')
class_file.close()

# Make Train data(yolo) text file
annotations_voc = []
for i in range(len(directory_list)):
    for j in range(len(label_list[i])):
        annotations_voc.append(os.path.join(directory_list[i], label_list[i][j]))
print('annotations_voc : \n', annotations_voc)

def convert_annotation(annotation_voc, converted_file):
    tree = ET.parse(annotation_voc)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b_box = (round(int(xmlbox.find('xmin').text) / 3),
                 round(int(xmlbox.find('ymin').text) / 3),
                 round(int(xmlbox.find('xmax').text) / 3),
                 round(int(xmlbox.find('ymax').text) / 3))
        converted_file.write(" " + ",".join([str(a) for a in b_box]) + ',' + str(cls_id))

converted_file = open('/train_all.txt', 'w')
for annotation_voc in annotations_voc:
    image_id = annotation_voc.split('/')[-1].split('.')[0] + '.jpg'
    path = new_path + '/' + '_'.join(image_id.split('_')[:-1]) + '/' + image_id
    converted_file.write(path)
    convert_annotation(annotation_voc, converted_file)
    converted_file.write('\n')
converted_file.close()