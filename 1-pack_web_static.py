#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from contents of
web_static folder """
from fabric.api import local
from datetime import datetime


""" Generate a .tgz archive from web_static """
timestamp = datetime.now()
timestamp_str = timestamp.strftime("%Y%m%d%H%M%S")
created_archive = "web_static_" + timestamp_str + ".tgz"
print(created_archive)
