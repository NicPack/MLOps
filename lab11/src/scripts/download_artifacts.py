import os

import boto3
from settings import settings

s3 = boto3.resource("s3")


def download_s3_directory(
    bucket_name: str = settings.s3_bucket_name,
    s3_folder: str = settings.s3_artifacts_path,
    local_dir: str = settings.local_artifacts_path,
):
    """
    Download the contents of a folder directory
    Args:
        bucket_name: the name of the s3 bucket
        s3_folder: the folder path in the s3 bucket
        local_dir: a relative or absolute directory path in the local file system
    """
    print(f"bucket name: {bucket_name}")
    bucket = s3.Bucket(bucket_name)
    for obj in bucket.objects.filter(Prefix=s3_folder):
        print(f"obj: {obj.key}")
        target = (
            obj.key
            if local_dir is None
            else os.path.join(local_dir, os.path.relpath(obj.key, s3_folder))
        )
        if not os.path.exists(os.path.dirname(target)):
            os.makedirs(os.path.dirname(target))
        if obj.key[-1] == "/":
            continue
        bucket.download_file(obj.key, target)


if __name__ == "__main__":
    download_s3_directory()
