from yolo import YOLO

# from tensorflow.python.framework.ops import disable_eager_execution
# disable_eager_execution()

from PIL import Image
# import matplotlib.pyplot as plt

def objectDetection(file, model_path, class_path):
    yolo = YOLO(model_path=model_path, class_path=class_path,
                anchors_path='model_data/tiny_yolo_anchors.txt')
    image = Image.open(file)
    # model = yolo.get_model()
    # model.summary()
    # image.show()

    result_image = yolo.detect_image(image)

    result_image.show()
    # plt.imshow(result_image)
    # display(result_image)


# objectDetection('data/YoloTrainSet/diget/diget_1.jpg',
#                 'trained_weights_final.h5',
#                 'classes.txt')

# for i in range(20):
#     objectDetection(f'data/YoloTrainSet/kancho/kancho_{i+1}.jpg',
#                     'trained_weights_final.h5',
#                     'classes.txt')

for i in range(20):
    objectDetection(f'data/YoloTrainSet/changgu/changgu_{i+1}.jpg',
                    'trained_weights_final.h5',
                    'classes.txt')