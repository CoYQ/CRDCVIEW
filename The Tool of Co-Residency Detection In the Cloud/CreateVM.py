# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateVM.ui'
#
# Created: Sun Jul 17 21:26:52 2016
#      by: PyQt4 UI code generator 4.10.4
# key= HomeAloneKey
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from connectEC2 import *
import global_list
from mythread import MyTread
import threading
from time import sleep,ctime

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(QtGui.QWidget, QtCore.QObject):


    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(532, 277)
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 40, 421, 201))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox_VMname = QtGui.QComboBox(self.layoutWidget)
        self.comboBox_VMname.setObjectName(_fromUtf8("comboBox_VMname"))
        self.comboBox_VMname.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_VMname, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.lineEdit_keyname = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_keyname.setObjectName(_fromUtf8("lineEdit_keyname"))
        self.gridLayout.addWidget(self.lineEdit_keyname, 1, 1, 1, 1)
        self.lineEdit_count = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_count.setObjectName(_fromUtf8("lineEdit_count"))
        self.gridLayout.addWidget(self.lineEdit_count, 4, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.comboBox_typevale = QtGui.QComboBox(self.layoutWidget)
        self.comboBox_typevale.setObjectName(_fromUtf8("comboBox_typevale"))
        self.comboBox_typevale.addItem(_fromUtf8(""))
        self.comboBox_typevale.addItem(_fromUtf8(""))
        self.comboBox_typevale.addItem(_fromUtf8(""))
        self.comboBox_typevale.addItem(_fromUtf8(""))
        self.comboBox_typevale.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_typevale, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.VMbuilt)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def VMbuilt(self):
        #ubuntu
        print self.comboBox_VMname.currentText()
        #homealonekey
        print self.lineEdit_keyname.text()
        #t2.micro
        print self.comboBox_typevale.currentText()
        #1
        print self.lineEdit_count.text()
        # global Ui_Login.login_ip
        print global_list.login_ip
        print global_list.login_secret_access_key
        connEC2CreateVM = ConnEC2()
        resultconnt =connEC2CreateVM.connect(global_list.login_ip,global_list.login_secret_access_key)
        print resultconnt
        print str(self.comboBox_VMname.currentText())
        print str(self.lineEdit_keyname.text())
        print str(self.lineEdit_count.text())
        print str(self.comboBox_typevale.currentText())
        if resultconnt==True:
            QtGui.QMessageBox.information(self, "Warning", u"请等待一分钟，正在配置！")
            vmname=str(self.comboBox_VMname.currentText())
            vmpasswordname=str(self.lineEdit_keyname.text())
            vmtype=str(self.lineEdit_count.text())
            vmnumber=str(self.comboBox_typevale.currentText())

            # args=[vmname,vmpasswordname,vmtype,vmnumber]
            #vmcreat=threading.Thread(target=connEC2CreateVM.creatInstance,args=(vmname,vmpasswordname,vmtype,vmnumber))
            # resultVM=connEC2CreateVM.creatInstance(str(self.comboBox_VMname.currentText()),str(self.lineEdit_keyname.text()),str(self.lineEdit_count.text()), str(self.comboBox_typevale.currentText()))
            #开启创建虚拟机线程
            vmcreat =MyTread(connEC2CreateVM.creatInstance, (vmname, vmpasswordname, vmtype, vmnumber),'CreatVM')
            # print 'VMcreat starting',ctime()
            vmcreat.start()
            # vmcreat.join()
            # # sleep(60)
            # resultVM=vmcreat.getResult()
            # # print 'VMcreat done', ctime()
            # print resultVM
            # # 获得返回结果
            # # getresult=MyTread(self.Waitresult,(),'get createvm result')
            # # getresult.start()
            # # print 'ok1'
            # if resultVM==True:
            #     QtGui.QMessageBox.information(self, "Warning", u"创建虚拟机成功")
            # else:
            #     QtGui.QMessageBox.information(self, "Warning", u"创建虚拟机失败")
        else:
            QtGui.QMessageBox.information(self, "Warning", u"用户未登陆，请先登陆账户！")





    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "创建虚拟机", None))
        self.label.setText(_translate("Dialog", "镜像文件", None))
        self.comboBox_VMname.setItemText(0, _translate("Dialog", "ubuntu", None))
        self.label_4.setText(_translate("Dialog", "登录密钥", None))
        self.label_3.setText(_translate("Dialog", "实例类型", None))
        self.label_2.setText(_translate("Dialog", "虚拟机数量", None))
        self.comboBox_typevale.setItemText(0, _translate("Dialog", "t2.micro", None))
        self.comboBox_typevale.setItemText(1, _translate("Dialog", "t2.small", None))
        self.comboBox_typevale.setItemText(2, _translate("Dialog", "t2.medium", None))
        self.comboBox_typevale.setItemText(3, _translate("Dialog", "t2.large", None))
        self.comboBox_typevale.setItemText(4, _translate("Dialog", "m3.medium", None))
        self.pushButton.setText(_translate("Dialog", "确定", None))
        self.pushButton_2.setText(_translate("Dialog", "取消", None))
    #
    # def Waitresult(self):
    #     print 'qiuyuqin'
    #     time.sleep(60)
    #     resultvm =self.vmcreat.getResult()
    #     print resultvm
    #     if resultvm == True:
    #         QtGui.QMessageBox.information(self, "Warning", u"创建虚拟机成功")
    #     else:
    #         QtGui.QMessageBox.information(self, "Warning", u"创建虚拟机失败")
    #     return resultvm

