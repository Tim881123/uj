# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'computer.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1101, 928)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(200, 250, 671, 681))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_1 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.button_1.setFont(font)
        self.button_1.setObjectName("button_1")
        self.horizontalLayout.addWidget(self.button_1)
        self.button_2 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.button_2.setFont(font)
        self.button_2.setObjectName("button_2")
        self.horizontalLayout.addWidget(self.button_2)
        self.button_3 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.button_3.setFont(font)
        self.button_3.setObjectName("button_3")
        self.horizontalLayout.addWidget(self.button_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_4 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.button_4.setFont(font)
        self.button_4.setObjectName("button_4")
        self.horizontalLayout_2.addWidget(self.button_4)
        self.button_5 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.button_5.setFont(font)
        self.button_5.setObjectName("button_5")
        self.horizontalLayout_2.addWidget(self.button_5)
        self.button_6 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.button_6.setFont(font)
        self.button_6.setObjectName("button_6")
        self.horizontalLayout_2.addWidget(self.button_6)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_7 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.button_7.setFont(font)
        self.button_7.setObjectName("button_7")
        self.horizontalLayout_3.addWidget(self.button_7)
        self.button_8 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.button_8.setFont(font)
        self.button_8.setObjectName("button_8")
        self.horizontalLayout_3.addWidget(self.button_8)
        self.button_9 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.button_9.setFont(font)
        self.button_9.setObjectName("button_9")
        self.horizontalLayout_3.addWidget(self.button_9)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.button_clear = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.button_clear.setFont(font)
        self.button_clear.setObjectName("button_clear")
        self.horizontalLayout_4.addWidget(self.button_clear)
        self.button_0 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.button_0.setFont(font)
        self.button_0.setObjectName("button_0")
        self.horizontalLayout_4.addWidget(self.button_0)
        self.button_equal = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.button_equal.setFont(font)
        self.button_equal.setObjectName("button_equal")
        self.horizontalLayout_4.addWidget(self.button_equal)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd.setGeometry(QtCore.QRect(200, 80, 671, 163))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.lcd.setFont(font)
        self.lcd.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcd.setDigitCount(10)
        self.lcd.setObjectName("lcd")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 10, 311, 71))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1101, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "计算机"))
        self.button_1.setText(_translate("MainWindow", "1"))
        self.button_2.setText(_translate("MainWindow", "2"))
        self.button_3.setText(_translate("MainWindow", "3"))
        self.button_4.setText(_translate("MainWindow", "4"))
        self.button_5.setText(_translate("MainWindow", "5"))
        self.button_6.setText(_translate("MainWindow", "6"))
        self.button_7.setText(_translate("MainWindow", "7"))
        self.button_8.setText(_translate("MainWindow", "8"))
        self.button_9.setText(_translate("MainWindow", "9"))
        self.button_clear.setText(_translate("MainWindow", "清除"))
        self.button_0.setText(_translate("MainWindow", "0"))
        self.button_equal.setText(_translate("MainWindow", "確認"))
        self.label.setText(_translate("MainWindow", "請輸入房號"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
