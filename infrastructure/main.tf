provider "aws" {
    region = "us-east-1"
}

resource "aws_eip_association" "eip_assoc" {
  instance_id   = aws_instance.example-tf-minecraft.id
  allocation_id = "eipalloc-0bd21d49db21757ed"
}

resource "aws_instance" "example-tf-minecraft" {
    ami             = "ami-03c24b8c921499588"
    instance_type   = "t2.medium"
    security_groups = [
        "minecraft-2"
    ]    
}