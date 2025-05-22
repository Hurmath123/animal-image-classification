import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import requests
import tempfile

st.title("Animal Image Classification")
st.write("Upload an image to classify the animal using a pre-trained EfficientNetB0 model.")

# Remote URL to the model file (host this on Hugging Face or Google Drive with direct access)
MODEL_URL = "https://huggingface.co/Frough11/animal-classification/blob/main/efficientnetb0_best.h5"

@st.cache_resource
def load_remote_model():
    with tempfile.NamedTemporaryFile(suffix=".h5") as tmp:
        response = requests.get(MODEL_URL)
        tmp.write(response.content)
        tmp.flush()
        return load_model(tmp.name)

# Load model from URL
model = load_remote_model()

# Define class names
class_names = [
    'Bear', 'Bird', 'Cat', 'Cow', 'Deer', 'Dog', 'Dolphin',
    'Elephant', 'Giraffe', 'Horse', 'Kangaroo', 'Lion',
    'Panda', 'Tiger', 'Zebra'
]

# File uploader
uploaded_file = st.file_uploader("Upload an animal image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB").resize((224, 224))
    st.image(img, caption='Uploaded Image', use_column_width=True)

    x = image.img_to_array(img) / 255.0
    x = np.expand_dims(x, axis=0)

    # Make prediction
    pred = model.predict(x)
    confidence = np.max(pred) * 100
    predicted_class = class_names[np.argmax(pred)]

    st.markdown(f"### Prediction: **{predicted_class}**")
    st.markdown(f"**Confidence:** {confidence:.2f}%")
