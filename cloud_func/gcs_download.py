# set GOOGLE_APPLICATION_CREDENTIALS from .json file

import pickle
from google.cloud import storage
from config import model_file, bucket_name

storage_client = storage.Client()
bucket = storage_client.get_bucket(bucket_name)

blob = bucket.blob(model_file)
blob.download_to_filename("tmp.pkl")
model = pickle.load(open("tmp.pkl", 'rb'))