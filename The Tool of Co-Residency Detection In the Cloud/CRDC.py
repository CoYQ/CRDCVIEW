# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CRDC.ui'
#
# Created: Sun Jul 24 16:30:30 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!
from collections import defaultdict
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QObject, pyqtSignal, pyqtSlot
from Login import *
from CreateVM import *
from hostinfo import HostInfo
from Random import Randomtest
from Monopoly import *
from destnation.Process import DesProcessor
import global_list
import thread
from mythread import MyTread
import operator

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


class Ui_CRDC(QtGui.QWidget, QtCore.QObject):
    # Random选择测试虚拟机
    # global RandomtestselectedIndex
    # 构造虚拟机
    global hostsdict
    serviceList = []
    ip = None
    hostsdict = defaultdict()
    hostsdict[ip] = defaultdict()
    hostsdict[ip]['host'] = ''
    hostsdict[ip]['username'] = ''
    hostsdict[ip]['private_key'] = ''
    hostsdict[ip]['domainID'] = ''
    hostsdict[ip]['port'] = ''
    '''
    hostsdict = [HostInfo(host='54.222.179.10', username='ubuntu', private_key='HomeAloneKey.pem',domainID='564')]
        # , HostInfo(host='4.2.79.11', username='ubuntu', private_key='HomeAloneKey.pem')
        # , HostInfo(host='54.222.179.112', username='ubuntu', private_key='HomeAloneKey.pem')
        # , HostInfo(host='54.222.179.13', username='ubuntu', private_key='HomeAloneKey.pem')
        # , HostInfo(host='54.222.179.14', username='ubuntu', private_key='HomeAloneKey.pem')
        # , HostInfo(host='54.222.179.16', username='ubuntu', private_key='HomeAloneKey.pem')]
    '''
    dict = []
    #####目标同驻检测
    selectedIndex = []
    output_refresh = pyqtSignal(str)
    complete_signal = pyqtSignal()
    complete = 1
    desProcessor = None

    def setupUi(self, CRDC):
        # 主界面
        CRDC.setObjectName(_fromUtf8("CRDC"))
        CRDC.resize(800, 700)
        CRDC.setAcceptDrops(False)
        CRDC.setAutoFillBackground(False)
        self.verticalLayout_15 = QtGui.QVBoxLayout(CRDC)
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.verticalLayout_login = QtGui.QVBoxLayout()
        self.verticalLayout_login.setObjectName(_fromUtf8("verticalLayout_login"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.usernamelable = QtGui.QLabel(CRDC)
        self.usernamelable.setObjectName(_fromUtf8("usernamelable"))
        self.horizontalLayout.addWidget(self.usernamelable)
        self.label = QtGui.QLabel(CRDC)
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        # 登录虚拟机
        self.Loginbtn = QtGui.QPushButton(CRDC)
        self.Loginbtn.setObjectName(_fromUtf8("Loginbtn"))
        self.horizontalLayout.addWidget(self.Loginbtn)
        self.Exitbtn_2 = QtGui.QPushButton(CRDC)
        self.Exitbtn_2.setObjectName(_fromUtf8("Exitbtn_2"))
        self.horizontalLayout.addWidget(self.Exitbtn_2)
        self.verticalLayout_login.addLayout(self.horizontalLayout)
        self.line_3 = QtGui.QFrame(CRDC)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_login.addWidget(self.line_3)
        self.verticalLayout_15.addLayout(self.verticalLayout_login)
        self.verticalLayout_VM = QtGui.QVBoxLayout()
        self.verticalLayout_VM.setObjectName(_fromUtf8("verticalLayout_VM"))
        self.horizontalLayout_login = QtGui.QHBoxLayout()
        self.horizontalLayout_login.setObjectName(_fromUtf8("horizontalLayout_login"))
        self.JianceChangjing = QtGui.QGroupBox(CRDC)
        self.JianceChangjing.setObjectName(_fromUtf8("JianceChangjing"))
        self.JCCJxialaicaidan = QtGui.QComboBox(self.JianceChangjing)
        self.JCCJxialaicaidan.setGeometry(QtCore.QRect(10, 30, 135, 27))
        self.JCCJxialaicaidan.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.JCCJxialaicaidan.setObjectName(_fromUtf8("JCCJxialaicaidan"))
        self.JCCJxialaicaidan.addItem(_fromUtf8(""))
        self.JCCJxialaicaidan.addItem(_fromUtf8(""))
        self.JCCJxialaicaidan.addItem(_fromUtf8(""))
        self.horizontalLayout_login.addWidget(self.JianceChangjing)
        spacerItem1 = QtGui.QSpacerItem(13, 13, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_login.addItem(spacerItem1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.CreateVMbtn = QtGui.QPushButton(CRDC)
        self.CreateVMbtn.setObjectName(_fromUtf8("CreateVMbtn"))
        self.verticalLayout.addWidget(self.CreateVMbtn)
        self.ReadVMinforbtn_2 = QtGui.QPushButton(CRDC)
        self.ReadVMinforbtn_2.setObjectName(_fromUtf8("ReadVMinforbtn_2"))
        self.verticalLayout.addWidget(self.ReadVMinforbtn_2)
        self.horizontalLayout_login.addLayout(self.verticalLayout)
        self.verticalLayout_VM.addLayout(self.horizontalLayout_login)
        self.line_2 = QtGui.QFrame(CRDC)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_VM.addWidget(self.line_2)
        self.verticalLayout_15.addLayout(self.verticalLayout_VM)

        # 随机同驻检测
        self.scrollArea_randomtest = QtGui.QScrollArea(CRDC)
        self.scrollArea_randomtest.setWidgetResizable(True)
        self.scrollArea_randomtest.setObjectName(_fromUtf8("scrollArea_randomtest"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 764, 194))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_14 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.TobeDetectedComputerName = QtGui.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.TobeDetectedComputerName.setFont(font)
        self.TobeDetectedComputerName.setFocusPolicy(QtCore.Qt.NoFocus)
        self.TobeDetectedComputerName.setObjectName(_fromUtf8("TobeDetectedComputerName"))
        self.verticalLayout_6.addWidget(self.TobeDetectedComputerName)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))

        # 随机同驻检测——读取虚拟机显示列表
        self.TableWidget_randomtest_VMIP = QtGui.QTableWidget(self.scrollAreaWidgetContents)
        self.TableWidget_randomtest_VMIP.setObjectName(_fromUtf8("listView_VMIP"))
        self.TableWidget_randomtest_VMIP.setColumnCount(2)
        self.TableWidget_randomtest_VMIP.setRowCount(15)
        self.TableWidget_randomtest_VMIP.setColumnWidth(0, 150)
        self.TableWidget_randomtest_VMIP.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.TableWidget_randomtest_VMIP.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        # self.TableWidget_randomtest_VMIP.setCurrentCell()
        # self.TableWidget_randomtest_VMIP.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        # self.TableWidget_randomtest_VMIP.setSelectionModel(QtGui.QAbstractItemView.ExtendedSelection)
        # 对表头文字的字体、颜色进行设置
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        # 获得水平方向表头的Item对象
        self.TableWidget_randomtest_VMIP.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        self.TableWidget_randomtest_VMIP.setHorizontalHeaderItem(1, item)
        self.verticalLayout_5.addWidget(self.TableWidget_randomtest_VMIP)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem2)
        # 虚拟机配置
        self.configuerDectectionbtn = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.configuerDectectionbtn.setObjectName(_fromUtf8("configuerDectectionbtn"))
        self.verticalLayout_2.addWidget(self.configuerDectectionbtn)
        #检测dimainID
        self.DetectDomainbtn = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.DetectDomainbtn.setObjectName(_fromUtf8("DetectDomainbtn"))
        self.verticalLayout_2.addWidget(self.DetectDomainbtn)
        # 按照domainID排序
        self.Sortdomainbtn = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.Sortdomainbtn.setObjectName(_fromUtf8("Sortdomainbtn"))
        self.verticalLayout_2.addWidget(self.Sortdomainbtn)
        # 开始检测按钮
        self.StartRandomTestDectectionbtn = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.StartRandomTestDectectionbtn.setObjectName(_fromUtf8("StartRandomTestDectectionbtn"))
        self.verticalLayout_2.addWidget(self.StartRandomTestDectectionbtn)
        # 停止检测
        self.StopDetectbtn = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.StopDetectbtn.setObjectName(_fromUtf8("StopDetectbtn"))
        self.verticalLayout_2.addWidget(self.StopDetectbtn)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        # 输出检测结果text
        self.OutputtextEdit = QtGui.QTextEdit(self.scrollAreaWidgetContents)
        self.OutputtextEdit.setObjectName(_fromUtf8("OutputtextEdit"))
        self.OutputtextEdit.setReadOnly(True)
        # tEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.verticalLayout_3.addWidget(self.OutputtextEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.verticalLayout_14.addLayout(self.verticalLayout_6)
        self.scrollArea_randomtest.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_15.addWidget(self.scrollArea_randomtest)

        # 目标同驻检测
        self.DestationDetectScrollArea = QtGui.QScrollArea(CRDC)
        self.DestationDetectScrollArea.setWidgetResizable(True)
        self.DestationDetectScrollArea.setObjectName(_fromUtf8("DestationDetectScrollArea"))
        self.scrollAreaWidgetContents_3 = QtGui.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 764, 328))
        self.scrollAreaWidgetContents_3.setObjectName(_fromUtf8("scrollAreaWidgetContents_3"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.verticalLayout_canshu = QtGui.QVBoxLayout()
        self.verticalLayout_canshu.setObjectName(_fromUtf8("verticalLayout_canshu"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.DestinationComputerName = QtGui.QLabel(self.scrollAreaWidgetContents_3)
        self.DestinationComputerName.setEnabled(True)
        self.DestinationComputerName.setObjectName(_fromUtf8("DestinationComputerName"))
        self.horizontalLayout_8.addWidget(self.DestinationComputerName)
        self.DesinationComputerIP = QtGui.QLineEdit(self.scrollAreaWidgetContents_3)
        self.DesinationComputerIP.setObjectName(_fromUtf8("DesinationComputerIP"))
        self.horizontalLayout_8.addWidget(self.DesinationComputerIP)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.socketName = QtGui.QLabel(self.scrollAreaWidgetContents_3)
        self.socketName.setObjectName(_fromUtf8("socketName"))
        self.horizontalLayout_9.addWidget(self.socketName)
        self.SoceketText = QtGui.QLineEdit(self.scrollAreaWidgetContents_3)
        self.SoceketText.setObjectName(_fromUtf8("SoceketText"))
        self.horizontalLayout_9.addWidget(self.SoceketText)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.CommunicationSpeedName = QtGui.QLabel(self.scrollAreaWidgetContents_3)
        self.CommunicationSpeedName.setObjectName(_fromUtf8("CommunicationSpeedName"))
        self.horizontalLayout_10.addWidget(self.CommunicationSpeedName)
        self.CommunicationSpeedSpinBox = QtGui.QLabel(self.scrollAreaWidgetContents_3)
        # self.CommunicationSpeedSpinBox.setMaximum(1000000000)
        self.CommunicationSpeedSpinBox.setObjectName(_fromUtf8("CommunicationSpeedSpinBox"))
        self.horizontalLayout_10.addWidget(self.CommunicationSpeedSpinBox)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_10)
        self.verticalLayout_canshu.addLayout(self.horizontalLayout_7)
        self.line_4 = QtGui.QFrame(self.scrollAreaWidgetContents_3)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout_canshu.addWidget(self.line_4)
        self.verticalLayout_10.addLayout(self.verticalLayout_canshu)
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.TobeDetectedComputerName_2 = QtGui.QLabel(self.scrollAreaWidgetContents_3)
        self.TobeDetectedComputerName_2.setObjectName(_fromUtf8("TobeDetectedComputerName_2"))
        self.verticalLayout_11.addWidget(self.TobeDetectedComputerName_2)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))

        self.VMTobeSelectedList = QtGui.QTableWidget(0, 1, self.scrollAreaWidgetContents_3)
        self.VMTobeSelectedList.setObjectName(_fromUtf8("VMTobeSelectedList"))
        self.VMTobeSelectedList.setColumnWidth(0, 300)
        self.VMTobeSelectedList.setHorizontalHeaderLabels(QtCore.QString(u"主机列表;").split(";"))
        self.VMTobeSelectedList.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

        self.horizontalLayout_11.addWidget(self.VMTobeSelectedList)
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.SelectAll = QtGui.QPushButton(self.scrollAreaWidgetContents_3)
        self.SelectAll.setObjectName(_fromUtf8("SelectAll"))
        self.verticalLayout_12.addWidget(self.SelectAll)
        self.Select = QtGui.QPushButton(self.scrollAreaWidgetContents_3)
        self.Select.setObjectName(_fromUtf8("Select"))
        self.verticalLayout_12.addWidget(self.Select)
        self.DisSelect = QtGui.QPushButton(self.scrollAreaWidgetContents_3)
        self.DisSelect.setObjectName(_fromUtf8("DisSelect"))
        self.verticalLayout_12.addWidget(self.DisSelect)
        self.horizontalLayout_11.addLayout(self.verticalLayout_12)
        self.VMSelectedList = QtGui.QTextEdit(self.scrollAreaWidgetContents_3)
        self.VMSelectedList.setObjectName(_fromUtf8("VMSelectedList"))
        self.horizontalLayout_11.addWidget(self.VMSelectedList)
        self.verticalLayout_11.addLayout(self.horizontalLayout_11)
        self.verticalLayout_10.addLayout(self.verticalLayout_11)
        self.verticalLayout_13 = QtGui.QVBoxLayout()
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.FlooderName = QtGui.QLabel(self.scrollAreaWidgetContents_3)
        self.FlooderName.setObjectName(_fromUtf8("FlooderName"))
        self.horizontalLayout_13.addWidget(self.FlooderName)
        # self.FlooderSelectBox = QtGui.QSpinBox(self.scrollAreaWidgetContents_3)
        # self.FlooderSelectBox.setMaximum(1000)
        # self.FlooderSelectBox.setObjectName(_fromUtf8("FlooderSelectBox"))
        # self.horizontalLayout_13.addWidget(self.FlooderSelectBox)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.startbtn_2 = QtGui.QPushButton(self.scrollAreaWidgetContents_3)
        self.startbtn_2.setObjectName(_fromUtf8("startbtn_2"))
        self.horizontalLayout_14.addWidget(self.startbtn_2)
        self.stopbtn_2 = QtGui.QPushButton(self.scrollAreaWidgetContents_3)
        self.stopbtn_2.setObjectName(_fromUtf8("stopbtn_2"))
        self.horizontalLayout_14.addWidget(self.stopbtn_2)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_14)
        self.verticalLayout_13.addLayout(self.horizontalLayout_12)
        self.Ouput = QtGui.QTextEdit(self.scrollAreaWidgetContents_3)
        self.Ouput.setObjectName(_fromUtf8("Ouput"))
        self.Ouput.setReadOnly(True)
        self.verticalLayout_13.addWidget(self.Ouput)
        self.verticalLayout_10.addLayout(self.verticalLayout_13)
        self.verticalLayout_9.addLayout(self.verticalLayout_10)
        self.DestationDetectScrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_15.addWidget(self.DestationDetectScrollArea)

        # 平台独占性检测
        self.scrollArea_homealon = QtGui.QScrollArea(CRDC)
        self.scrollArea_homealon.setWidgetResizable(True)
        self.scrollArea_homealon.setObjectName(_fromUtf8("scrollArea_homealon"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 764, 417))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.groupBox_shenqingduzhanfuwu = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_shenqingduzhanfuwu.setObjectName(_fromUtf8("groupBox_shenqingduzhanfuwu"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.groupBox_shenqingduzhanfuwu)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        # 申请独占服务 虚拟机服务列表
        self.comboBox_applyVMduzhanfuwu = QtGui.QComboBox(self.groupBox_shenqingduzhanfuwu)
        self.comboBox_applyVMduzhanfuwu.setObjectName(_fromUtf8("comboBox_applyVMduzhanfuwu"))
        # 添加服务
        # self.comboBox_applyVMduzhanfuwu.addItem(_fromUtf8(""))
        # self.comboBox_applyVMduzhanfuwu.addItem(_fromUtf8(""))
        self.verticalLayout_7.addWidget(self.comboBox_applyVMduzhanfuwu)
        self.verticalLayout_4.addWidget(self.groupBox_shenqingduzhanfuwu)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        self.verticalLayout_4.addItem(spacerItem4)
        self.groupBox_serverlist = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_serverlist.setObjectName(_fromUtf8("groupBox_serverlist"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox_serverlist)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.checkBox_ssh = QtGui.QCheckBox(self.groupBox_serverlist)
        self.checkBox_ssh.setObjectName(_fromUtf8("checkBox_ssh"))
        self.verticalLayout_8.addWidget(self.checkBox_ssh)
        self.checkBox_ntpd = QtGui.QCheckBox(self.groupBox_serverlist)
        self.checkBox_ntpd.setObjectName(_fromUtf8("checkBox_ntpd"))
        self.verticalLayout_8.addWidget(self.checkBox_ntpd)
        self.checkBox_mail = QtGui.QCheckBox(self.groupBox_serverlist)
        self.checkBox_mail.setObjectName(_fromUtf8("checkBox_mail"))
        self.verticalLayout_8.addWidget(self.checkBox_mail)
        self.checkBox_firefox = QtGui.QCheckBox(self.groupBox_serverlist)
        self.checkBox_firefox.setObjectName(_fromUtf8("checkBox_firefox"))
        self.verticalLayout_8.addWidget(self.checkBox_firefox)
        # 添加其他服务
        # self.lineEdit_otherserver = QtGui.QLineEdit(self.groupBox_serverlist)
        # self.lineEdit_otherserver.setObjectName(_fromUtf8("lineEdit_otherserver"))
        # self.verticalLayout_8.addWidget(self.lineEdit_otherserver)

        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        self.verticalLayout_4.addWidget(self.groupBox_serverlist)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem6)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.startbtn = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        self.startbtn.setObjectName(_fromUtf8("startbtn"))
        self.horizontalLayout_6.addWidget(self.startbtn)
        self.stopbtn = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        self.stopbtn.setObjectName(_fromUtf8("stopbtn"))
        self.horizontalLayout_6.addWidget(self.stopbtn)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        self.verticalLayout_4.addItem(spacerItem8)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.textEdit_outputHomealone = QtGui.QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit_outputHomealone.setObjectName(_fromUtf8("textEdit_outputHomealone"))
        self.textEdit_outputHomealone.setReadOnly(True)
        self.horizontalLayout_4.addWidget(self.textEdit_outputHomealone)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.scrollArea_homealon.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_15.addWidget(self.scrollArea_homealon)

        # 事件注册
        # **************************************************************************************888*************************
        self.retranslateUi(CRDC)
        # 登录事件
        QtGui.QWidget.connect(self.Loginbtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.onActivatLogin)
        QtGui.QWidget.connect(self.Exitbtn_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.onActivatExit)
        # 创建读取虚拟机
        QtGui.QWidget.connect(self.CreateVMbtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.onActivatCreateVMbtn)
        QtGui.QWidget.connect(self.ReadVMinforbtn_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.onActivatReadVMbtn)
        QtGui.QWidget.connect(self.JCCJxialaicaidan, QtCore.SIGNAL(_fromUtf8('activated(int)')), self.onActivated)
        # 选择检测方法显示
        self.scrollArea_randomtest.show()
        self.scrollArea_homealon.hide()
        self.DestationDetectScrollArea.hide()

        # 随机检测
        # QtGui.QWidget.connect(self.OutputtextEdit,)
        QtGui.QWidget.connect(self.DetectDomainbtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.onDectDomainID)
        QtGui.QWidget.connect(self.Sortdomainbtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.onSortdomain)
        QtGui.QWidget.connect(self.StartRandomTestDectectionbtn, QtCore.SIGNAL(_fromUtf8('clicked()')),
                              self.onStartdetect)
        QtGui.QWidget.connect(self.configuerDectectionbtn, QtCore.SIGNAL(_fromUtf8('clicked()')),
                              self.onconfiguerdetect)
        QtGui.QWidget.connect(self.StopDetectbtn, QtCore.SIGNAL(_fromUtf8('clicked()')),
                              self.RandomtestStopdetect)
        #设置复选框点击确认按钮，如果是多列单独确认可以用。
        # self.TableWidget_randomtest_VMIP.itemClicked.connect(self.handleItemClicked)
        self.Sortdomainbtn.setEnabled(False)
        self.StartRandomTestDectectionbtn.setEnabled(False)
        self.StopDetectbtn.setEnabled(False)
        #self.DetectDomainbtn.setEnabled(False)
        # 平台独占性检测
        QtGui.QWidget.connect(self.comboBox_applyVMduzhanfuwu, QtCore.SIGNAL(_fromUtf8('activated(int)')),self.homeAloneIP)
        self.checkBox_ssh.stateChanged.connect(self.modifySSH)
        self.checkBox_ntpd.stateChanged.connect(self.modifyNtpd)
        self.checkBox_mail.stateChanged.connect(self.modifyMail)
        self.checkBox_firefox.stateChanged.connect(self.modifyFirefox)
        QtGui.QWidget.connect(self.startbtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.onActivatStartHA)
        QtGui.QWidget.connect(self.stopbtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.onActivatStopHA)
        QtCore.QMetaObject.connectSlotsByName(CRDC)

        # 目标同住检测
        self.output_refresh.connect(self.refresh_result)
        self.complete_signal.connect(self.change_complete_signal)
        QtGui.QWidget.connect(self.SelectAll, QtCore.SIGNAL(_fromUtf8('clicked()')), self.onActSelectAll)
        QtGui.QWidget.connect(self.Select, QtCore.SIGNAL(_fromUtf8('clicked()')), self.onActSelect)
        QtGui.QWidget.connect(self.DisSelect, QtCore.SIGNAL(_fromUtf8('clicked()')), self.onActDisSelect)
        QtGui.QWidget.connect(self.stopbtn_2, QtCore.SIGNAL(_fromUtf8('clicked()')), self.onActStopAll)
        self.VMTobeSelectedList.itemClicked.connect(self.handleItemClicked)
        QtGui.QWidget.connect(self.startbtn_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.onActivatDestinationDectect)

    # 登录虚拟机
    def onActivatLogin(self):
        loginForm = QtGui.QDialog()
        loginUi = Ui_Login()
        loginUi.setupUi(loginForm)
        loginForm.result = False
        loginForm.show()
        # if loginForm.result()== True:
        loginForm.exec_()
    def onActivatExit(self):
        sys.exit()
    # 读入虚拟机信息
    def onActivatReadVMbtn(self):
        global hostsdict
        filePath = QtGui.QFileDialog.getOpenFileName()
        # if filePath:
        #     global_list.var.set(filePath.name)
        # print filePath
        hostsdict.clear()
        # 读取文本内容
        fd = file(filePath, 'r')
        while True:
            line = fd.readline()
            if line:
                tmpList = line.split()
                ip = tmpList[0]
                hostsdict[ip] = defaultdict()
                hostsdict[ip]['host'] = tmpList[0]
                hostsdict[ip]['username'] = tmpList[1]
                hostsdict[ip]['private_key'] = tmpList[2]
                if len(tmpList) >= 4:
                    hostsdict[ip]['passwd']=tmpList[3]
                if len(tmpList) >= 5:
                    hostsdict[ip]['port']=tmpList[4]
                pass  # do something here
            else:
                break
        fd.close()
        # 随机同驻检测
        i = 0
        self.TableWidget_randomtest_VMIP.clearContents()
        self.VMTobeSelectedList.clearContents()
        for ip, info in hostsdict.iteritems():
            # 随机同驻检测
            self.TableWidget_randomtest_VMIP.setRowCount(i + 1)
            item = QtGui.QTableWidgetItem(str(hostsdict[ip]['host']))
            item.setCheckState(QtCore.Qt.Unchecked)
            self.TableWidget_randomtest_VMIP.setItem(i, 0, item)
            # 目标同驻检测
            self.VMTobeSelectedList.setRowCount(i + 1)
            item2 = QtGui.QTableWidgetItem(str(hostsdict[ip]['host']+":"+hostsdict[ip].get('port')))
            item2.setCheckState(QtCore.Qt.Unchecked)
            self.VMTobeSelectedList.setItem(i, 0, item2)
            i = i + 1
            # item = QtGui.QTableWidgetItem(str(self.Randomtest_hosts[i].private_key))
            # print self.Randomtest_hosts[i].private_key
            # self.TableWidget_randomtest_VMIP.setItem(i,1,item)
            # homeAlone
            self.comboBox_applyVMduzhanfuwu.clear()
            for ip, info in hostsdict.iteritems():
                self.comboBox_applyVMduzhanfuwu.addItem(str(hostsdict[ip]['host']))
    # 创建虚拟机
    def onActivatCreateVMbtn(self):
        createForm = QtGui.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(createForm)
        createForm.show()
        createForm.exec_()
    # 检测方式切换
    def onActivated(self, cuindex):
        if cuindex == 0:
            self.scrollArea_randomtest.show()
            self.scrollArea_homealon.hide()
            self.DestationDetectScrollArea.hide()
        # HomeAlone
        if cuindex == 1:
            self.scrollArea_randomtest.hide()
            self.scrollArea_homealon.show()
            self.DestationDetectScrollArea.hide()
            # 获取虚拟机IP
            # connEC2_homeAlone = ConnEC2()
            # resultconnt = connEC2_homeAlone.connect(global_list.login_ip, global_list.login_secret_access_key)
            # global hostsIPhomeAlone
            # hostsIPhomeAlone = []
            # if resultconnt == True:
            #     instdict = connEC2_homeAlone.getInstance()
            #     for ip, info in instdict.iteritems():
            #         self.comboBox_applyVMduzhanfuwu.addItem(str(ip))
            #         hostsIPhomeAlone.append(str(ip))
            # else:
            #     pass

        if cuindex == 2:
            self.scrollArea_randomtest.hide()
            self.scrollArea_homealon.hide()
            self.DestationDetectScrollArea.show()

    # ********************************************************************************************************************
    # 随机同驻检测
    def onconfiguerdetect(self):
        randomtest = Randomtest()
        self.OutputtextEdit.clear()
        QtGui.QMessageBox.warning(self, "Warning", u"正在配置，请等待一分钟!")
        checkempty=0
        for i in range(self.TableWidget_randomtest_VMIP.rowCount()):
            item = self.TableWidget_randomtest_VMIP.item(i, 0)
            if item.checkState() == QtCore.Qt.Checked:
                ip = str(item.text())
                username = hostsdict[ip]['username']
                private_key = hostsdict[ip]['private_key']
                configvmthread = MyTread(randomtest.config, (ip, username, private_key), u'配置randomtest实验环境')
                self.OutputtextEdit.append(u"开始配置虚拟机：" + ip)
                configvmthread.start()
                checkempty=checkempty+1
        if checkempty==0:
            QtGui.QMessageBox.warning(self,"Warning", u"请选择需要配置的VM!")
            # configresult=configvmthread.getResult()
    def onDectDomainID(self):
        global hostsdict
        threadlist=[]
        randomtest = Randomtest()
        for i in range(self.TableWidget_randomtest_VMIP.rowCount()):
            item = self.TableWidget_randomtest_VMIP.item(i, 0)
            ip=str(item.text())
            username = hostsdict[ip]['username']
            private_key = hostsdict[ip]['private_key']
            DomaindIDthread = MyTread(randomtest.detectDomainID,(hostsdict,ip, username, private_key,i), u'detect domainID')
            threadlist.append(DomaindIDthread)
            DomaindIDthread.start()
        QtGui.QMessageBox.information(self, "Warning", u"请等待所有domainID检测结束！")
        # for j in range(len(threadlist)):
        #     str(threadlist[j].getResult())
        # 打印domainID
        # i = 0
        # for ip, info in hostsdict.iteritems():
        #     self.TableWidget_randomtest_VMIP.setRowCount(i + 1)
        #     item = QtGui.QTableWidgetItem(str(hostsdict[ip]['host']))
        #     item.setCheckState(QtCore.Qt.Unchecked)
        #     self.TableWidget_randomtest_VMIP.setItem(i, 0, item)
        #     newitem = QtGui.QTableWidgetItem(str(hostsdict[ip]['domainID']))
        #     self.TableWidget_randomtest_VMIP.setItem(i, 1, newitem)
        #     i = i + 1
        self.Sortdomainbtn.setEnabled(True)
        # self.StartRandomTestDectectionbtn.setEnabled(True)
        # self.StopDetectbtn.setEnabled(True)
    def onSortdomain(self):
        signalDomainID=True
        # self.TableWidget_randomtest_VMIP.clearContents()
        HostList = []
        for ip,info in hostsdict.iteritems():
            if('domainID'in info):
                tmpHost = (ip, int(info['domainID']))
                HostList.append(tmpHost)
            else:
                signalDomainID=False
                QtGui.QMessageBox.information(self, "Warning", u"请等待所有domainID检测结束！")
                break
        if(signalDomainID):
            HostList.sort(lambda x, y: cmp(x[1], y[1]))
            i = 0
            for i in range(len(HostList)):
                self.TableWidget_randomtest_VMIP.setRowCount(i + 1)
                item = QtGui.QTableWidgetItem(str(HostList[i][0]))
                item.setCheckState(QtCore.Qt.Unchecked)
                self.TableWidget_randomtest_VMIP.setItem(i, 0, item)
                newitem = QtGui.QTableWidgetItem(str(HostList[i][1]))
                self.TableWidget_randomtest_VMIP.setItem(i, 1, newitem)
                i = i + 1
                self.StartRandomTestDectectionbtn.setEnabled(True)
                self.StopDetectbtn.setEnabled(True)
        else:
            self.StartRandomTestDectectionbtn.setEnabled(False)
            self.StopDetectbtn.setEnabled(False)
    def handleItemClicked(self, item):
        if item.checkState() == QtCore.Qt.Unchecked:
            item.setCheckState(QtCore.Qt.Checked)
        else:
            item.setCheckState(QtCore.Qt.Unchecked)
    def onStartdetect(self):
        self.OutputtextEdit.setText("")
        global_list.RandomtestselectedIndex = []
        self.OutputtextEdit.append(u"待检测虚拟机：")
        for i in range(self.TableWidget_randomtest_VMIP.rowCount()):
            item = self.TableWidget_randomtest_VMIP.item(i, 0)
            if item.checkState() == QtCore.Qt.Checked:
                global_list.RandomtestselectedIndex.append(item.text())
                self.OutputtextEdit.append(item.text())
        if len(global_list.RandomtestselectedIndex) < 2:
            QtGui.QMessageBox.warning(self, "Warning", u"请至少选择两台虚拟机!")
        else:
           i=0
           selectnum = len(global_list.RandomtestselectedIndex)
           while(i<(selectnum-1)):
               randomtest = Randomtest()
               host1=str(global_list.RandomtestselectedIndex[i])
               host1domaid=int(hostsdict[host1]['domainID'])
               #option1
               j = i + 1
               while(j<selectnum):
                   host2 = str(global_list.RandomtestselectedIndex[j])
                   host2domaid = int(hostsdict[host2]['domainID'])
                   if (host2domaid==host1domaid):
                       self.OutputtextEdit.append(host1 + "and" + host2 + u"虚拟机不同驻")
                   elif((abs(host2domaid-host1domaid))>=16):
                       self.OutputtextEdit.append(host1 + "and" + host2 + u"虚拟机不同驻")
                   else:
                       tempindex = []
                       tempindex.append(host1)
                       tempindex.append(host2)
                       print host1 + "and" + host2 + u"start detect"
                       dectresult = MyTread(randomtest.detect, (tempindex, hostsdict), u"detect colocation")
                       dectresult.start()
                       time.sleep(1.5)
                   j=j+1
               i=i+1
               #option2
               '''
               j=i+1
               host2=str(global_list.RandomtestselectedIndex[j])
               host2domaid=int(hostsdict[host2]['domainID'])
               if (host2domaid==host1domaid):
                   self.OutputtextEdit.append(host1+"and"+ host2+u"虚拟机不同驻")
               elif((host2domaid-host1domaid)<16):
                   # print host1+" tap1 "
                   # print "j"+str(j)
                   # print "selectnum"+str(selectnum)
                   while(((host2domaid-host1domaid)<16)and(j<selectnum)):
                       tempindex = []
                       tempindex.append(host1)
                       tempindex.append(host2)
                       print host1+"and"+host2+u"start detect"
                       dectresult = MyTread(randomtest.detect, (tempindex, hostsdict), u"detect colocation")
                       dectresult.start()
                       time.sleep(1.5)
                       j=j+1
                       if(j<selectnum):
                           host2=str(global_list.RandomtestselectedIndex[j])
                           host2domaid=int(hostsdict[host2]['domainID'])
               else:
                   self.OutputtextEdit.append(host1+"and"+host2+u"虚拟机不同驻")
               i=i+1
               '''
    def RandomtestStopdetect(self):
        self.OutputtextEdit.append(u"检测停止")
        i = 0
        while (i < (len(global_list.RandomtestselectedIndex)-1)):
            randomtest = Randomtest()
            # tempindex = []
            # tempindex.append(global_list.RandomtestselectedIndex[i])
            # j = i + 1
            # tempindex.append(global_list.RandomtestselectedIndex[j])
            # host, username, private_key
            # dectresult = randomtest.detect(tempindex, hostsdict)
            host = str(global_list.RandomtestselectedIndex[i])
            private_key = hostsdict[host]['private_key']
            username = hostsdict[host]['username']
            dectstop = MyTread(randomtest.stop, (host, username, private_key), u'停止检测')
            # global_list.detectthread.append(dectresult)
            dectstop.start()
            i = i + 1
            #sys.exit()
        # lenthread=range(len(global_list.RandomtestselectedIndex)-1)
        # for i in lenthread:
        #     global_list.detectthread[i].__exit__
        # for i in range(self.TableWidget_randomtest_VMIP.rowCount()):
        #     item = self.TableWidget_randomtest_VMIP.item(i, 0)
        #     if item.checkState() == QtCore.Qt.Checked:
        #         # print item.text()
        #         self.OutputtextEdit.append(item.text())

    ##***********************************************************************************************************
    # HomeAlonedect
    def homeAloneIP(self, cuindex):
        self.homeAloneIP = self.comboBox_applyVMduzhanfuwu.itemText(cuindex)
    def modifySSH(self, state):
        if state == QtCore.Qt.Checked:
            self.serviceList.append('ssh')
            print self.serviceList
        else:
            self.serviceList.remove('ssh')
            print self.serviceList
    def modifyNtpd(self, state):
        if state == QtCore.Qt.Checked:
            self.serviceList.append('ntpd')
            print self.serviceList
        else:
            self.serviceList.remove('ntpd')
            print self.serviceList
    def modifyMail(self, state):
        if state == QtCore.Qt.Checked:
            self.serviceList.append('mail')
            print self.serviceList
        else:
            self.serviceList.remove('mail')
            print self.serviceList
    def modifyFirefox(self, state):
        if state == QtCore.Qt.Checked:
            self.serviceList.append('firefox')
            print self.serviceList
        else:
            self.serviceList.remove('firefox')
            print self.serviceList
    def onActivatStartHA(self):
        host = str(self.homeAloneIP)
        print 'yuan', host
        print hostsdict
        private_key = hostsdict[host]['passwd']
        print 'yuan', private_key
        username = hostsdict[str(host)]['username']
        vmport=int(hostsdict[str(host)]['port'])
        # scList = 'firefox'
        scList = self.serviceList
        if len(scList) == 0:
            QtGui.QMessageBox.warning(self, "Warning", u"请至少选择1个服务!")
        else:
            self.textEdit_outputHomealone.clear()
            self.textEdit_outputHomealone.append(u'您选择 ' + str(scList) + u'服务进行检测.')

            self.ha = HomeAloneDetect(host, username, private_key, scList, vmport)
            #print 'ok2'
            # outContext = ha.detect1(host, username, private_key, scList)
            self.ha.startDetect()
            # return ha
    def onActivatStopHA(self):
        host = str(self.homeAloneIP)
        private_key = hostsdict[host]['passwd']
        print 'yuan', private_key
        username = hostsdict[host]['username']
        vmport=hostsdict[host]['port']
        # scList = 'firefox'
        outContext = self.ha.stop(host, username, private_key, vmport)

        if outContext is not None:
            self.textEdit_outputHomealone.append(u'检测正常终止。')
        else:
            self.textEdit_outputHomealone.append(u'检测出现异常！')

    ##************************************************************************************
    # 目标同驻检测
    def fill_tobe_detected(self, vm_dict):
        i = 0
        for ip in vm_dict.iteritems():
            self.VMTobeSelectedList.setRowCount(i + 1)
            item = QtGui.QTableWidgetItem(str(hostsdict[ip]['host']))
            item.setCheckState(QtCore.Qt.Unchecked)
            self.VMTobeSelectedList.setItem(i, 0, item)
    def onActStopAll(self):
        if self.complete == 1:
            self.warning(u"没有进行中的检测!")
        else:
            self.question(u"确定要停止检测?")
            self.change_complete_signal()
            self.desProcessor.stopAll()
    def handleItemClicked(self, item):
        if item.checkState() == QtCore.Qt.Unchecked:
            item.setCheckState(QtCore.Qt.Checked)
        else:
            item.setCheckState(QtCore.Qt.Unchecked)
    def onActSelectAll(self):
        for i in range(self.VMTobeSelectedList.rowCount()):
            item = self.VMTobeSelectedList.item(i, 0)
            item.setCheckState(QtCore.Qt.Checked)
        self.onActSelect()
    def onActDisSelect(self):
        for i in range(self.VMTobeSelectedList.rowCount()):
            item = self.VMTobeSelectedList.item(i, 0)
            item.setCheckState(QtCore.Qt.Unchecked)
        self.onActSelect()
    def onActSelect(self):
        self.VMSelectedList.setText("")
        self.selectedIndex = []
        for i in range(self.VMTobeSelectedList.rowCount()):
            item = self.VMTobeSelectedList.item(i, 0)
            if item.checkState() == QtCore.Qt.Checked:
                self.selectedIndex.append(str(item.text()))
                self.VMSelectedList.append(item.text())
    def change_complete_signal(self):
        self.complete = 1
    def onActivatDestinationDectect(self):
        if self.complete == 0:
            self.warning(u"请先停止当前检测!")
        elif not len(self.selectedIndex):
            self.warning(u"请先选择待检测虚拟机!")
        else:
            selected_hosts = []
            self.complete = 0
            self.Ouput.setText("")
            for index in self.selectedIndex:
                # import pdb;pdb.set_trace()
                index = index[:index.find(":")]
                hostinfo = HostInfo(host=index, username=hostsdict.get(str(index)).get('username'), port=int(hostsdict.get(str(index)).get('port')),
                                    private_key=hostsdict.get(str(index)).get('private_key'), passwd=hostsdict.get(str(index)).get('passwd'))
                selected_hosts.append(hostinfo)
            print self.selectedIndex
            desComputerIP = str(self.DesinationComputerIP.text())
            desSocket = int(self.SoceketText.text())
            self.desProcessor = DesProcessor(selected_hosts, desComputerIP, desSocket,
                                             output_signal=self.output_refresh, complete_signal=self.complete_signal)
            thread.start_new_thread(self.desProcessor.detectAll, ())
    def refresh_result(self, info):
        self.Ouput.append(info)
        cursor = self.Ouput.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        self.Ouput.setTextCursor(cursor)
    def warning(self, info):
        QtGui.QMessageBox.warning(self, "Pyqt", info)  # 弹出警告框
    def question(self, info):
        QtGui.QMessageBox.question(self, "Pyqt", info, QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)  # 弹出询问框

    ##************************************************************************
    def retranslateUi(self, CRDC):
        # 主界面
        CRDC.setWindowTitle(_translate("CRDC", "云平台同驻检测工具", None))
        self.usernamelable.setText(_translate("CRDC", "用户名", None))
        self.Loginbtn.setText(_translate("CRDC", "登录", None))
        self.Exitbtn_2.setText(_translate("CRDC", "退出", None))
        self.JianceChangjing.setTitle(_translate("CRDC", "检测场景", None))
        self.JCCJxialaicaidan.setItemText(0, _translate("CRDC", "随机同驻检测", None))
        self.JCCJxialaicaidan.setItemText(1, _translate("CRDC", "平台独占性检测", None))
        self.JCCJxialaicaidan.setItemText(2, _translate("CRDC", "目标同驻检测", None))
        self.CreateVMbtn.setText(_translate("CRDC", "创建虚拟机", None))
        self.ReadVMinforbtn_2.setText(_translate("CRDC", "读入虚拟机信息", None))

        # 随机同驻检测
        self.TobeDetectedComputerName.setText(_translate("CRDC", "待检测虚拟机列表", None))
        item = self.TableWidget_randomtest_VMIP.horizontalHeaderItem(0)
        item.setText(_translate("CRDC", "虚拟机IP", None))
        item = self.TableWidget_randomtest_VMIP.horizontalHeaderItem(1)
        item.setText(_translate("CRDC", "Domain ID", None))
        self.DetectDomainbtn.setText(_translate("CRDC", "检测DomainID", None))
        self.Sortdomainbtn.setText(_translate("CRDC", "按DomainID排序", None))
        self.configuerDectectionbtn.setText(_translate("CRDC", "配置虚拟机", None))
        self.StartRandomTestDectectionbtn.setText(_translate("CRDC", "开始检测", None))
        self.StopDetectbtn.setText(_translate("CRDC", "停止检测", None))

        # 目标同驻检测
        self.DestinationComputerName.setText(_translate("CRDC", "目标虚拟机IP：", None))
        self.DesinationComputerIP.setText(_translate("CRDC", "218.241.135.34", None))
        self.socketName.setText(_translate("CRDC", "端口号: ", None))
        self.SoceketText.setText(_translate("CRDC", "4356", None))
        # self.CommunicationSpeedName.setText(_translate("CRDC", "通讯速率(kb/s):", None))
        self.TobeDetectedComputerName_2.setText(_translate("CRDC", "待检测虚拟机列表", None))
        # item = self.VMTobeSelectedList.verticalHeaderItem(0)
        # item.setText(_translate("CRDC", "序号", None))
        # item = self.VMTobeSelectedList.horizontalHeaderItem(0)
        # item.setText(_translate("CRDC", "虚拟机IP", None))
        # __sortingEnabled = self.VMTobeSelectedList.isSortingEnabled()
        # self.VMTobeSelectedList.setSortingEnabled(False)
        # self.VMTobeSelectedList.setSortingEnabled(__sortingEnabled)
        self.SelectAll.setText(_translate("CRDC", "全选", None))
        self.Select.setText(_translate("CRDC", "选择", None))
        self.DisSelect.setText(_translate("CRDC", "清空", None))
        self.FlooderName.setText(_translate("CRDC", " ", None))
        self.startbtn_2.setText(_translate("CRDC", " 开始检测 ", None))
        self.stopbtn_2.setText(_translate("CRDC", "停止检测", None))

        # 平台独占性检测
        self.groupBox_shenqingduzhanfuwu.setTitle(_translate("CRDC", "已申请独占服务的虚拟机", None))
        self.groupBox_serverlist.setTitle(_translate("CRDC", "服务列表", None))
        # self.comboBox_applyVMduzhanfuwu.setItemText(0, _translate("CRDC", "192.168.1.1", None))
        # self.comboBox_applyVMduzhanfuwu.setItemText(1, _translate("CRDC", "192.168.16.5", None))
        self.checkBox_ssh.setText(_translate("CRDC", "ssh", None))
        self.checkBox_ntpd.setText(_translate("CRDC", "ntpd", None))
        self.checkBox_mail.setText(_translate("CRDC", "mail", None))
        self.checkBox_firefox.setText(_translate("CRDC", "firefox", None))
        self.startbtn.setText(_translate("CRDC", "开始", None))
        self.stopbtn.setText(_translate("CRDC", "停止", None))
