variable "bucket_name_prefix" {
  description = "Prefix for the S3 bucket names"
  type        = string
}

variable "region" {
  description = "AWS region to create the S3 bucket in"
  type        = string
  default     = "us-east-1"
}

variable "random_suffix" {
  description = "Random suffix to append to bucket names for uniqueness"
  type        = string
}

variable "lifecycle_days" {
  description = "Number of days after which to transition objects to the specified storage class"
  type        = number
  default     = 90
}

variable "lifecycle_storage_class" {
  description = "Storage class to transition objects to after the specified number of days"
  type        = string
  default     = "GLACIER"
}