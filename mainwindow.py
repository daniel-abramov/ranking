# -*- coding: utf-8 -*-

# Created: Sun Jun 15 19:05:16 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(489, 566)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.prioritiesEdit = QtGui.QLineEdit(self.centralwidget)
        self.prioritiesEdit.setObjectName("prioritiesEdit")
        self.horizontalLayout.addWidget(self.prioritiesEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.normalizeButton = QtGui.QPushButton(self.centralwidget)
        self.normalizeButton.setObjectName("normalizeButton")
        self.gridLayout.addWidget(self.normalizeButton, 0, 1, 1, 1)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 2)
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 489, 21))
        self.menubar.setObjectName("menubar")
        self.menuCriterias = QtGui.QMenu(self.menubar)
        self.menuCriterias.setObjectName("menuCriterias")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdditive = QtGui.QAction(MainWindow)
        self.actionAdditive.setObjectName("actionAdditive")
        self.actionMultiplicative = QtGui.QAction(MainWindow)
        self.actionMultiplicative.setObjectName("actionMultiplicative")
        self.actionKobbDouglas = QtGui.QAction(MainWindow)
        self.actionKobbDouglas.setObjectName("actionKobbDouglas")
        self.actionMainIndividual = QtGui.QAction(MainWindow)
        self.actionMainIndividual.setObjectName("mainIndividualAction")
        self.actionPareto = QtGui.QAction(MainWindow)
        self.actionPareto.setObjectName("actionPareto")
        self.menuCriterias.addAction(self.actionAdditive)
        self.menuCriterias.addAction(self.actionMultiplicative)
        self.menuCriterias.addAction(self.actionKobbDouglas)
        self.menuCriterias.addAction(self.actionMainIndividual)
        self.menuCriterias.addAction(self.actionPareto)
        self.menubar.addAction(self.menuCriterias.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Priorities", None, QtGui.QApplication.UnicodeUTF8))
        self.prioritiesEdit.setText(QtGui.QApplication.translate("MainWindow", "1.0, 1.0, 1.0", None, QtGui.QApplication.UnicodeUTF8))
        self.normalizeButton.setText(QtGui.QApplication.translate("MainWindow", "Normalize", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCriterias.setTitle(QtGui.QApplication.translate("MainWindow", "Criteria", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdditive.setText(QtGui.QApplication.translate("MainWindow", "Additive", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMultiplicative.setText(QtGui.QApplication.translate("MainWindow", "Multiplicative", None, QtGui.QApplication.UnicodeUTF8))
        self.actionKobbDouglas.setText(QtGui.QApplication.translate("MainWindow", "Kobb-Douglas", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMainIndividual.setText(QtGui.QApplication.translate("MainWindow", "Main Individual", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPareto.setText(QtGui.QApplication.translate("MainWindow", "Pareto", None, QtGui.QApplication.UnicodeUTF8))

