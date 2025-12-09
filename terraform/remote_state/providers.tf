terraform {
  required_version = ">=1.7.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  backend "s3" {
    region = "us-east-1"
    bucket = "nicolas-mlops"
    key    = "mlops/terraform.tfstate"
  }
}

provider "aws" {
  region = "us-east-1"
}