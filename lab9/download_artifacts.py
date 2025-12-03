import boto3
import os

BUCKET_NAME = "nicolas-mlops"
PREFIX = "model/"
LOCAL_DIR = "model/"

s3 = boto3.client("s3")

os.makedirs(LOCAL_DIR, exist_ok=True)
response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix=PREFIX)

if "Contents" in response:
    for obj in response["Contents"]:
        key = obj["Key"]

        if key.endswith("/"):
            continue
        
        relative_path = key[len(PREFIX):] if key.startswith(PREFIX) else key
        local_file= os.path.join(LOCAL_DIR, relative_path)

        local_folder = os.path.dirname(local_file)
        os.makedirs(local_folder, exist_ok=True)

        print(f"Downloading {key} to {local_folder}")
        s3.download_file(BUCKET_NAME, key, local_file)
    print("Download Complete")
else:
    print("No objects found with this prefix: {PREFIX}")