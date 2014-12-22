#!/usr/bin/python

# Debug

#import logging
#logging.basicConfig(level=logging.DEBUG,filename='/tmp/fabric.debug.log')

from fabric.api import *
from fabric.colors import *

# Define sets of servers as roles
env.roledefs = {
    'localservers': ['localhost'],
    'remoteservers': ['172.245.17.194']
}

# Set the user to use for ssh
env.user = 'root'

@roles('localservers','remoteservers')

def get_os_ver(verbose=False):
	run('cat /etc/issue')
