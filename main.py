# -*- coding: utf-8 -*-
"""

"""
from PyQt5 import QtCore, QtGui, uic, QtWidgets
import sys



class MainScreen(QtWidgets.QMainWindow):
    def __init__(self):
        '''
        This is the main screen that the user interacts with.

        '''

        super(self.__class__, self).__init__()
        uic.loadUi('gui.ui', self)

        self.new_user.clicked.connect(self.new_user_clicked)
        self.old_user.clicked.connect(self.old_user_clicked)
        self.clear_all.clicked.connect(self.clear_all_clicked)
        self.scan.clicked.connect(self.scan_clicked)


        # timer = QtCore.QTimer(self)
        # timer.timeout.connect(self.updateFromGlobal)
        # timer.start(100)

    def new_user_clicked(self):
        print("new user")
        self.status_info.setText("مستخدم جديد: ")
        textboxvalue = self.username_entry.text()
        self.status_info.setText(self.status_info.text() + " " + textboxvalue + " ")
        self.username_entry.clear()

    def old_user_clicked(self):
        print("older user")
        self.status_info.setText("مستخدم قديم")
    def clear_all_clicked(self):
        print("clear all")
        self.status_info.setText("تم مسح جميع البيانات")
    def scan_clicked(self):
        print("scan")
        self.status_info.setText(self.status_info.text() + "\n" + "جاري تشغيل البصمة ")


app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
screen = MainScreen()  # We set the form to be our ExampleApp (design)
screen.show()  # Show the form
sys.exit(app.exec_())  # and execute the app
