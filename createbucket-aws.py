# This would need pip install boto3

import boto3
import os
import sys

# create an s3 resource
s3 = boto3.resource('s3')

# create an s3 bucket
bucket_name = 'XXXXXXXXX'
s3.create_bucket(Bucket=bucket_name)

# upload a file to the bucket
file_name = 'my-file.txt'
s3.Object(bucket_name, file_name).put(Body=open(file_name, 'rb'))