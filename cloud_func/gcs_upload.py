# set GOOGLE_APPLICATION_CREDENTIALS from .json file

from google.cloud import storage
from config import model_file, bucket_name

storage_client = storage.Client()

storage_client.create_bucket(bucket_name)
bucket = storage_client.get_bucket(bucket_name)

blob = bucket.blob(model_file)
blob.upload_from_filename(model_file)