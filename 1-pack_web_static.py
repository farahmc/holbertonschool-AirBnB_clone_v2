#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from contents of
web_static folder """
from fabric.api import local
from datetime import datetime


def do_pack():
    """ Generate a .tgz archive from web_static """
    timenow = datetime.now()
    timenow_str = timenow.strftime("%Y%m%d%H%M%S")

    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static".
              format(timenow_str))
        return("versions/web_static_{}.tgz".format(timenow_str))
    except:
        None
