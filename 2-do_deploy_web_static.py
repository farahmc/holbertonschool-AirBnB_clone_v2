#!/usr/bin/python3
""" Fabric script that distributes an archive to your web servers"""
import os.path
from fabric.api import *

env.hosts = ['3.92.23.198', '54.174.101.66']


def do_deploy(archive_path):
    """ Distribute an archive to your web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        """ upload archive """
        put(archive_path, "/tmp/")

        """ create directory and uncompress """
        archive = archive_path.split("/")[-1]
        filename = archive_path_split.split(".")[0]
        directory = "/data/web_static/releases/" + filename
        run("mkdir -p {}".format(directory))
        run("tar -xzf /tmp/{} -C {}".format(archive, directory))

        """ move subdirectory into correct directory"""
        run("mv {0}/web_static/* {0}".format(directory))

        """ delete archive & directory"""
        run("rm /tmp/{}".format(archive))
        run("rm -rf {}/web_static".format(directory))

        """ delete old symlink & create new symlink """
        run("rm -rf /data/web_static/current/")
        run("ln -s {} /data/web_static/current".format(directory))

    except:
        return False
