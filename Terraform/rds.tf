resource "aws_db_instance" "django-app-rds" {
  identifier                 = "django-app-rds"
  allocated_storage          = 25
  storage_type               = "gp2"
  engine                     = "postgres"
  engine_version             = "10"
  auto_minor_version_upgrade = true
  instance_class             = "db.t3.micro"
  username                   = var.master_rds_user
  password                   = var.master_rds_password
  port                       = 5432
  publicly_accessible        = true

  backup_retention_period = 7
  backup_window           = "00:00-01:00"
  maintenance_window      = "wed:01:30-wed:02:30"
  skip_final_snapshot     = true
  copy_tags_to_snapshot   = true

  monitoring_role_arn = data.terraform_remote_state.base.outputs.rds_role_arn
  monitoring_interval = 10

  tags = {
    Environment = "Production"
    Type        = "RDS"
    Terraform   = "True"
    Name        = "prod-metrcs-rds"
  }
}
