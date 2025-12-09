variable "regions" {
  description = "List of AWS regions to create resources in"
  type        = list(string)
  default     = ["us-east-1", "us-west-2"]
}

variable "bucket_name_prefix" {
  description = "Prefix for the S3 bucket names"
  type        = string
  default     = "multi-region-bucket"
}