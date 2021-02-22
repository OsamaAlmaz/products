resource "aws_ecr_repository" "django-app" {
  name = "django-app"
  tags = {
    Terrafrom = "True"
    Name      = "django-app"
  }
}
