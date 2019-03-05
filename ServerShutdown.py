# -*- coding: cp1252 -*-
################################################################################
# Description:
# This program is used to send notification when the server goes down.
# It will ping server to check if server is up and running.
# If server doesn’t respond to ping request then application will send sms
# to mobile number mentioned in program. 
# IP address of server whose status have to be known, mobile number and
# password of way2sms user account have to be entered in user interface.
# If battery status is less than 20% and server is online sms will be sent.
# If battery status is less than 20% and server is offline sms will be sent.     
#
################################################################################
# $TI Release: F2833x/F2823x Header Files and Peripheral Examples V142 $
# $Release Date: March  4, 2019 $
# $Copyright: Copyright (C) 2018-2019 Sushmitha K -
#             http://www.ti.com/ ALL RIGHTS RESERVED $
################################################################################
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serverShutdown.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(614, 346)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        Form.setFont(font)
        self.line_5 = QtGui.QFrame(Form)
        self.line_5.setGeometry(QtCore.QRect(10, 415, 641, 31))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 20, 521, 301))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.line_4 = QtGui.QFrame(self.layoutWidget)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout_2.addWidget(self.line_4)
        self.label = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("background-color: rgb(118, 118, 118);"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.line = QtGui.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.plainTextEdit = QtGui.QPlainTextEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setMinimumSize(QtCore.QSize(362, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.horizontalLayout.addWidget(self.plainTextEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.plainTextEdit_2 = QtGui.QPlainTextEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_2.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_2.setSizePolicy(sizePolicy)
        self.plainTextEdit_2.setMinimumSize(QtCore.QSize(362, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setObjectName(_fromUtf8("plainTextEdit_2"))
        self.horizontalLayout_2.addWidget(self.plainTextEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.plainTextEdit_3 = QtGui.QPlainTextEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_3.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_3.setSizePolicy(sizePolicy)
        self.plainTextEdit_3.setMinimumSize(QtCore.QSize(362, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit_3.setFont(font)
        self.plainTextEdit_3.setObjectName(_fromUtf8("plainTextEdit_3"))
        self.horizontalLayout_3.addWidget(self.plainTextEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.line_3 = QtGui.QFrame(self.layoutWidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_2.addWidget(self.line_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.pushButton = QtGui.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.line_6 = QtGui.QFrame(self.layoutWidget)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.verticalLayout_2.addWidget(self.line_6)
        self.layoutWidget.raise_()
        self.line_5.raise_()

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.readValue)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.plainTextEdit.copy)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), sys.exit)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.plainTextEdit_2.update)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.plainTextEdit_3.update)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "SERVER SHUTDOWN", None))
        self.label_2.setText(_translate("Form", "Server Address ", None))
        self.label_3.setText(_translate("Form", "Mobile Number ", None))
        self.label_4.setText(_translate("Form", "Password           ", None))
        self.pushButton.setText(_translate("Form", "OK", None))
        self.pushButton_2.setText(_translate("Form", "Exit", None))

#Function to read values from user interface.
    def readValue(self):
        self.label.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
        #x = self.ping("www.google.com")
        ipAddr = self.plainTextEdit.toPlainText()
        ipAddr = str(ipAddr)
        print ipAddr

        mobileNo = self.plainTextEdit_2.toPlainText()
        mobileNo = str(mobileNo)
        print mobileNo
        
        password = self.plainTextEdit_3.toPlainText()
        password = str(password)
        print password

       # if x == 0:
       #     self.label.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
       #     self.callmethods(ipAddr, mobileNo, password)
       # else:
       #     self.label.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
            

#Function to check battery status of system in which program will be running. 
    def battery_status(self):
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percent = str(battery.percent)

        if plugged==False: plugged="Not Plugged In"
        else: plugged="Plugged In"
        print(percent+'% | '+plugged)

        percent = int(percent)
        return [percent, plugged]

#Function to send ping request to server whose status have to be known.
    def ping(self, host):
        r = pyping.ping(host)

        if r.ret_code == 0:
            a = r.ret_code
            print("Success")
        else:
            a = r.ret_code
            print("Failed with {}".format(r.ret_code))
        return a

#Function to send sms to mobile number mentioned in program.
    def sendmsg(self, mobileNo, password, percent):
        base_url = "http://www.way2sms.com/"
        login_url = base_url + "send-sms"
        driver = webdriver.PhantomJS()
        driver.set_window_size(1120, 550)
        
        driver.get(base_url)
        inputElement = driver.find_element_by_id("mobileNo")
        inputElement.send_keys(mobileNo)
        driver.save_screenshot('screenshot.png')
        inputElement = driver.find_element_by_id("password")
        inputElement.send_keys(password)
        python_button = driver.find_elements_by_xpath("//button[@class='btn-theme-sm btn-ls text-uppercase']")[0]
        python_button.click()
    
        mobileNo2 = 'xxxxxxxxxx' #mobile number to which sms have to be sent.
        driver.get(login_url)
        driver.save_screenshot('screenshot5.png')
        driver.save_screenshot('screenshot2.png')
    
    
        inputElement = driver.find_element_by_id("mobile")
        inputElement.send_keys(mobileNo2)

        inputElement = driver.find_element_by_id("message")
        inputElement.send_keys(percent)

        python_button = driver.find_elements_by_xpath("//button[@class='btn-theme-sm btn-ls text-uppercase']")[0]
        python_button.click()

        print "message sent"
       
        
    def callmethods(self, ipaddr, mobileNo, password):
        x = self.battery_status()
        percent = x[0]
        plugged = x[1]
        a = self.ping(ipaddr)
        if percent < 20 and plugged == "Plugged In" and a == 0:
            self.sendmsg(mobileNo, password,"Srv:Online Sys:powerdown")
        elif percent < 20 and plugged == "Plugged In" and a == 1:
            self.sendmsg(mobileNo, password,"Srv:Offline")
        
if __name__ == "__main__":
    import sys
    import time
    import psutil
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import pyping
#    from selenium.webdriver.support.ui import WebDriverWait
#    from selenium.common.exceptions import TimeoutException
    from selenium import webdriver
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By

    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    app.processEvents()
    Form.show()
    sys.exit(app.exec_())






