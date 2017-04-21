# coding=utf-8
__author__ = 'YuanLipeng'

import threading
from Connect import *
import time
import global_list
from PyQt4 import QtGui
from collections import defaultdict

class HomeAloneDetect():
    # self.filePath = '/home/uername/'
    def __init__(self, host, username, private_key, scList, vmport):
        # host = '54.222.252.118'
        # private_key = 'HomeAloneKey.pem'
        # username = 'ubuntu'
        # scList = 'firefox'
        print 'ok1'
        self.t = threading.Thread(target=self.detect1, args=(host, username, private_key, scList, vmport))
        pass

    def detect1(self, host, username, private_key, scList, vmport):
        FILEDic = {'firefox': '/usr/lib/firefox/libnss3.so', 'mail': '/usr/lib/firefox/libnss3.so', 'ntpd': '/usr/lib/firefox/libnss3.so', 'ssh': ''}
        ssh = Connection(host=host, username=username, passwd=private_key, port=vmport)
        print 'success connect'
        print ssh
        global_list.ui_CRDC.textEdit_outputHomealone.append(u'远程连接成功')
        #ssh.execute('su')
        #ssh.execute('1')
        #ssh.execute('cd /root')
        # tmpcommand = 'cd /home/' + username
        # ssh.execute(tmpcommand)
        ssh.execute('ls | grep "detect$" && rm -r detect/')
        ssh.execute('mkdir detect')

        print 'putting detect file.'
        ssh.put('homeAlone/zlib-1.2.8.tar.gz', './detect/zlib-1.2.8.tar.gz')
        ssh.put('homeAlone/config.sh', './detect/config.sh')
        ssh.put('homeAlone/attack.c', './detect/attack.c')
        # ssh.put('homeAlone/attack.py', './detect/attack.py')
        ssh.put('homeAlone/stop.sh', './detect/stop.sh')
        print 'put all.'

        t = ssh.execute('chmod +x ./detect/config.sh')
        out = ssh.execute('./detect/config.sh')

        print out
        time.sleep(2)
        exit1 = False
        for sc in scList:
            filePath = FILEDic[sc]

            print "starting detect by " + str(sc)
            global_list.ui_CRDC.textEdit_outputHomealone.append(u"通过" + str(sc) + u'检测：')

            count = 0
            while count < 5:
                print str(count + 1) + "th group detecting starts."
                # print "li"
                # global_list.hmPrintText = global_list.ui_CRDC.textEdit_outputHomealone.textCursor()
                # global_list.hmPrintText.movePosition(QtGui.QTextCursor.End)
                # global_list.hmPrintText.insertText(u"开始第" + str(count + 1) + u"组检测." + '\n')
                # global_list.ui_CRDC.textEdit_outputHomealone.setTextCursor(global_list.hmPrintText)
                # global_list.ui_CRDC.textEdit_outputHomealone.ensureCursorVisible()
                global_list.ui_CRDC.textEdit_outputHomealone.append(u"开始第" + str(count + 1) + u"组检测：")
                # os.system(path + 'attack ' + str(filePath) + ' ' + str(count))
                output = ssh.execute('./detect/attack ' + str(filePath) + ' ' + str(count + 1) + ' ' + str(sc))
                for line in output:
                    # global_list.hmPrintText = global_list.ui_CRDC.textEdit_outputHomealone.textCursor()
                    # global_list.hmPrintText.movePosition(QtGui.QTextCursor.End)
                    # global_list.hmPrintText.insertText('\t' + str(line))
                    # global_list.ui_CRDC.textEdit_outputHomealone.setTextCursor(global_list.hmPrintText)
                    # global_list.ui_CRDC.textEdit_outputHomealone.ensureCursorVisible()
                    global_list.ui_CRDC.textEdit_outputHomealone.append(u'    ' + str(line))

                if len(output) == 0:
                    exit1 = True
                    break
                time.sleep(1)
                print str(count + 1) + "th group done."
                count += 1
                pass
            if exit1:
                break
            print "finished"

            # global_list.hmPrintText = global_list.ui_CRDC.textEdit_outputHomealone.textCursor()
            # global_list.hmPrintText.movePosition(QtGui.QTextCursor.End)
            # global_list.hmPrintText.insertText('\n')
            # global_list.ui_CRDC.textEdit_outputHomealone.setTextCursor(global_list.hmPrintText)
            # global_list.ui_CRDC.textEdit_outputHomealone.ensureCursorVisible()

        print "************************************************"
        print "printing result..."
        if exit1:
            print '检测被终止'
            global_list.ui_CRDC.textEdit_outputHomealone.append(u"*************************************************\n检测被终止。")
            ssh.close()
            return 1
        resultStr = self.getResult(host, username, private_key,vmport)
        if (resultStr is True) and (exit1 is False):
            global_list.ui_CRDC.textEdit_outputHomealone.append(
                u"*************************************************\n检测结果：\n" + str(host) + u"实例是平台独占的.")
        elif (resultStr is False) and (exit1 is False):
            global_list.ui_CRDC.textEdit_outputHomealone.append(
                u"*************************************************\n检测结果：\n" + str(host) + u"实例不是平台独占的.")
        ssh.close()
        return 0

    def startDetect(self):
        self.t.start()

    def stop(self, host, username, private_key, vmport):
        ssh1 = Connection(host=host, username=username, passwd=private_key, port=vmport)
        print 'success connect'
        t = ssh1.execute('chmod +x ./detect/stop.sh')
        out = ssh1.execute('./detect/stop.sh')
        ssh1.close()
        return out

    def getResult(self, host, username, private_key, vmport):
        resultDic = defaultdict()
        nowTime = time.strftime('%Y%m%d-%H%M%S', time.localtime(time.time()))
        ssh2 = Connection(host=host, username=username, passwd=private_key, port=vmport)
        ssh2.get('./detect/result_data.txt', 'homeAlone/' + nowTime)
        count = 0
        sCount = 0
        with open('./homeAlone/' + nowTime, 'r') as f:
            lines = f.readlines()
            # print lines
            for line in lines:
                # print line
                tmpList = str(line).replace('\n', '').split('\t')
                # print tmpList
                if resultDic.get(tmpList[0]) is None:
                    resultDic[tmpList[0]] = defaultdict()
                resultDic[tmpList[0]][tmpList[1]] = float(tmpList[2])
            # 评判是否同驻
            for keyStr, valueStr in resultDic.iteritems():
                print keyStr
                cnt = 0
                for group, timestr in valueStr.iteritems():
                    print group, '\t', timestr
                    if timestr < 14.0:
                        cnt += 1
                if cnt >= 3:
                    count += 1
            sCount = len(resultDic)
        ssh2.close()
        if sCount - count < 1:
            return True
        return False

def main():

    host = '218.241.135.34'
    private_key = 'id_rs'
    username = 'ubuntu'
    scList = 'mail'
    hm = HomeAloneDetect()
    hm.startDetect()
    # hm.detect1(host, username, private_key, scList)

if __name__ == '__main__':
    main()
