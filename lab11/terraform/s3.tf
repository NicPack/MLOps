module "lab11_s3_bucket" {
  source  = "terraform-aws-modules/s3-bucket/aws"
  version = "5.9.1"
  bucket  = "mlops-lab11-nicolas"
  force_destroy = true
}