#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

# install nginx
apt-get -y update
apt-get -y install nginx
service nginx start

# create directories
mkdir -p "/data/web_static/releases/test"
mkdir -p "/data/web_static/shared"

# create symlink (delete if exists first)
ln -s -f -n /data/web_static/releases/test/ /data/web_static/current

# create a & populate dummy index
printf "Success!\n" > /data/web_static/releases/test/index.html

# set permissions
chown -R ubuntu:ubuntu /data/

# update nginx config
sed -i '/listen 80 default_server;/a location /hbnb_static { \n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

service nginx restart
