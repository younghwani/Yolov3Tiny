from yolo import YOLO

# from tensorflow.python.framework.ops import disable_eager_execution
# disable_eager_execution()

from PIL import Image
import matplotlib.pyplot as plt

def objectDetection(file, model_path, class_path):
    yolo = YOLO(model_path=model_path, class_path=class_path,
                anchors_path='model_data/tiny_yolo_anchors.txt')
    image = Image.open(file)
    # model = yolo.get_model()
    # model.summary()
    image.show()

    result_image = yolo.detect_image(image)

    result_image.show()
    # plt.imshow(result_image)
    # display(result_image)


objectDetection('data/dog.jpg',
                'model_data/yolo-tiny.h5',
                'model_data/coco_classes.txt')