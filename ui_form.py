# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btClose = QPushButton(self.centralwidget)
        self.btClose.setObjectName(u"btClose")
        self.btClose.setGeometry(QRect(720, 440, 61, 21))
        self.Tabs = QTabWidget(self.centralwidget)
        self.Tabs.setObjectName(u"Tabs")
        self.Tabs.setGeometry(QRect(0, 0, 800, 480))
        self.tabGen = QWidget()
        self.tabGen.setObjectName(u"tabGen")
        self.Tabs.addTab(self.tabGen, "")
        self.tabCons = QWidget()
        self.tabCons.setObjectName(u"tabCons")
        self.Tabs.addTab(self.tabCons, "")
        self.tabAju = QWidget()
        self.tabAju.setObjectName(u"tabAju")
        self.comboBox = QComboBox(self.tabAju)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(400, 240, 72, 24))
        self.lineEdit = QLineEdit(self.tabAju)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 100, 113, 24))
        self.Tabs.addTab(self.tabAju, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.Tabs.raise_()
        self.btClose.raise_()
        QWidget.setTabOrder(self.Tabs, self.btClose)

        self.retranslateUi(MainWindow)

        self.Tabs.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tabGen), QCoreApplication.translate("MainWindow", u"General", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tabCons), QCoreApplication.translate("MainWindow", u"Consulta", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tabAju), QCoreApplication.translate("MainWindow", u"Ajustes", None))
    # retranslateUi

