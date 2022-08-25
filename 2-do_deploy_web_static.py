#!/usr/bin/python3
""" Fabric script that distributes an archive to your web servers"""
import os.path
from fabric.api import *

env.hosts = ['3.92.23.198', '54.174.101.66']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """ Distribute an archive to your web servers"""
    if os.path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        archive_path_split = archive_path.split("/")[1]
        filename = archive_path_split.split(".")[0]
        run("mkdir -p /data/web_static/releases/{}".format(filename))
        run("tar -xf /tmp/{} -C /data/web_static/releases/{}".
            format(archive_path_split, filename))

        run("rm /tmp/{}".format(archive_path_split))

        run("rm -rf /data/web_static/current")

    except:
        return False
