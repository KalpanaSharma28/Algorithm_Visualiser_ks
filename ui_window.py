# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_windowiHLxDk.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtWidgets import (QComboBox, QHBoxLayout,
    QPushButton, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.algorithm_combo = QComboBox(self.centralwidget)
        self.algorithm_combo.addItem("")
        self.algorithm_combo.addItem("")
        self.algorithm_combo.addItem("")
        self.algorithm_combo.addItem("")
        self.algorithm_combo.addItem("")
        self.algorithm_combo.addItem("")
        self.algorithm_combo.setObjectName(u"algorithm_combo")

        self.verticalLayout_2.addWidget(self.algorithm_combo)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sort_button = QPushButton(self.centralwidget)
        self.sort_button.setObjectName(u"sort_button")

        self.horizontalLayout.addWidget(self.sort_button)

        self.reset_button = QPushButton(self.centralwidget)
        self.reset_button.setObjectName(u"reset_button")

        self.horizontalLayout.addWidget(self.reset_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_4.addWidget(self.textEdit)


        self.verticalLayout.addLayout(self.verticalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.algorithm_combo.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sorting Visualizer", None))
        self.algorithm_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"Bubble Sort", None))
        self.algorithm_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"Insertion Sort", None))
        self.algorithm_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"Selection Sort", None))
        self.algorithm_combo.setItemText(3, QCoreApplication.translate("MainWindow", u"Merge Sort", None))
        self.algorithm_combo.setItemText(4, QCoreApplication.translate("MainWindow", u"Quick Sort", None))
        self.algorithm_combo.setItemText(5, QCoreApplication.translate("MainWindow", u"Counting Sort", None))

        self.sort_button.setText(QCoreApplication.translate("MainWindow", u"Sort", None))
        self.reset_button.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
    # retranslateUi

