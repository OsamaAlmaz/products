data "terraform_remote_state" "base" {
  backend = "s3"

  config = {
    bucket = "dataapp.terraform"
    key    = "base.tfstate"
    region = "us-east-1"
  }
}

data "terraform_remote_state" "vpc" {
  backend = "s3"

  config = {
    bucket = "dataapp.terraform"
    key    = "vpc.tfstate"
    region = "us-east-1"
  }
}
