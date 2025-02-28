#!/usr/bin/env python3

import boto3
import requests
import os
from urllib.parse import urlparse

bucket = "bucket-name"
expiration = 604800

# downloading the file
url = "https://example.com/file.gif"
file = "downloaded_file.gif"

response = requests.get(url)
with open(file, 'wb') as f:
    f.write(response.content)

print(f"Downloaded file: {file}")

# uploading to S3
s3 = boto3.client('s3')
s3.upload_file(file, bucket, file)
print(f"Uploaded to the following S3 bucket: {bucket}")

# generating presign
presign = s3.generate_presigned_url('get_object', Params = {'Bucket': bucket, 'Key': file}, ExpiresIn = expiration)
print(f"\nPresign expires in {expiration} seconds: {presign}")
