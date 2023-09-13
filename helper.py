import joblib
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from skimage.transform import resize
import gzip

# model = pickle.load(open('DB_model.p','rb'))
compressed_model_filename = 'compressed_model.p.gz'

# Load the compressed model using gzip.
with gzip.open(compressed_model_filename, 'rb') as compressed_model_file:
    model = joblib.load(compressed_model_file)

# Testing a brand new Image
def Diabetic_Retinopathy(img):
    flat_data = []
    img = imread(img)
    img_resized = resize(img, (150,150,3))
    flat_data.append(img_resized.flatten())
    flat_data = np.array(flat_data)
    # print(img.shape)
    plt.imshow(img_resized)
    y_out = model.predict(flat_data)

    if y_out == 0:
        predicted_output = 'Mild'
    elif y_out == 1:
        predicted_output = 'Moderate'
    elif y_out == 2:
        predicted_output = 'No DR'
    elif y_out == 3:
        predicted_output = 'Proliferate DR'
    else:
        predicted_output = 'Severe'

    return predicted_output