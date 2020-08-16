# minecraftadmin
Simple dashboard for managing my son's minecraft servers and allowing me to experiment with some different technologies.

## infrastructure: terraforms to create infrastructure
Consists of spinning up an ec2 instance with a snapshot AMI, associating the correct security groups and an elastic IP.

    TODO:
    - Move away from snapshots and use persistent storage
    - Convert to spot instances

## minecraftadmin: Flask application for basic adminstration

    TODO:
    - Get things ready for an initial commit