# 🐾 Animal Image Classifier

A Streamlit web application for classifying animals in images using pre-trained deep learning models (EfficientNetB0 & MobileNetV2). Built using TensorFlow and Streamlit, this app can identify 15 types of animals from user-uploaded images.

## 📌 Project Objective

The goal of this project is to classify images of animals into 15 different categories using transfer learning techniques with EfficientNetB0 and MobileNetV2 models.

## 🧠 Supported Classes

- Bear
- Bird
- Cat
- Cow
- Deer
- Dog
- Dolphin
- Elephant
- Giraffe
- Horse
- Kangaroo
- Lion
- Panda
- Tiger
- Zebra

## 🗂️ Project Structure

📁 animal-image-classifier/
├── app.py # Streamlit web app
├── efficientnetb0_best.h5 # Trained model (EfficientNetB0)
├── mobilenetv2_best.h5 # Trained model (MobileNetV2)
├── requirements.txt # Python dependencies
├── ml animal classification.ipynb # Model training and evaluation notebook
└── README.md # Project documentation

bash
Copy
Edit

## 🚀 Getting Started

### 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/Hurmath123/animal-image-classifier.git
cd animal-image-classifier
Create a virtual environment and activate it:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the dependencies:

bash
Copy
Edit
pip install -r requirements.txt
▶️ Run the Streamlit App
bash
Copy
Edit
streamlit run app.py
📷 Usage
Upload an image (.jpg, .jpeg, or .png)

The model will display the predicted animal class and confidence score

🧾 Model Training
See the ml animal classification.ipynb notebook for the training and evaluation process using transfer learning.

🧳 Deployment
This app is also deployable on Hugging Face Spaces using Streamlit.

🌐 Deployment on Hugging Face
Step 1: Create a Hugging Face Account
Go to https://huggingface.co and sign up.

Step 2: Create a New Space
Click on "New Space"

Choose Gradio or Streamlit

Select Python

Name your Space (e.g., animal-classifier)

Upload the following files to the Space:

app.py

efficientnetb0_best.h5

requirements.txt

Step 3: Push to Hugging Face
You can use Git or the web interface to push files:

bash
Copy
Edit
git lfs install
git clone https://huggingface.co/spaces/YOUR_USERNAME/animal-classifier
cd animal-classifier
# Copy your files here
git add .
git commit -m "Initial commit"
git push
Make sure to include:

nginx
Copy
Edit
streamlit
tensorflow
numpy
pillow
in your requirements.txt.

Once deployed, Hugging Face will automatically run app.py.

🧑‍💻 Author
Hurmath123
🔗 GitHub
