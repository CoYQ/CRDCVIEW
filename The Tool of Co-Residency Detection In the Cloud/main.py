#-*- coding: utf-8 -*-

from PyQt4 import QtGui
from Login import *
from CRDC import *
import global_list

class MainWindow(QtGui.QDialog):
    def __init__(self,parent=None):

        QtGui.QWidget.__init__(self,parent)
        # self.ui_login=Ui_Login()
        # Ui_Dialog为.ui产生.py文件中窗体类名，经测试类名以Ui_为前缀，加上UI窗体对象名（此处为Dialog，见上图）
        global_list.ui_CRDC=Ui_CRDC()
        global_list.ui_CRDC.setupUi(self)
        # self.ui_login.setupUi(self)

if __name__ == "__main__":

    import sys
    #显示界面
    app = QtGui.QApplication(sys.argv)
    myapp=MainWindow()
    myapp.show()
    app.exec_()