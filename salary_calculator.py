# -*- coding: utf-8 -*-

import sys
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

class Ui_MainWindow(QtGui.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(710, 553)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 190, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.tax_rate = QtGui.QSpinBox(self.centralwidget)
        self.tax_rate.setGeometry(QtCore.QRect(250, 190, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.tax_rate.setFont(font)
        self.tax_rate.setMaximum(99)
        self.tax_rate.setProperty("value", 0)
        self.tax_rate.setObjectName(_fromUtf8("tax_rate"))
        self.results_window = QtGui.QTextEdit(self.centralwidget)
        self.results_window.setGeometry(QtCore.QRect(10, 330, 211, 141))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.results_window.setFont(font)
        self.results_window.setObjectName(_fromUtf8("results_window"))
        self.results_window_2 = QtGui.QTextEdit(self.centralwidget)
        self.results_window_2.setGeometry(QtCore.QRect(230, 330, 211, 141))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.results_window_2.setFont(font)
        self.results_window_2.setObjectName(_fromUtf8("results_window_2"))
        self.calc_tax_button = QtGui.QPushButton(self.centralwidget)
        self.calc_tax_button.setGeometry(QtCore.QRect(440, 60, 241, 81))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.calc_tax_button.setFont(font)
        self.calc_tax_button.setObjectName(_fromUtf8("calc_tax_button"))
        self.clear_button = QtGui.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(460, 380, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.clear_button.setFont(font)
        self.clear_button.setObjectName(_fromUtf8("clear_button"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(250, 270, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.brutto_box = QtGui.QTextEdit(self.centralwidget)
        self.brutto_box.setGeometry(QtCore.QRect(120, 110, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.brutto_box.setFont(font)
        self.brutto_box.setObjectName(_fromUtf8("brutto_box"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 60, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.calc_tax_button_2 = QtGui.QPushButton(self.centralwidget)
        self.calc_tax_button_2.setGeometry(QtCore.QRect(440, 150, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.calc_tax_button_2.setFont(font)
        self.calc_tax_button_2.setObjectName(_fromUtf8("calc_tax_button_2"))
        self.calc_tax_button_3 = QtGui.QPushButton(self.centralwidget)
        self.calc_tax_button_3.setGeometry(QtCore.QRect(440, 230, 241, 81))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.calc_tax_button_3.setFont(font)
        self.calc_tax_button_3.setObjectName(_fromUtf8("calc_tax_button_3"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 0, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 270, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 710, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.calc_tax_button.setStyleSheet("background-color: yellow")
        self.calc_tax_button_2.setStyleSheet("background-color: yellow")
        self.calc_tax_button_3.setStyleSheet("background-color: yellow")
        self.clear_button.setStyleSheet("QPushButton { background-color : #cc0000; color : white; }")
        self.label_2.setStyleSheet("QLabel {color : white}")
        self.label_4.setStyleSheet("QLabel {color : white}")
        self.label.setStyleSheet("QLabel {color : white}")
        self.label_3.setStyleSheet("QLabel {color : white}")
        self.label_5.setStyleSheet("QLabel {color : white}")
        self.results_window.setStyleSheet("QTextEdit { background-color : #808080; color : yellow; }")
        self.results_window_2.setStyleSheet("QTextEdit { background-color : #808080; color : yellow; }")
        self.brutto_box.setStyleSheet("QTextEdit { background-color : #808080; color : yellow; }")
        self.tax_rate.setStyleSheet("QSpinBox { background-color : #808080; color : yellow; }")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.clear_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.results_window_2.clear)
        QtCore.QObject.connect(self.clear_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.results_window.clear)
        QtCore.QObject.connect(self.clear_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.brutto_box.clear)
        self.calc_tax_button.clicked.connect(self.BasicEmployee)
        self.calc_tax_button_2.clicked.connect(self.Student)
        self.calc_tax_button_3.clicked.connect(self.Pensioner)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_4.setText(_translate("MainWindow", "Fundusz wakacyjny [%]", None))
        self.calc_tax_button.setText(_translate("MainWindow", "Pracownik zwyczajny", None))
        self.clear_button.setText(_translate("MainWindow", "wyczysc wszystko", None))
        self.label_5.setText(_translate("MainWindow", "Na wakacje", None))
        self.label.setText(_translate("MainWindow", "Stawka brutto", None))
        self.calc_tax_button_2.setText(_translate("MainWindow", "Student", None))
        self.calc_tax_button_3.setText(_translate("MainWindow", "Emeryt/Rencista", None))
        self.label_2.setText(_translate("MainWindow", "OBLICZ SWOJĄ PENSJĘ", None))
        self.label_3.setText(_translate("MainWindow", "Stawka netto", None))

     # function to calculate the salary for an ordinary worker
    def BasicEmployee(self):
        brutto = int(self.brutto_box.toPlainText())
        holiday = (self.tax_rate.value())
        insurance = (brutto * 0.0976) + (brutto * 0.015) + (brutto * 0.0245)
        c = brutto - insurance
        health_tax = c * 0.09
        health_tax2 = c * 0.0775
        basic_tax = brutto - insurance - 111.25
        tax = basic_tax * 0.18
        tax2 = tax - 46.33
        advance_tax = tax2 - health_tax2
        salary = float(brutto - insurance - health_tax - advance_tax)
        holiday2 = round((salary*holiday*0.01), 2)
        salary1 = round(salary, 2) - holiday2
        full_salary = "Twoja pensja netto wynosi: " + str(salary1) + " PLN"
        holiday3 = "Na wakacje odkladasz: " + str(holiday2) + " PLN"
        self.results_window.setText(full_salary)
        self.results_window_2.setText(holiday3)

    # function to calculate the salary for a student
    def Student(self):
        brutto = int(self.brutto_box.toPlainText())
        holiday = (self.tax_rate.value())
        cost = brutto * 0.2
        basic_tax = brutto - cost
        advance_tax = basic_tax * 0.18
        salary = float(brutto - advance_tax)
        salary1 = round(salary, 2)
        holiday1 = round((salary1 * holiday * 0.01), 2)
        salary2 = salary1 - holiday1
        full_salary = "Twoja pensja netto wynosi: " + str(salary2) + " PLN"
        holiday2 = "Na wakacje odkladasz: " + str(holiday1) + " PLN"
        self.results_window.setText(full_salary)
        self.results_window_2.setText(holiday2)

    #function to calculate the salary for a pensioner
    def Pensioner(self):
        brutto = int(self.brutto_box.toPlainText())
        holiday = (self.tax_rate.value())
        insurance = (brutto * 0.0976) + (brutto * 0.015)
        c = brutto - insurance
        health_tax = c * 0.09
        health_tax2 = c * 0.0775
        basic_tax = brutto - insurance - 111.25
        tax = basic_tax * 0.18
        tax2 = tax - 46.33
        advance_tax = tax2 - health_tax2
        salary = float(brutto - insurance - health_tax - advance_tax)
        holiday2 = round((salary * holiday * 0.01), 2)
        salary1 = round(salary, 2) - holiday2
        full_salary = "Twoja pensja netto wynosi: " + str(salary1) + " PLN"
        holiday3 = "Na wakacje odkladasz: " + str(holiday2) + " PLN"
        self.results_window.setText(full_salary)
        self.results_window_2.setText(holiday3)


app = QtGui.QApplication(sys.argv)
app.setStyleSheet("QMainWindow{background-color: #333333}")
window = Ui_MainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)
window.show()
sys.exit(app.exec_())