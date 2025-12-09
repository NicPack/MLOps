output "bucket_arns" {
  value = {
    "${var.regions[0]}" = aws_s3_bucket.us_east_1_bucket.arn
    "${var.regions[1]}" = aws_s3_bucket.us_west_2_bucket.arn
  }
}

output "bucket_regions" {
  value = {
    "${aws_s3_bucket.us_east_1_bucket.id}" = var.regions[0]
    "${aws_s3_bucket.us_west_2_bucket.id}" = var.regions[1]
  }
}