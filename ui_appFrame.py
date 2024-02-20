# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'appFramenMQOxv.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(410, 120)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"font: 700 10pt \"Small Fonts\";")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainbox = QFrame(self.centralwidget)
        self.mainbox.setObjectName(u"mainbox")
        self.mainbox.setStyleSheet(u"#mainbox {\n"
"	background-color: #000;\n"
"	border-radius: 8px;\n"
"}")
        self.mainbox.setFrameShape(QFrame.NoFrame)
        self.mainbox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mainbox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.title = QFrame(self.mainbox)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(0, 50))
        self.title.setMaximumSize(QSize(16777215, 50))
        self.title.setStyleSheet(u"padding-left: 1px;\n"
"padding-right: 2px;")
        self.title.setFrameShape(QFrame.NoFrame)
        self.title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(8, 0, 8, 0)
        self.label = QLabel(self.title)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: #fff;\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.label)

        self.mini = QPushButton(self.title)
        self.mini.setObjectName(u"mini")
        self.mini.setMaximumSize(QSize(20, 20))
        self.mini.setCursor(QCursor(Qt.PointingHandCursor))
        self.mini.setStyleSheet(u"#mini {\n"
"	border: none;\n"
"	color: #999;\n"
"	font-size: 30px;\n"
"}\n"
"#mini:hover {\n"
"	background-color: #000;\n"
"	color: #fff;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.mini)

        self.close = QPushButton(self.title)
        self.close.setObjectName(u"close")
        self.close.setMaximumSize(QSize(20, 20))
        self.close.setCursor(QCursor(Qt.PointingHandCursor))
        self.close.setStyleSheet(u"#close {\n"
"	border: none;\n"
"	color: #999;\n"
"	font-size: 20px;\n"
"}\n"
"#close:hover {\n"
"	background-color: #000;\n"
"	color: #fff;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.close)


        self.verticalLayout_2.addWidget(self.title)

        self.body = QFrame(self.mainbox)
        self.body.setObjectName(u"body")
        self.body.setMinimumSize(QSize(0, 70))
        self.body.setMaximumSize(QSize(16777215, 70))
        self.body.setFrameShape(QFrame.NoFrame)
        self.body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.body)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.options = QFrame(self.body)
        self.options.setObjectName(u"options")
        self.options.setMaximumSize(QSize(16777215, 16777215))
        self.options.setFrameShape(QFrame.NoFrame)
        self.options.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.options)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.startstop = QPushButton(self.options)
        self.startstop.setObjectName(u"startstop")
        self.startstop.setMaximumSize(QSize(16777, 16777215))
        self.startstop.setCursor(QCursor(Qt.PointingHandCursor))
        self.startstop.setStyleSheet(u"#startstop {\n"
"background: none;\n"
"height: 40px;\n"
"color: #fff;\n"
"border: none;\n"
"}\n"
"\n"
"")
        self.startstop.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.startstop)


        self.verticalLayout_3.addWidget(self.options)


        self.verticalLayout_2.addWidget(self.body)


        self.verticalLayout.addWidget(self.mainbox)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"jupyter notebook", None))
        self.mini.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.close.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.startstop.setText(QCoreApplication.translate("MainWindow", u"BASLAT", None))
    # retranslateUi

