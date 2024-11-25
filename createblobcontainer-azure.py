# This would need pip install azure-storage-blob azure-identity


from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

# Azure Storage account name
account_name = "<your_account_name>"

# Define container (bucket) and file details
container_name = "example-container"
local_file_path = "example.txt"
blob_name = "uploaded-example.txt"

# Authenticate using DefaultAzureCredential
credential = DefaultAzureCredential()

# Connect to the Blob Service Client
blob_service_client = BlobServiceClient(
    f"https://{account_name}.blob.core.windows.net", credential=credential
)

# Step 1: Create a container (similar to creating an S3 bucket)
print(f"Creating container: {container_name}")
container_client = blob_service_client.create_container(container_name)

# Step 2: Upload a file to the container
print(f"Uploading file to container '{container_name}' as blob '{blob_name}'")
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

# Read the file and upload it
with open(local_file_path, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)

print(f"File '{local_file_path}' uploaded to blob '{blob_name}' in container '{container_name}'.")
