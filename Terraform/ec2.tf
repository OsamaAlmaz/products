provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "django-app-instance" {
    ami    =  "ami-django-tweet-app"
    instance_type = "t2.micro"
}