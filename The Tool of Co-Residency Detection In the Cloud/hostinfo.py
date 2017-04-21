# -*- coding: utf-8 -*-
# !/usr/bin/python


class HostInfo(object):
    def __init__(self, host, username,port=None, private_key=None, passwd=None,domainID=None):
        self.host = host
        self.port = port
        self.username = username
        self.private_key = private_key
        self.passwd = passwd
        self.domainID =domainID
    def getHostInfo(self,host):
        pass
