import argparse
import os
from pathlib import Path

import boto3

s3 = boto3.client("s3")
BUCKET_NAME = "mlops-lab11-nicolas"

parser = argparse.ArgumentParser("send to bucket")
parser.add_argument(
    "-f",
    "--file",
    required=True,
    help="Path to a file that will be send to s3 bucket",
)
parser.add_argument(
    "-d", "--directory", required=False, help="Bucket directory to put the file in"
)


def upload_file(file_path, s3_key):
    with open(file_path,"rb") as f:
        file_content = f.read()
        s3.put_object(Bucket=BUCKET_NAME, Key=s3_key, Body=file_content)
    print(f"Uploaded file to s3://{BUCKET_NAME}/{s3_key}")


def upload_directory(local_dir, s3_prefix):
    local_path = Path(local_dir)

    for file_path in local_path.rglob("*"):
        if file_path.is_file():
            relative_path = file_path.relative_to(local_path)
            s3_key = (
                os.path.join(s3_prefix, str(relative_path))
                if s3_prefix
                else str(relative_path)
            )
            s3_key = s3_key.replace(os.sep, "/")

            upload_file(str(file_path), s3_key)


if __name__ == "__main__":
    args = parser.parse_args()

    local_path = Path(args.file)
    s3_prefix = args.directory or ""

    if local_path.is_file():
        file_name = local_path.name
        s3_key = os.path.join(s3_prefix, file_name) if s3_prefix else file_name
        s3_key = s3_key.replace(os.sep, "/")

        upload_file(file_name, s3_key)
    elif local_path.is_dir():
        upload_directory(str(local_path), s3_prefix)
    else:
        print(f"Error: {args.file} is not a valid file or directory")
