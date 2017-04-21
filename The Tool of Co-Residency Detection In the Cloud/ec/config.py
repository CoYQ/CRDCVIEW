#!/usr/bin/env python

import os

os.system('sudo apt-get update')

os.system('sudo apt-get install gcc libxen-dev xen-utils ruby -y')

os.system('sudo mount -t xenfs xenfs /proc/xen')

os.system('gcc -o ec ec.c')

os.system('chmod u+x g.rb')