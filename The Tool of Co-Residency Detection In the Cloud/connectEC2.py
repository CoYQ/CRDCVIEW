#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Yuan'
import boto.ec2
from collections import defaultdict
import time
import sys
import global_list
from Queue import Queue
from PyQt4 import QtCore, QtGui

reload(sys)
sys.setdefaultencoding("utf-8")

# class ConnEC2
'''
    function: connect EC2
    connect(): login
    getInstance(): get All instances' domanID and IP
    creatInstance(): create instance/VM
    runInstance(): start instance/VM, inparam:idList:instance's id of needing start
'''


class ConnEC2:
    instanceDic = defaultdict()

    def __init__(self):
        pass

    # 连接虚拟机
    def connect(self, aws_access_key_id, aws_secret_access_key):
        try:
            self.conn = boto.ec2.connect_to_region('cn-north-1', \
                                                   aws_access_key_id=aws_access_key_id, \
                                                   aws_secret_access_key=aws_secret_access_key)
            reservations = self.conn.get_all_instances()
            # instances = reservations[0].instances
            if reservations is not None:
                ok = True
            else:
                ok = False
                # for reservation in list(reservations):
                #     # print reservation
                #     instances = reservation.instances
                #     for instance in list(instances):
                #         _id = str(instance).split(':')[1]
                #         self.instanceDic[_id] = str(instance.ip_address)
                # print instance, '\t', instance.ip_address
        except:
            ok = False
        return ok

    # 获得虚拟机实例
    def getInstance(self):
        reservations = self.conn.get_all_instances()
        for reservation in list(reservations):
            instances = reservation.instances
            for instance in list(instances):
                _id = str(instance).split(':')[1]
                self.instanceDic[instance.ip_address] = str(_id)
        # images = self.conn.get_all_images()
        # # images.__doc__
        return self.instanceDic

    # 创建虚拟机实例
    def creatInstance(self, imageName=None, keyName=None, count=None, instanceType='t2.micro'):
        typeDic = {'ubuntu': 'ami-0220b23b'}
        imageNo = typeDic[str(imageName)]
        print imageNo
        print keyName
        print count
        print instanceType
        # imageName = 'ami-0220b23b'
        # count = 1
        # keyName = 'HomeAloneKey'
        # instanceType = 't2.micro'
        try:
            print "开始创建，等待1分钟"
            tmpReservation = self.conn.run_instances(image_id=imageNo, max_count=int(str(count)),
                                                     min_count=int(str(count)), \
                                                     key_name=str(keyName), instance_type=instanceType)
            time.sleep(60)
            print "创建结束"
            if tmpReservation is not None:
                ok = True
            else:
                ok = False
        except:
            ok = False
        return ok

    # 运行虚拟机
    def runInstance(self, idList):
        runList = idList
        statusList = self.conn.get_all_instance_status(instance_ids=idList)
        print statusList
        for status in statusList:
            inst = str(status).split(':')[1]
            if inst in runList:
                runList.remove(inst)
        try:
            tmpReservation = self.conn.start_instances(instance_ids=runList)
            time.sleep(60)
            if tmpReservation is not None:
                ok = True
            else:
                ok = False
        except:
            ok = False
        return ok

    def __del__(self):
        self.close()

    # def main(self):
    #     instDic = defaultdict()
    #     connEC2 = ConnEC2()
    #     aws_access_key_id = ''
    #     aws_secret_access_key = ''
    #     print connEC2.connect(aws_access_key_id, aws_secret_access_key)
    #     instDic = connEC2.getInstance()
    #     for _id, IP in instDic.iteritems():
    #         print _id, '\t', IP
    #     print "starting"
    #     print connEC2.creatInstance(imageName = 'ubuntu', count='1', keyName='HomeAloneKey', instanceType='t2.micro')
    #     print 'done'
    #     instDic = connEC2.getInstance()
    #     for _id, IP in instDic.iteritems():
    #         print _id, '\t', IP
    #     instList = ['i-bcf1ad04', 'i-7c4c10c4']
    #     connEC2.runInstance(instList)
    # if __name__ == '__main__':
    #     main()
