#!usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os

if __name__ == '__main__':
    username = sys.argv[1]
    print 'start config ...'
    os.system('cd /home/' + str(username) + '/detect/')
    # os.system('tar -xvzf ./detect/zlib-1.2.3.tar.gz')
    # os.system('cd zlib-1.2.3.tar.gz')
    # os.system('./configure')
    # os.system('make')
    # os.system('sudo make install')
    # os.system('cd ..')
    os.system('ls | grep "attack$" && rm ./attack')
    os.system('ls | grep "attack_data.txt$" && rm ./attack_data.txt')
    os.system('gcc attack.c -o attack -lz')
    print 'config finished'