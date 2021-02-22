resource "aws_lb" "the_alb" {
}

resource "aws_lb_target_group" "django-app" {
  name        = "django-app"
  port        = 3000
  protocol    = "HTTP"
  target_type = "ip"
  vpc_id      = data.terraform_remote_state.vpc.outputs.thevpc_id
  health_check {
    interval = 300
    path     = "/login"
  }
}