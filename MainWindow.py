import re
import matplotlib
from PyQt5.QtWidgets import QMessageBox
from Plotter import Plotter

matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(739, 481)
        MainWindow.setMinimumSize(QtCore.QSize(739, 481))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 80, 211, 61))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, -10, 331, 61))
        self.label_2.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 241, 61))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 180, 241, 61))
        self.label_4.setObjectName("label_4")

        # line edit of equation
        self.equation = QtWidgets.QLineEdit(self.centralwidget)
        self.equation.setGeometry(QtCore.QRect(200, 100, 151, 22))
        self.equation.setObjectName("lineEdit")
        # line edit of max value for x
        self.maxValue = QtWidgets.QLineEdit(self.centralwidget)
        self.maxValue.setGeometry(QtCore.QRect(240, 150, 101, 22))
        self.maxValue.setObjectName("lineEdit_2")
        # line edit of min value for x
        self.minValue = QtWidgets.QLineEdit(self.centralwidget)
        self.minValue.setGeometry(QtCore.QRect(230, 200, 101, 22))
        self.minValue.setObjectName("lineEdit_3")

        self.plotButton = QtWidgets.QPushButton(self.centralwidget,
                                                clicked=lambda: self.plot(self.equation.text(), self.maxValue.text(),
                                                                          self.minValue.text()))
        self.plotButton.setGeometry(QtCore.QRect(290, 300, 131, 28))
        self.plotButton.setObjectName("plot_btn")
        text = "fds"
        # self.plotButton.clicked.connect(self.plot("Fsf"))

        self.label_5 = QtWidgets.QLabel(self.centralwidget, )
        self.label_5.setGeometry(QtCore.QRect(400, 50, 371, 231))
        self.label_5.setMaximumSize(QtCore.QSize(371, 231))
        self.label_5.setObjectName("label_5")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Function plotter"))
        self.label.setText(_translate("MainWindow", "Enter equation to plot :"))
        self.label_2.setText(_translate("MainWindow", "Welcome to your function plotter "))
        self.label_3.setText(_translate("MainWindow", "Enter maximum value for x :"))
        self.label_4.setText(_translate("MainWindow", "Enter minimum value for x :"))
        self.plotButton.setText(_translate("MainWindow", "Plot Graph"))
        self.label_5.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Instructions</span></p><p>- Enter the function of x, like 5*x^3+2*x.</p><p>- The supported operators: + - / * ^.</p><p><br/></p></body></html>"))

    # End of UI
    def showErrorMessage(self, errorMessage):
        QMessageBox.about(self.centralwidget, "Error", errorMessage)

    def validateNumbers(self, value):
        try:
            int(value)
            return True
        except:
            return False

    def isValidRange(self, minValue, maxValue):
        return minValue <= maxValue

    def validateEquation(self, equation):
        equation = equation.replace(" ", "")
        if equation == "":
            # self.showErrorMessage("The Functon Field is Empty, Please Enter it")
            return "The Functon Field is Empty, Please Enter it"

        toMatch = "(-)?(\d+$)|((-)?(\d+[+-])?(\d+[\*\/])?[xX](\^\d+)?([+-](\d+)?([\*\/][xX](\^\d+)?)?)*)*$"
        matched = re.match(toMatch, equation)
        if not matched:
            # self.showErrorMessage("Invalid Function")
            return "Invalid Function"
            # return False
        func = equation.replace('^', '**').replace('X', 'x')
        return func

    def plot(self, equation, maxValue, minValue):
        try:
            orginialEqu = equation
            # validate Function
            ret = self.validateEquation(equation)
            if ret == "The Functon Field is Empty, Please Enter it" or ret == "Invalid Function":
                self.showErrorMessage(ret)
                return
            else:
                equation=ret
            #validate max value
            if self.validateNumbers(maxValue) is False:
                self.showErrorMessage("Please Enter an integer number for maximum value")
                return
            #validate min value
            if self.validateNumbers(minValue) is False:
                self.showErrorMessage("Please Enter an integer number for minimum value")
                return
            minValue = int(minValue)
            maxValue = int(maxValue)
            #validate range
            if self.isValidRange(minValue, maxValue) is False:
                self.showErrorMessage("Please Enter valid range")
                return
            p = Plotter()
            p.plot(minValue, maxValue, equation, orginialEqu)
        except ValueError as err:
            print(err.args[0])
            return


# main function
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())