

resource "aws_s3_bucket" "my-bucket" {
  bucket = "nicolas-mlops-bucket-terraform"
  tags = {
    "name" = "my-bucket"
  }
}

resource "aws_s3_bucket" "my_bucket_us_west_2" {
  provider = aws.us-west-2
  bucket   = "nicolas-mlops-bucket-terraform-us-west-2"
  tags = {
    "name" = "my-bucket-us-west-2"
  }
}