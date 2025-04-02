# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QTabWidget, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 500)
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
        self.lbIP = QLabel(self.tabAju)
        self.lbIP.setObjectName(u"lbIP")
        self.lbIP.setGeometry(QRect(300, 78, 111, 16))
        self.lbHTTP = QLabel(self.tabAju)
        self.lbHTTP.setObjectName(u"lbHTTP")
        self.lbHTTP.setGeometry(QRect(300, 60, 121, 16))
        self.tabla = QTableWidget(self.tabAju)
        if (self.tabla.columnCount() < 2):
            self.tabla.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tabla.setObjectName(u"tabla")
        self.tabla.setGeometry(QRect(0, 240, 221, 192))
        self.testMaxi = QPushButton(self.tabAju)
        self.testMaxi.setObjectName(u"testMaxi")
        self.testMaxi.setGeometry(QRect(670, 70, 80, 24))
        self.widget = QWidget(self.tabAju)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(420, 50, 224, 48))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.ipAdd = QLineEdit(self.widget)
        self.ipAdd.setObjectName(u"ipAdd")

        self.gridLayout.addWidget(self.ipAdd, 1, 0, 1, 1)

        self.nameAdd = QLineEdit(self.widget)
        self.nameAdd.setObjectName(u"nameAdd")

        self.gridLayout.addWidget(self.nameAdd, 1, 1, 1, 1)

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
        self.lbIP.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.lbHTTP.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        ___qtablewidgetitem = self.tabla.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"IP", None));
        ___qtablewidgetitem1 = self.tabla.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        self.testMaxi.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n IP", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tabAju), QCoreApplication.translate("MainWindow", u"Ajustes", None))
    # retranslateUi

