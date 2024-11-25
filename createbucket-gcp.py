# this would need pip install google-cloud-storage

from google.cloud import storage

# GCP project and bucket details
project_id = "<your_project_id>"
bucket_name = "example-bucket"
local_file_path = "example.txt"
blob_name = "uploaded-example.txt"

# Step 1: Initialize the Storage Client
storage_client = storage.Client(project=project_id)

# Step 2: Create a new bucket
print(f"Creating bucket: {bucket_name}")
bucket = storage_client.create_bucket(bucket_name)
print(f"Bucket {bucket_name} created.")

# Step 3: Upload a file to the bucket
print(f"Uploading file '{local_file_path}' to bucket '{bucket_name}' as blob '{blob_name}'")
blob = bucket.blob(blob_name)

# Read the file and upload it
with open(local_file_path, "rb") as file_data:
    blob.upload_from_file(file_data)

print(f"File '{local_file_path}' uploaded to bucket '{bucket_name}' as blob '{blob_name}'.")
