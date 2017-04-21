#!usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import time

FILEDic = {'firefox':'/usr/lib/firefox/libnss3.so', 'mail':'', 'ntpd':'', 'ssh':''}

if __name__ == '__main__':
    print 'hello'
    username = sys.argv[1]
    # path = '/home/' + str(username) + '/detect/'
    # os.system('tar -xvzf ./detect/zlib-1.2.3.tar.gz')
    # os.system('cd zlib-1.2.3.tar.gz')
    # os.system('./configure')
    # os.system('make')
    # os.system('sudo make install')
    # os.system('cd ..')
    # os.system('ls | grep "attack$" && rm ./attack')
    # os.system('ls | grep "attack_data.txt$" && rm ./attack_data.txt')
    # os.system('gcc attack.c -o attack -lz')
    inparam = sys.argv[2]
    scList = str(inparam).split('/')
    for sc in scList:
        filePath = FILEDic[sc]
        print "starting detect by " + str(sc)
        count = 0
        while count < 5:
            print str(count + 1) + "th group detecting starts."
            # os.system(path + 'attack ' + str(filePath) + ' ' + str(count))
            time.sleep(900)
            print str(count + 1) + "th group done."
            count += 1
            pass
        print "finished"
    print "************************************************"
    print "printing result..."
