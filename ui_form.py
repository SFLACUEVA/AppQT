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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
    QHBoxLayout, QLabel, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btClose = QPushButton(self.centralwidget)
        self.btClose.setObjectName(u"btClose")
        self.btClose.setGeometry(QRect(720, 0, 81, 21))
        self.Tabs = QTabWidget(self.centralwidget)
        self.Tabs.setObjectName(u"Tabs")
        self.Tabs.setGeometry(QRect(0, 0, 800, 480))
        self.Tabs.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.tabGen = QWidget()
        self.tabGen.setObjectName(u"tabGen")
        self.horizontalLayoutWidget_2 = QWidget(self.tabGen)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, 0, 521, 451))
        self.chaLayout = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.chaLayout.setObjectName(u"chaLayout")
        self.chaLayout.setContentsMargins(0, 0, 0, 0)
        self.btCharge = QPushButton(self.tabGen)
        self.btCharge.setObjectName(u"btCharge")
        self.btCharge.setGeometry(QRect(530, 20, 261, 41))
        self.groupBox = QGroupBox(self.tabGen)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(530, 60, 261, 171))
        self.horizontalLayoutWidget_3 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 30, 241, 130))
        self.configLayout = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.configLayout.setObjectName(u"configLayout")
        self.configLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_13 = QLabel(self.horizontalLayoutWidget_3)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout.addWidget(self.label_13)

        self.label_2 = QLabel(self.horizontalLayoutWidget_3)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_4 = QLabel(self.horizontalLayoutWidget_3)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.horizontalLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.label_10 = QLabel(self.horizontalLayoutWidget_3)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout.addWidget(self.label_10)

        self.label_11 = QLabel(self.horizontalLayoutWidget_3)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout.addWidget(self.label_11)


        self.configLayout.addLayout(self.verticalLayout)

        self.limLayout = QVBoxLayout()
        self.limLayout.setObjectName(u"limLayout")

        self.configLayout.addLayout(self.limLayout)

        self.unitsLayout = QVBoxLayout()
        self.unitsLayout.setObjectName(u"unitsLayout")
        self.label_14 = QLabel(self.horizontalLayoutWidget_3)
        self.label_14.setObjectName(u"label_14")

        self.unitsLayout.addWidget(self.label_14)

        self.label_6 = QLabel(self.horizontalLayoutWidget_3)
        self.label_6.setObjectName(u"label_6")

        self.unitsLayout.addWidget(self.label_6)

        self.label_7 = QLabel(self.horizontalLayoutWidget_3)
        self.label_7.setObjectName(u"label_7")

        self.unitsLayout.addWidget(self.label_7)

        self.label_8 = QLabel(self.horizontalLayoutWidget_3)
        self.label_8.setObjectName(u"label_8")

        self.unitsLayout.addWidget(self.label_8)

        self.label_9 = QLabel(self.horizontalLayoutWidget_3)
        self.label_9.setObjectName(u"label_9")

        self.unitsLayout.addWidget(self.label_9)

        self.label_12 = QLabel(self.horizontalLayoutWidget_3)
        self.label_12.setObjectName(u"label_12")

        self.unitsLayout.addWidget(self.label_12)


        self.configLayout.addLayout(self.unitsLayout)

        self.statusGroup = QGroupBox(self.tabGen)
        self.statusGroup.setObjectName(u"statusGroup")
        self.statusGroup.setGeometry(QRect(530, 330, 261, 111))
        self.statusText = QPlainTextEdit(self.statusGroup)
        self.statusText.setObjectName(u"statusText")
        self.statusText.setGeometry(QRect(10, 30, 161, 70))
        self.statusText.setReadOnly(True)
        self.groupBox_5 = QGroupBox(self.tabGen)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(530, 230, 261, 101))
        self.verticalLayoutWidget_2 = QWidget(self.groupBox_5)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 30, 241, 61))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.batLoad = QPushButton(self.verticalLayoutWidget_2)
        self.batLoad.setObjectName(u"batLoad")

        self.horizontalLayout_2.addWidget(self.batLoad)

        self.batSave = QPushButton(self.verticalLayoutWidget_2)
        self.batSave.setObjectName(u"batSave")

        self.horizontalLayout_2.addWidget(self.batSave)

        self.batRefresh = QPushButton(self.verticalLayoutWidget_2)
        self.batRefresh.setObjectName(u"batRefresh")

        self.horizontalLayout_2.addWidget(self.batRefresh)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.batCombo = QComboBox(self.verticalLayoutWidget_2)
        self.batCombo.addItem("")
        self.batCombo.setObjectName(u"batCombo")

        self.verticalLayout_4.addWidget(self.batCombo)

        self.Tabs.addTab(self.tabGen, "")
        self.tabCons = QWidget()
        self.tabCons.setObjectName(u"tabCons")
        self.groupBox_2 = QGroupBox(self.tabCons)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(530, 270, 261, 171))
        self.horizontalLayoutWidget_4 = QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(10, 30, 241, 130))
        self.configLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.configLayout_2.setObjectName(u"configLayout_2")
        self.configLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_15 = QLabel(self.horizontalLayoutWidget_4)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_2.addWidget(self.label_15)

        self.label_16 = QLabel(self.horizontalLayoutWidget_4)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_2.addWidget(self.label_16)

        self.label_17 = QLabel(self.horizontalLayoutWidget_4)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_2.addWidget(self.label_17)

        self.label_18 = QLabel(self.horizontalLayoutWidget_4)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_2.addWidget(self.label_18)

        self.label_19 = QLabel(self.horizontalLayoutWidget_4)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_2.addWidget(self.label_19)

        self.label_20 = QLabel(self.horizontalLayoutWidget_4)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_2.addWidget(self.label_20)


        self.configLayout_2.addLayout(self.verticalLayout_2)

        self.consConfLayout = QVBoxLayout()
        self.consConfLayout.setObjectName(u"consConfLayout")
        self.batNameLab = QLabel(self.horizontalLayoutWidget_4)
        self.batNameLab.setObjectName(u"batNameLab")
        self.batNameLab.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.consConfLayout.addWidget(self.batNameLab)

        self.vMLab = QLabel(self.horizontalLayoutWidget_4)
        self.vMLab.setObjectName(u"vMLab")
        self.vMLab.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.consConfLayout.addWidget(self.vMLab)

        self.iMLab = QLabel(self.horizontalLayoutWidget_4)
        self.iMLab.setObjectName(u"iMLab")
        self.iMLab.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.consConfLayout.addWidget(self.iMLab)

        self.imLab = QLabel(self.horizontalLayoutWidget_4)
        self.imLab.setObjectName(u"imLab")
        self.imLab.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.consConfLayout.addWidget(self.imLab)

        self.tMLab = QLabel(self.horizontalLayoutWidget_4)
        self.tMLab.setObjectName(u"tMLab")
        self.tMLab.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.consConfLayout.addWidget(self.tMLab)

        self.ctLab = QLabel(self.horizontalLayoutWidget_4)
        self.ctLab.setObjectName(u"ctLab")
        self.ctLab.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.consConfLayout.addWidget(self.ctLab)


        self.configLayout_2.addLayout(self.consConfLayout)

        self.unitsLayout_2 = QVBoxLayout()
        self.unitsLayout_2.setObjectName(u"unitsLayout_2")
        self.label_21 = QLabel(self.horizontalLayoutWidget_4)
        self.label_21.setObjectName(u"label_21")

        self.unitsLayout_2.addWidget(self.label_21)

        self.label_22 = QLabel(self.horizontalLayoutWidget_4)
        self.label_22.setObjectName(u"label_22")

        self.unitsLayout_2.addWidget(self.label_22)

        self.label_23 = QLabel(self.horizontalLayoutWidget_4)
        self.label_23.setObjectName(u"label_23")

        self.unitsLayout_2.addWidget(self.label_23)

        self.label_24 = QLabel(self.horizontalLayoutWidget_4)
        self.label_24.setObjectName(u"label_24")

        self.unitsLayout_2.addWidget(self.label_24)

        self.label_25 = QLabel(self.horizontalLayoutWidget_4)
        self.label_25.setObjectName(u"label_25")

        self.unitsLayout_2.addWidget(self.label_25)

        self.label_26 = QLabel(self.horizontalLayoutWidget_4)
        self.label_26.setObjectName(u"label_26")

        self.unitsLayout_2.addWidget(self.label_26)


        self.configLayout_2.addLayout(self.unitsLayout_2)

        self.horizontalLayoutWidget_5 = QWidget(self.tabCons)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(0, 0, 521, 451))
        self.consLayout = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.consLayout.setObjectName(u"consLayout")
        self.consLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox_3 = QGroupBox(self.tabCons)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(530, 20, 261, 101))
        self.verticalLayoutWidget = QWidget(self.groupBox_3)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 30, 241, 61))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btLoad = QPushButton(self.verticalLayoutWidget)
        self.btLoad.setObjectName(u"btLoad")

        self.horizontalLayout.addWidget(self.btLoad)

        self.btRefresh = QPushButton(self.verticalLayoutWidget)
        self.btRefresh.setObjectName(u"btRefresh")

        self.horizontalLayout.addWidget(self.btRefresh)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.sumCombo = QComboBox(self.verticalLayoutWidget)
        self.sumCombo.setObjectName(u"sumCombo")

        self.verticalLayout_3.addWidget(self.sumCombo)

        self.groupBox_4 = QGroupBox(self.tabCons)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(530, 120, 261, 151))
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox_4)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(10, 30, 241, 111))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_27 = QLabel(self.horizontalLayoutWidget_7)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_5.addWidget(self.label_27)

        self.label_28 = QLabel(self.horizontalLayoutWidget_7)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_5.addWidget(self.label_28)

        self.label_29 = QLabel(self.horizontalLayoutWidget_7)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_5.addWidget(self.label_29)

        self.label_30 = QLabel(self.horizontalLayoutWidget_7)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_5.addWidget(self.label_30)

        self.label_31 = QLabel(self.horizontalLayoutWidget_7)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_5.addWidget(self.label_31)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.StartLb = QLabel(self.horizontalLayoutWidget_7)
        self.StartLb.setObjectName(u"StartLb")
        font = QFont()
        font.setPointSize(7)
        self.StartLb.setFont(font)

        self.verticalLayout_6.addWidget(self.StartLb)

        self.StopLb = QLabel(self.horizontalLayoutWidget_7)
        self.StopLb.setObjectName(u"StopLb")
        self.StopLb.setFont(font)

        self.verticalLayout_6.addWidget(self.StopLb)

        self.vLb = QLabel(self.horizontalLayoutWidget_7)
        self.vLb.setObjectName(u"vLb")

        self.verticalLayout_6.addWidget(self.vLb)

        self.iLb = QLabel(self.horizontalLayoutWidget_7)
        self.iLb.setObjectName(u"iLb")

        self.verticalLayout_6.addWidget(self.iLb)

        self.tLb = QLabel(self.horizontalLayoutWidget_7)
        self.tLb.setObjectName(u"tLb")

        self.verticalLayout_6.addWidget(self.tLb)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)

        self.Tabs.addTab(self.tabCons, "")
        self.tabTest = QWidget()
        self.tabTest.setObjectName(u"tabTest")
        self.horizontalLayoutWidget_6 = QWidget(self.tabTest)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(0, 0, 521, 451))
        self.loadLayout = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.loadLayout.setObjectName(u"loadLayout")
        self.loadLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox_6 = QGroupBox(self.tabTest)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(550, 10, 231, 181))
        self.verticalLayoutWidget_3 = QWidget(self.groupBox_6)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 30, 211, 141))
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_34 = QLabel(self.verticalLayoutWidget_3)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_8.addWidget(self.label_34)

        self.label_33 = QLabel(self.verticalLayoutWidget_3)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_8.addWidget(self.label_33)

        self.label_32 = QLabel(self.verticalLayoutWidget_3)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_8.addWidget(self.label_32)

        self.label_35 = QLabel(self.verticalLayoutWidget_3)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_8.addWidget(self.label_35)


        self.horizontalLayout_4.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.testFloat = QLabel(self.verticalLayoutWidget_3)
        self.testFloat.setObjectName(u"testFloat")

        self.verticalLayout_9.addWidget(self.testFloat)

        self.testLoad = QLabel(self.verticalLayoutWidget_3)
        self.testLoad.setObjectName(u"testLoad")

        self.verticalLayout_9.addWidget(self.testLoad)

        self.testCurrent = QLabel(self.verticalLayoutWidget_3)
        self.testCurrent.setObjectName(u"testCurrent")

        self.verticalLayout_9.addWidget(self.testCurrent)

        self.testR = QLabel(self.verticalLayoutWidget_3)
        self.testR.setObjectName(u"testR")

        self.verticalLayout_9.addWidget(self.testR)


        self.horizontalLayout_4.addLayout(self.verticalLayout_9)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)

        self.testBtn = QPushButton(self.verticalLayoutWidget_3)
        self.testBtn.setObjectName(u"testBtn")

        self.verticalLayout_7.addWidget(self.testBtn)

        self.groupBox_7 = QGroupBox(self.tabTest)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(550, 230, 231, 61))
        self.discBtn = QPushButton(self.groupBox_7)
        self.discBtn.setObjectName(u"discBtn")
        self.discBtn.setGeometry(QRect(10, 30, 209, 24))
        self.Tabs.addTab(self.tabTest, "")
        self.tabAju = QWidget()
        self.tabAju.setObjectName(u"tabAju")
        self.groupBox_8 = QGroupBox(self.tabAju)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setGeometry(QRect(10, 10, 241, 151))
        self.horizontalLayoutWidget = QWidget(self.groupBox_8)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 30, 221, 111))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_12.addWidget(self.label)

        self.label_37 = QLabel(self.horizontalLayoutWidget)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_12.addWidget(self.label_37)

        self.label_38 = QLabel(self.horizontalLayoutWidget)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_12.addWidget(self.label_38)

        self.label_36 = QLabel(self.horizontalLayoutWidget)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_12.addWidget(self.label_36)

        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_12.addWidget(self.label_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_12)

        self.settingsLayout = QVBoxLayout()
        self.settingsLayout.setObjectName(u"settingsLayout")

        self.horizontalLayout_6.addLayout(self.settingsLayout)

        self.pushButton = QPushButton(self.tabAju)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(260, 30, 111, 24))
        self.pushButton_2 = QPushButton(self.tabAju)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(260, 60, 111, 24))
        self.label_40 = QLabel(self.tabAju)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(0, 430, 791, 16))
        self.Tabs.addTab(self.tabAju, "")
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setEnabled(False)
        self.checkBox.setGeometry(QRect(640, 0, 78, 22))
        self.checkBox.setChecked(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.Tabs.raise_()
        self.btClose.raise_()
        self.checkBox.raise_()
        QWidget.setTabOrder(self.Tabs, self.btClose)

        self.retranslateUi(MainWindow)

        self.Tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.btCharge.setText(QCoreApplication.translate("MainWindow", u"Charge with current settings", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Charge configuration", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"NAME", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"MAX VOLTAGE ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"MAX CURRENT ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"MIN CURRENT ", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"MAX TEMP", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"TEMP COMP", None))
        self.label_14.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u00baC", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"-mV/\u00baC", None))
        self.statusGroup.setTitle(QCoreApplication.translate("MainWindow", u"State", None))
        self.statusText.setPlainText(QCoreApplication.translate("MainWindow", u"Waiting", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Select battery model", None))
        self.batLoad.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.batSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.batRefresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.batCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"MVH1290", None))

        self.Tabs.setTabText(self.Tabs.indexOf(self.tabGen), QCoreApplication.translate("MainWindow", u"General", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Charge configuration", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"NAME", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"MAX VOLTAGE ", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"MAX CURRENT ", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"MIN CURRENT ", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"MAX TEMP", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"TEMP COMP", None))
        self.batNameLab.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.vMLab.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.iMLab.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.imLab.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.tMLab.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.ctLab.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_21.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u00baC", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"-mV/\u00baC", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Select charge", None))
        self.btLoad.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.btRefresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Charge summary", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Start:", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Stop:", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Voltage range:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Current range:", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Temperature range:", None))
        self.StartLb.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.StopLb.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.vLb.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.iLb.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.tLb.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tabCons), QCoreApplication.translate("MainWindow", u"Summary", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Load test", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Float voltage:", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Load voltage:", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Current:", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Resistor:", None))
        self.testFloat.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.testLoad.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.testCurrent.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.testR.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.testBtn.setText(QCoreApplication.translate("MainWindow", u"Start test", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Discharge test", None))
        self.discBtn.setText(QCoreApplication.translate("MainWindow", u"Start test", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tabTest), QCoreApplication.translate("MainWindow", u"Test", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Server address:", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Device name:", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Load resistor:", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"SSID:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"SSID Password:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Connect to server", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Connect to WiFi", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Sergio Franco Lacueva, 2025", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tabAju), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Online", None))
    # retranslateUi

