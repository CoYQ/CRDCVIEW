# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created: Qiu Yuqin 16 20:53:33 2016
#      by: PyQt4 UI code generator 4.10.4
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from connectEC2 import *
import global_list
# from CRDC import *

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

class Ui_Login(QtGui.QWidget, QtCore.QObject):
    loginForm = None
    def setupUi(self, Login):
        self.loginForm = Login
        Login.setObjectName(_fromUtf8("Login"))
        Login.setWindowModality(QtCore.Qt.ApplicationModal)
        Login.resize(585, 332)
        self.widget = QtGui.QWidget(Login)
        self.widget.setGeometry(QtCore.QRect(40, 30, 511, 281))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label2_2 = QtGui.QLabel(self.widget)
        self.label2_2.setObjectName(_fromUtf8("label2_2"))
        self.horizontalLayout.addWidget(self.label2_2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.comboBox_cloudtype = QtGui.QComboBox(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_cloudtype.sizePolicy().hasHeightForWidth())
        self.comboBox_cloudtype.setSizePolicy(sizePolicy)
        self.comboBox_cloudtype.setObjectName(_fromUtf8("comboBox_cloudtype"))
        self.comboBox_cloudtype.addItem(_fromUtf8(""))
        self.comboBox_cloudtype.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.comboBox_cloudtype)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_username = QtGui.QLabel(self.widget)
        self.label_username.setLineWidth(2)
        self.label_username.setObjectName(_fromUtf8("label_username"))
        self.horizontalLayout_6.addWidget(self.label_username)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.lineEdit_username = QtGui.QLineEdit(self.widget)
        self.lineEdit_username.setObjectName(_fromUtf8("lineEdit_username"))
        self.horizontalLayout_6.addWidget(self.lineEdit_username)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_keyid = QtGui.QLabel(self.widget)
        self.label_keyid.setLineWidth(2)
        self.label_keyid.setObjectName(_fromUtf8("label_keyid"))
        self.horizontalLayout_2.addWidget(self.label_keyid)
        self.lineEdit_key_id = QtGui.QLineEdit(self.widget)
        self.lineEdit_key_id.setObjectName(_fromUtf8("lineEdit_key_id"))
        self.horizontalLayout_2.addWidget(self.lineEdit_key_id)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_access_key = QtGui.QLabel(self.widget)
        self.label_access_key.setObjectName(_fromUtf8("label_access_key"))
        self.horizontalLayout_3.addWidget(self.label_access_key)
        self.lineEdit_access_key = QtGui.QLineEdit(self.widget)
        self.lineEdit_access_key.setObjectName(_fromUtf8("lineEdit_access_key"))
        self.horizontalLayout_3.addWidget(self.lineEdit_access_key)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.loginbtn_login = QtGui.QPushButton(self.widget)
        self.loginbtn_login.setObjectName(_fromUtf8("loginbtn_login"))
        self.horizontalLayout_4.addWidget(self.loginbtn_login)
        self.loginbtn_exit = QtGui.QPushButton(self.widget)
        self.loginbtn_exit.setObjectName(_fromUtf8("loginbtn_exit"))
        self.horizontalLayout_4.addWidget(self.loginbtn_exit)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.retranslateUi(Login)
        QtCore.QObject.connect(self.loginbtn_login, QtCore.SIGNAL(_fromUtf8("clicked()")), self.loginactivity)
        QtCore.QObject.connect(self.loginbtn_exit, QtCore.SIGNAL(_fromUtf8("clicked()")), Login.reject)
        QtCore.QMetaObject.connectSlotsByName(Login)

    #login detect
    def loginactivity(self):
        if self.comboBox_cloudtype.currentIndex()==0:
            connEC2 = ConnEC2()
            global_list.login_ip = str(self.lineEdit_key_id.text())
            global_list.login_secret_access_key = str(self.lineEdit_access_key.text())
            result = connEC2.connect(global_list.login_ip, global_list.login_secret_access_key)
            if result == True:
                # QtCore.QObject.connect(self.loginbtn_login, QtCore.SIGNAL(_fromUtf8("clicked()")), self.reject)
                print "登陆账户成功！"
                global_list.ui_CRDC.usernamelable.setText(
                    _translate("CRDC", u"用户名：" + self.lineEdit_username.text(), None))
                QtGui.QMessageBox.information(self, "Warning", u"登录成功！")
                # global_list.ui_CRDC.OutputtextEdit.append(u"创建虚拟机成功！")
                self.loginForm.reject()
            else:
                r = QtGui.QMessageBox.information(self, "Warning", u"登录名或秘钥有误，登录失败",
                                                  QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
                if r == QtGui.QMessageBox.Yes:
                    self.loginname.clear()
                    self.loginname_2.clear()
        elif self.comboBox_cloudtype.currentIndex()==1:
            self.label_username.setText(_translate("Login", "Domain", None))
            self.label_keyid.setText(_translate("Login", "User Name", None))
            self.label_access_key.setText(_translate("Login", "Password", None))
            if self.label_keyid.text()== None or self.label_username.text()== None:
                QtGui.QMessageBox.information(self, "Warning", u"请填写登录名及域")
            else:
                self.loginForm.reject()
    def retranslateUi(self, Login):
        Login.setWindowTitle(_translate("Login", "Login", None))
        self.label2_2.setText(_translate("Login", "云平台", None))
        self.comboBox_cloudtype.setItemText(0, _translate("Login", "EC2", None))
        self.comboBox_cloudtype.setItemText(1, _translate("Login", "OpenStack", None))
        self.label_username.setText(_translate("Login", "用户名", None))
        self.label_keyid.setText(_translate("Login", "aws_access_key_id", None))
        self.label_access_key.setText(_translate("Login", "aws_secret_access_key", None))
        self.loginbtn_login.setText(_translate("Login", "登录", None))
        self.loginbtn_exit.setText(_translate("Login", "退出", None))