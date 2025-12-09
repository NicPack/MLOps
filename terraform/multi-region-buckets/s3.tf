terraform {
  required_version = "~> 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }

    random = {
      source  = "hashicorp/random"
      version = "~> 3.0"
    }
  }
}

provider "aws" {
  region = var.regions[0]
}
provider "aws" {
  alias  = "us_west_2"
  region = var.regions[1]
}

resource "random_id" "bucket_suffix" {
  count       = length(var.regions)
  byte_length = 8

}

resource "aws_s3_bucket" "us_east_1_bucket" {
  bucket = "${var.bucket_name_prefix}-${var.regions[0]}-${random_id.bucket_suffix[0].hex}"
  tags = {
    "name" = "my-bucket-${var.regions[0]}"
  }
}

resource "aws_s3_bucket_versioning" "us_east_1_bucket" {
  bucket = aws_s3_bucket.us_east_1_bucket.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_lifecycle_configuration" "us_east_1_bucket" {
  bucket = aws_s3_bucket.us_east_1_bucket.id

  rule {
    id     = "transition-to-glacier"
    status = "Enabled"
    transition {
      days          = 30
      storage_class = "GLACIER"
    }
  }
}


resource "aws_s3_bucket" "us_west_2_bucket" {
  provider = aws.us_west_2
  bucket   = "${var.bucket_name_prefix}-${var.regions[1]}-${random_id.bucket_suffix[1].hex}"
  tags = {
    "name" = "my-bucket-${var.regions[1]}"
  }
}

resource "aws_s3_bucket_versioning" "us_west_2_bucket" {
  provider = aws.us_west_2
  bucket   = aws_s3_bucket.us_west_2_bucket.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_lifecycle_configuration" "us_west_2_bucket" {
  provider = aws.us_west_2
  bucket   = aws_s3_bucket.us_west_2_bucket.id

  rule {
    id     = "transition-to-glacier"
    status = "Enabled"
    transition {
      days          = 30
      storage_class = "GLACIER"
    }
  }
}