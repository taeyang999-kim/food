# predict.py
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
from PIL import Image

# 사전학습 모델 로드
model = MobileNetV2(weights="imagenet")

def predict_food(img):
    """
    img: PIL Image (Gradio에서 넘어옴)
    """

    img = img.resize((224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    preds = model.predict(img_array)
    decoded = decode_predictions(preds, top=1)[0][0]

    label = decoded[1]   # 예: cheeseburger
    confidence = float(decoded[2])  # 확률

    return label, confidence