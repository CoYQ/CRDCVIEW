# -*- coding: utf-8 -*-
__author__ = 'Qiu Yuqin'

import global_list
from PyQt4 import QtGui,QtCore
from Connect import *
import time
import string



class Randomtest(QtGui.QWidget,QtCore.QObject):
    global RandomtestselectedIndex
    global hostsdict
    def __init__(self):
        pass

    def config(self,host, username, private_key):
        ok=True
        try:
            ssh = Connection(host, username, private_key)
            ssh.put('ec\g.rb')
            #print "g.rb ok transport"
            ssh.put('ec\ec.c')
            #print "ec.rb ok transport"
            ssh.put('ec\config.py')
            ssh.put('ec\stop.sh')
            # ssh.put('ec\hvcalls-0.2.tar.gz')
            ssh.execute('python config.py')
            #print "excute config.py ok"
            ssh.close()
            #print "config is ok"
            #print out[0].strip()
        except:
            ok = False
            # print host+u"配置失败"
        if ok== True:
            global_list.ui_CRDC.OutputtextEdit.append(host + u"虚拟机随机同驻检测环境配置成功！")
        else:
            global_list.ui_CRDC.OutputtextEdit.append(host + u"虚拟机随机同驻检测环境配置失败！")
        return ok
    def detectDomainID(self,hostsdict,host, username, private_key,rowID):
        sign=True
        try:
            ssh = Connection(host, username, private_key)
            out = ssh.execute('sudo ./g.rb')
            domainid=out[0].strip()
            hostsdict[host]['domainID'] =domainid
            #print "domainid:" +hostsdict[host]['domainID']
            ssh.close()
        except:
            sign=False
        if ((sign==True)&(len(domainid)<6)):
            newitem = QtGui.QTableWidgetItem(str(domainid))
            global_list.ui_CRDC.TableWidget_randomtest_VMIP.setItem(rowID, 1, newitem)
        else:
            global_list.ui_CRDC.OutputtextEdit.append(host + u"domainID检测失败，重新配置虚拟机！")
        return hostsdict
    def detect(self,selectedIndex,hostsdict):
        global selected_listbox
        ok=True
        #VM1
        ip0=selectedIndex[0]
        username0=hostsdict[str(selectedIndex[0])]['username']
        pKey0=hostsdict[str(selectedIndex[0])]['private_key']
        domianID0=hostsdict[str(selectedIndex[0])]['domainID']
        #VM2
        ip1 = selectedIndex[1]
        username1 = hostsdict[str(selectedIndex[1])]['username']
        pKey1 = hostsdict[str(selectedIndex[1])]['private_key']
        domianID1 = hostsdict[str(selectedIndex[1])]['domainID']
        ssh1 = Connection(str(ip0), username0, pKey0)
        cmd = 'sudo ./ec 0 %s' % domianID1
        output = ssh1.execute(cmd)
        ssh1.close()
        ssh2 = Connection(str(ip1),username1, pKey1)
        cmd = 'sudo ./ec 1 %s %s' % (domianID0, output[0].strip())
        output2 = ssh2.execute(cmd)
        ssh2.close()
        print "detect:"+domianID0+"+"+domianID1
        if str(output2[0]) == 'Yes\n':
            global_list.ui_CRDC.OutputtextEdit.append(ip0 + "and" + ip1 + u"虚拟机同驻")
            ok=True
        else:
            global_list.ui_CRDC.OutputtextEdit.append(ip0 + "and" + ip1 + u"虚拟机不同驻")
            ok=False
        return ok
        # cursor = global_list.ui_CRDC.OutputtextEdit.textCursor()
        # cursor.movePosition(QtGui.QTextCursor.End)
        # global_list.ui_CRDC.global_list.ui_CRDC.OutputtextEdit.setTextCursor(cursor)
    def stop(self, host, username, private_key):
        ssh1 = Connection(host, username, private_key)
        print 'success connect'
        t = ssh1.execute('chmod +x ./stop.sh')
        out = ssh1.execute('./stop.sh')
        ssh1.close()
        print out
        return out
