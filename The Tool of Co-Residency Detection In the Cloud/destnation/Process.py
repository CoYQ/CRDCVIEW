# -*- coding: utf-8 -*-
# !/usr/bin/python
from Connect import Connection
import thread, time, logging
from hostinfo import HostInfo
from Client import Client
import pdb


class DesProcessor:
    def __init__(self, hostlist=None, desComputerIP=None, desPort=None, comSpeed=None, output_signal=None,
                 complete_signal=None):
        self.Flooder = 'destnation/Flooder.py'
        self.hostlist = hostlist
        self.desComputerIP = desComputerIP
        self.desPort = desPort
        self.comSpeed = comSpeed
        self.conn = None
        self.output_signal = output_signal
        self.complete_signal = complete_signal
        self.total = 0
        self.fake = 0

    def stopAll(self):
        if self.conn:
            self.conn.close()
        self.hostlist = []
        self.updateState(u"……………………………………………………………………………………")
        self.updateState(u"检测停止,共有%s台虚拟机与目标主机同驻" % self.total)
        self.output_signal = None

    def updateState(self, info):
        try:
            print info
            self.output_signal.emit(info)
        except Exception as e:
            logging.error(u"进程已经被强行终止")

    def detectAll(self):
        for hostinfo in self.hostlist:
            self.total += self.detectOne(hostinfo)
        self.complete_signal.emit()
        self.updateState(u"……………………………………………………………………………………")
        self.updateState(u"检测完毕,共有%s台虚拟机与目标主机同驻" % self.total)

    def detectOne(self, hostinfo):
        self.updateState(u"……………………………………………………………………………………")
        self.updateState(u"检测虚拟机:%s" % hostinfo.host)
        try:
            print hostinfo.__dict__
            self.conn = Connection(port=hostinfo.port,host=hostinfo.host, username=hostinfo.username, passwd=hostinfo.passwd)
        except Exception as e:
            self.updateState(u"主机连接失败:%s" % e)
            return 0
        try:
            self.conn.execute("rm ./Flooder.py")
        except Exception as e:
            print e
        self.conn.put(localpath=self.Flooder, remotepath='./Flooder.py')
        client = Client(self.desComputerIP, self.desPort, 10, self.conn)
        resu = self.client_monitor(client)
        if resu:
            self.updateState(u"同驻")
            return 1
        else:
            self.updateState(u"不同驻")
            return 0

    def client_monitor(self, client):
        thread.start_new_thread(client.process_commucate, ())
        thread.start_new_thread(client.send_data, ())
        while not client.complete:
            pass
        return client.resu


def main():
    hostinfo = HostInfo(host='218.241.135.34', port=4358, username='root', passwd='1')
    ob = DesProcessor(desComputerIP='218.241.135.34',desPort=4356,hostlist=[hostinfo])
    ob.detectAll()


if __name__ == '__main__':
    main()
