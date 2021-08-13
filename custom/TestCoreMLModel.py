import numpy as np
from PIL import Image
import coremltools
import matplotlib.pyplot as plt

def testMLModel(file, model_path):
    snackModel = coremltools.models.MLModel(model_path)

    # 이미지 로딩
    image = Image.open(file)

    image = image.resize((416, 416))

    # 실행
    result_image = snackModel.predict({'input1': image})

    # 실행 결과 표시
    print(result_image)
    # result_image.show()

testMLModel('/Users/kyh/GitHub/Yolov3Tiny/data/YoloTrainSet/kancho/kancho_1.jpg',
            'TinySnackModel7.mlmodel')

