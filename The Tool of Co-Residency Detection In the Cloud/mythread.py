# -*- coding: utf-8 -*-
# Created: Qiu Yuqin 8/21 2016

import threading
import os
import signal

class MyTread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name=name
        self.func=func
        self.args=args
        self.res =None
    #return result
    def getResult(self):
        while not self.res:
            pass
        return self.res
    #call函数
    def run(self):
        print 'starting' ,self.name
        self.res=apply(self.func, self.args)
    #exit函数
    def __exit__(self, exc_type, exc_val, exc_tb):
        os.kill(os.getpid(), signal.SIGTERM)