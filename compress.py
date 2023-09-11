import pickle
import gzip

# Replace 'your_model.pkl' with the filename of your Pickle model.
model_filename = 'DB_model.p'

# Load your machine learning model from the Pickle file.
with open(model_filename, 'rb') as model_file:
    model = pickle.load(model_file)

# Define the filename for the compressed model.
compressed_model_filename = 'compressed_model.p.gz'

# Compress and save the model using gzip.
with gzip.open(compressed_model_filename, 'wb') as compressed_model_file:
    pickle.dump(model, compressed_model_file)

print(f"Compressed model saved as {compressed_model_filename}")


