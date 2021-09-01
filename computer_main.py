import sys
from computer_ui import Ui_MainWindow
from PyQt5 import QtWidgets

class Digcalculator(QtWidgets.QMainWindow, Ui_MainWindow):
    lcdstring = ''
    operation = ''
    currentNum = 0 
    previousNum = 0
    result = 0
    def __init__(self, parent=None):
        super(Digcalculator, self).__init__()
        self.setupUi(self)
        self.action() #存放所有的信号槽
    def action(self): #定义按下数字执行的方法
        self.button_0.clicked.connect(self.buttonClicked)
        self.button_1.clicked.connect(self.buttonClicked)
        self.button_2.clicked.connect(self.buttonClicked)
        self.button_3.clicked.connect(self.buttonClicked)
        self.button_4.clicked.connect(self.buttonClicked)
        self.button_5.clicked.connect(self.buttonClicked)
        self.button_6.clicked.connect(self.buttonClicked)
        self.button_7.clicked.connect(self.buttonClicked)
        self.button_8.clicked.connect(self.buttonClicked)
        self.button_9.clicked.connect(self.buttonClicked)
        self.button_clear.clicked.connect(self.clearClicked)
        self.button_equal.clicked.connect(self.equalClicked)
    def buttonClicked(self):
        if len(self.lcdstring) <= 27: #长度小于27执行 
            self.lcdstring = self.lcdstring + self.sender().text() #旧LCD显示内容+按纽传过来的对象的text值
            if str(self.lcdstring) == '.':
                self.lcdstring = '0.'
                self.lcd.display(self.lcdstring)
                self.currentNum = float(self.lcdstring)
            else:
                if str(self.lcdstring).count('.') > 1:
                    self.lcdstring = str(self.lcdstring)[:-1]
                    self.lcd.display(self.lcdstring)
                    self.currentNum = float(self.lcdstring)
                else:
                    self.lcd.display(self.lcdstring)
                    self.currentNum = float(self.lcdstring)
        else: #LCD长度大于9
            pass
    def opClicked(self):
        if self.operation != '':
            self.equalClicked()
            self.previousNum = self.currentNum
            self.currentNum = 0
            self.lcdstring = ''
            self.operation = self.sender().text()
        else:
            self.previousNum = self.currentNum
            self.currentNum = 0
            self.lcdstring = ''
            self.operation = self.sender().text()
    def clearClicked(self):
        self.lcdstring = ''
        self.operation = ''
        self.currentNum = 0
        self.previousNum = 0
        self.result = 0
        self.lcd.display(0)
    def equalClicked(self):
        self.currentNum = self.result
        self.lcdstring = ''
        self.operation = ''
    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, u'警告', u'確認退出?', 
            QtWidgets.QMessageBox.Yes,QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Digcalculator()
    window.show()
    sys.exit(app.exec_())