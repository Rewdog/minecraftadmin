# minecraftadmin
Simple dashboard for managing my son's minecraft servers and allowing me to experiment with some different technologies.

## infrastructure: terraforms to create infrastructure
Consists of spinning up an ec2 instance with a snapshot AMI, associating the correct security groups and an elastic IP.

    TODO:
    - Move away from snapshots and use persistent storage
    - Convert to spot instances

## minecraftadmin: Flask application for basic adminstration
Simple minecraft

### Features
- Supports configuration of 3 worlds on one server
- Displays Server Status, and names of players within the world.
- Allow stop / start / status refresh of each world, or shutdown of entire instance

### Installation
1) Create lambda functions that allow you to start / stop instances and retrieve the status of the instance (TODO: commit code)
2) Enable your worlds to start / stop as a service (TODO: commit code)
3) Edit config.py, specifying the region that maps to the name of your service
4) `pip install -r requirements.txt`
5) set environment variables for USER and PASSWORD used in basic auth
6) Start the app
   1) For gunicorn, `gunicorn --bind 0.0.0.0:5000 wsgi:app`
   2) For flask
   ```
   export FLASK_APP=app.py
   flask run --host=0.0.0.0
   ```
7) Enable as a service (TODO: commit code)
