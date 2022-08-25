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
ln -s -f /data/web_static/releases/test/ /data/web_static/current

# create a & populate dummy index
printf "<html>
		<head>
		</head>
		<body>
			Hello World
		</body>
	</html>" > /data/web_static/releases/test/index.html

# update nginx config
sed -i '/server_name _;/a location /hbnb_static {alias /data/web_static/current/};' /etc/nginx/sites-available/default

service nginx restart
