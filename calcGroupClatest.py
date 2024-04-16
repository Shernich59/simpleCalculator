# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calcGroupClatest.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.NO1 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("1"))
        self.NO1.setGeometry(QtCore.QRect(190, 170, 61, 41))
        self.NO1.setObjectName("NO1")
        self.NO2 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("2"))
        self.NO2.setGeometry(QtCore.QRect(270, 170, 61, 41))
        self.NO2.setObjectName("NO2")
        self.NO3 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("3"))
        self.NO3.setGeometry(QtCore.QRect(350, 170, 61, 41))
        self.NO3.setObjectName("NO3")
        self.Add = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("+"))
        self.Add.setGeometry(QtCore.QRect(430, 170, 61, 41))
        self.Add.setObjectName("Add")
        self.NO4 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("4"))
        self.NO4.setGeometry(QtCore.QRect(190, 230, 61, 41))
        self.NO4.setObjectName("NO4")
        self.NO6 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("6"))
        self.NO6.setGeometry(QtCore.QRect(350, 230, 61, 41))
        self.NO6.setObjectName("NO6")
        self.NO5 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("5"))
        self.NO5.setGeometry(QtCore.QRect(270, 230, 61, 41))
        self.NO5.setObjectName("NO5")
        self.Subtract = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("-"))
        self.Subtract.setGeometry(QtCore.QRect(430, 230, 61, 41))
        self.Subtract.setObjectName("Subtract")
        self.NO7 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("7"))
        self.NO7.setGeometry(QtCore.QRect(190, 290, 61, 41))
        self.NO7.setObjectName("NO7")
        self.NO8 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("8"))
        self.NO8.setGeometry(QtCore.QRect(270, 290, 61, 41))
        self.NO8.setObjectName("NO8")
        self.NO9 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("9"))
        self.NO9.setGeometry(QtCore.QRect(350, 290, 61, 41))
        self.NO9.setObjectName("NO9")
        self.Multiply = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("*"))
        self.Multiply.setGeometry(QtCore.QRect(430, 290, 61, 41))
        self.Multiply.setObjectName("Multiply")
        self.Divide = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("/"))
        self.Divide.setGeometry(QtCore.QRect(430, 350, 61, 41))
        self.Divide.setObjectName("Divide")
        self.Clear = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("C"))
        self.Clear.setGeometry(QtCore.QRect(110, 350, 61, 41))
        self.Clear.setObjectName("Clear")
        self.NO0 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("0"))
        self.NO0.setGeometry(QtCore.QRect(190, 350, 61, 41))
        self.NO0.setObjectName("NO0")
        self.GROUPC = QtWidgets.QLabel(self.centralwidget)
        self.GROUPC.setGeometry(QtCore.QRect(170, 30, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(28)
        self.GROUPC.setFont(font)
        self.GROUPC.setObjectName("GROUPC")
        self.OutputLable = QtWidgets.QLabel(self.centralwidget)
        self.OutputLable.setGeometry(QtCore.QRect(190, 70, 291, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.OutputLable.setFont(font)
        self.OutputLable.setFrameShape(QtWidgets.QFrame.Box)
        self.OutputLable.setObjectName("OutputLable")
        self.Negativepostive = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.plus_minus_it())
        self.Negativepostive.setGeometry(QtCore.QRect(110, 290, 61, 41))
        self.Negativepostive.setObjectName("Negativepostive")
        self.Subtract_2 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.remove_it())
        self.Subtract_2.setGeometry(QtCore.QRect(110, 230, 61, 41))
        self.Subtract_2.setObjectName("Subtract_2")
        self.Percentage = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("%"))
        self.Percentage.setGeometry(QtCore.QRect(110, 170, 61, 41))
        self.Percentage.setObjectName("Percentage")
        self.NO0_2 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.math_it())
        self.NO0_2.setGeometry(QtCore.QRect(290, 350, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.NO0_2.setFont(font)
        self.NO0_2.setObjectName("NO0_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def plus_minus_it(self):
        screen = self.OutputLable.text()
        if "-" in screen:
            self.OutputLable.setText(screen.replace("-", ""))
        else:
            self.OutputLable.setText(f'-{screen}')
        
    
    #Remove character
    def remove_it(self):
        screen = self.OutputLable.text()
        #remove last item in string
        screen = screen[:-1]
        self.OutputLable.setText(screen)
        
    def math_it(self):
       #take whats on the screen
       screen = self.OutputLable.text()
       try:
           #do math
           answer = eval(screen)
           #Output answer to the screen
           self.OutputLable.setText(str(answer))
       except:
           #Output error to the screen
           self.OutputLable.setText("ERROR!!")
    
    def press_it(self, pressed):
        if pressed == "C":
            self.OutputLable.setText("0")
        else:
            #Check whether it starts with 0 and delete 0
            if self.OutputLable.text() == "0":
                self.OutputLable.setText("")
            #concatenate the pressed button which others
            self.OutputLable.setText(f'{self.OutputLable.text()}{pressed}')
    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.NO1.setText(_translate("MainWindow", "1"))
        self.NO2.setText(_translate("MainWindow", "2"))
        self.NO3.setText(_translate("MainWindow", "3"))
        self.Add.setText(_translate("MainWindow", "+"))
        self.NO4.setText(_translate("MainWindow", "4"))
        self.NO6.setText(_translate("MainWindow", "6"))
        self.NO5.setText(_translate("MainWindow", "5"))
        self.Subtract.setText(_translate("MainWindow", "-"))
        self.NO7.setText(_translate("MainWindow", "7"))
        self.NO8.setText(_translate("MainWindow", "8"))
        self.NO9.setText(_translate("MainWindow", "9"))
        self.Multiply.setText(_translate("MainWindow", "*"))
        self.Divide.setText(_translate("MainWindow", "/"))
        self.Clear.setText(_translate("MainWindow", "CLEAR"))
        self.NO0.setText(_translate("MainWindow", "0"))
        self.GROUPC.setText(_translate("MainWindow", "CALCULATOR GROUP C"))
        self.OutputLable.setText(_translate("MainWindow", "OUTPUT LABEL"))
        self.Negativepostive.setText(_translate("MainWindow", "+/-"))
        self.Subtract_2.setText(_translate("MainWindow", "<<"))
        self.Percentage.setText(_translate("MainWindow", "%"))
        self.NO0_2.setText(_translate("MainWindow", "CALCULATE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

