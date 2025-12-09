# variables.tf

variable "github_access_token" {
  description = "GitHub Personal Access Token"
  type        = string
  sensitive   = true
}

variable "repository_name" {
  description = "Name of the GitHub repository to create"
  type        = string
  default     = "mlops_terraform_repo"
}

variable "repository_description" {
  description = "Description of the GitHub repository"
  type        = string
  default     = "Repository managed by Terraform"
}

variable "repository_visibility" {
  description = "Visibility of the GitHub repository (public or private)"
  type        = bool
  default     = false
}