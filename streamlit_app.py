import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import json

model = tf.keras.models.load_model("model/model.h5")
with open("model/class_names.json", "r") as f:
    class_names = json.load(f)

st.title("Image Classifier")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB").resize((128, 128))
    st.image(img, caption="Uploaded Image", use_container_width=True)
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions[0])]
    st.write(f"**Prediction:** {predicted_class}")
