
locals {
  repository_visibility = var.repository_visibility ? "public" : "private"
}

terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}

provider "github" {
  token = var.github_access_token
}

resource "github_repository" "example" {
  name        = var.repository_name
  description = var.repository_description
  visibility  = local.repository_visibility
  auto_init   = true
}