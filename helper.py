import joblib
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from skimage.transform import resize
import gzip
from tensorflow.keras.models import load_model
import cv2
import tensorflow as tf

# model = pickle.load(open('DB_model.p','rb'))
DB_compressed_model_filename = 'saved_models/DB_model.p.gz'

# Load the compressed model using gzip.
with gzip.open(DB_compressed_model_filename, 'rb') as compressed_model_file:
    db_model = joblib.load(compressed_model_file)

glaucoma_model = load_model('saved_models/Glaucoma.h5')

# Testing a brand new Image
def Diabetic_Retinopathy(img):
    flat_data = []
    img = imread(img)
    img_resized = resize(img, (150,150,3))
    flat_data.append(img_resized.flatten())
    flat_data = np.array(flat_data)
    # print(img.shape)
    plt.imshow(img_resized)
    y_out = db_model.predict(flat_data)

    if y_out == 0:
        predicted_output = 'Mild Diabetic Retinopathy'
    elif y_out == 1:
        predicted_output = 'Moderate Diabetic Retinopathy'
    elif y_out == 2:
        predicted_output = 'No Diabetic Retinopathy'
    elif y_out == 3:
        predicted_output = 'Proliferate Diabetic Retinopathy'
    else:
        predicted_output = 'Severe Diabetic Retinopathy'

    return predicted_output

def Glaucoma_Detection(uploaded_file):
    # print("Uploaded file:", uploaded_file)
    img1 = imread(uploaded_file)
    resize = tf.image.resize(img1, (256,256))
    # plt.imshow(resize.numpy().astype(int))
    # plt.show()
    glaucoma_result = glaucoma_model.predict(np.expand_dims(resize/255,0))

    if glaucoma_result >  0.2:
        glaucoma_output = "Glaucoma detected"
    else:
        glaucoma_output = "Glaucoma not detected"

    return glaucoma_output