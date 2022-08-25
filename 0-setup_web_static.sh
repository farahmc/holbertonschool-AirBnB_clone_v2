#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

# install nginx
apt-get -y update
apt-get -y install nginx
service nginx start

# create directories & set user/group permissions
mkdir -p "/data/web_static/releases/test/"
mkdir -p "/data/web_static/shared/"
chown -R ubuntu:ubuntu /data/

# create symlink (delete if exists first)
ln -s -f -n /data/web_static/releases/test/ /data/web_static/current

# create a & populate dummy index
printf "Success!" > /data/web_static/releases/test/index.html

# update nginx config
sed -i '/add_header X-Served-By/a location /hbnb_static { \n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

service nginx restart
