resource "aws_s3_bucket" "my-bucket" {
  bucket = "nicolas-mlops-bucket-terraform-us-east-1"
  tags = {
    "name" = "my-bucket-us-east-1"
  }
}

resource "aws_s3_bucket" "my_bucket_us_west_2" {
  provider = aws.us-west-2
  bucket   = "nicolas-mlops-bucket-terraform-us-west-2"
  tags = {
    "name" = "my-bucket-us-west-2"
  }
}