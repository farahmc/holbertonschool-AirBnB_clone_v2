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
        """ upload archive """
        put(archive_path, "/tmp/")

    except:
        return False
