# !pip3 uninstall keras-nightly
# !pip3 uninstall -y tensorflow
# !pip3 install keras==2.1.6
# !pip3 install tensorflow-gpu==1.15.0
# !pip3 install h5py==2.10.0
# !pip install -U coremltools

final_model_path = 'trained_weights_final.h5'
classes_path = 'classes.txt'
anchors_path = 'model_data/yolo_anchors.txt'
# final_model_dir = '/Users/kyh/GitHub/Yolov3Tiny/tinySnackModel.h5'
final_model_dir = '/Users/kyh/GitHub/Yolov3Tiny/TinySnackModel.h5'
coreml_model_dir = 'TinySnackModel8.mlmodel'
#
# import tensorflow as tf
# from yolo import YOLO
# import coremltools
# from keras.models import load_model
# from coremltools.converters import keras as converter
#
# # from yolo import YOLO
# yolo = YOLO(model_path=final_model_path,
#             classes_path=classes_path,
#             anchors_path = anchors_path)
# model = yolo.get_model()
# model.save(final_model_dir)
#
# model.summary()

## 1, 2
import coremltools
coreml_model = coremltools.converters.keras.convert(final_model_dir,
                                                    image_input_names='image',
                                                    input_names='image',
                                                    input_name_shape_dict={'image':[None, 416, 416, 3]},
                                                    image_scale=1/255.0)
coreml_model.author = 'younghwankim'
coreml_model.short_description = 'Snack Recognition Model'
coreml_model.input_description['image'] = 'Takes as input an image of a snack'
# coreml_model.output_description['output1'] = '13 * 13 * 30'
# coreml_model.output_description['output2'] = '26 * 26 * 30'
coreml_model.save(coreml_model_dir)

#
# import coremltools
# coreml_model = coremltools.converters.keras.convert(final_model_path,
#                                                     image_input_names='image',
#                                                     input_names='image',
#                                                     input_name_shape_dict={'image':[None, 416, 416, 3]},
#                                                     output_names=['output1', 'output2'],
#                                                     image_scale=1/255.0)
# coreml_model.author = 'younghwankim'
# coreml_model.short_description = 'Snack Recognition Model'
# coreml_model.input_description['image'] = 'Takes as input an image of a snack'
# coreml_model.output_description['output1'] = '13 * 13 * 30'
# coreml_model.output_description['output2'] = '26 * 26 * 30'
# coreml_model.save(coreml_model_dir)



# 3
# import coremltools
#
#
# def getClasses(classes_path):
#     with open(classes_path) as f:
#         classes = f.read().splitlines()
#     return classes
#
#
# coreml_model = coremltools.converters.keras.convert(final_model_dir,
#                                                     image_input_names='image',
#                                                     input_name_shape_dict={'image': [None, 416, 416, 3]},
#                                                     input_names="image",
#                                                     image_scale=1 / 255.0,
#                                                     class_labels=getClasses(classes_path),
#                                                     is_bgr=True)
# coreml_model.save(coreml_model_dir)

# 4
# import coremltools
#
# coreml_model = coremltools.converters.keras.convert(final_model_dir, input_names='input1', image_input_names='input1', input_name_shape_dict={'input1': [None, 416, 416, 3]}, output_names=['output1', 'output2'], image_scale=1/255.)
#
# coreml_model.input_description['input1'] = 'Input image'
# coreml_model.output_description['output1'] = 'The 13x13 grid (Scale1)'
# coreml_model.output_description['output2'] = 'The 26x26 grid (Scale2)'
#
# coreml_model.author = 'YounghwanKim'
# coreml_model.license = 'Public Domain'
# coreml_model.short_description = "Takes as input an image of a snack"
#
# coreml_model.save(coreml_model_dir)
