from PyQt5 import QtCore, QtGui, QtWidgets
from modules import vaccination_schedule
import re
import datetime

class FindDialog(object):

    placeHolder = ""
    regex = ""
    windowName = ""
    manager = None

    def setupUi(self, findDialog):
        findDialog.setObjectName("findDialog")
        findDialog.resize(544, 411)
        findDialog.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Colombia))
        self.horizontalLayoutWidget = QtWidgets.QWidget(findDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 501, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.findLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.findLayout.setContentsMargins(0, 0, 0, 0)
        self.findLayout.setObjectName("findLayout")
        self.inputBox = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.inputBox.setInputMethodHints(QtCore.Qt.ImhNone)
        self.inputBox.setObjectName("inputBox")
        self.inputBox.setPlaceholderText(self.placeHolder)
        self.inputBox.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp(self.regex)))
        self.findLayout.addWidget(self.inputBox)
        self.findButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.findButton.setObjectName("findButton")
        self.findButton.clicked.connect(self.onFindClick)
        self.findLayout.addWidget(self.findButton)
        self.scrollArea = QtWidgets.QScrollArea(findDialog)
        self.scrollArea.setGeometry(QtCore.QRect(20, 90, 501, 311))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 499, 309))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.label.setReadOnly(True)
        self.label.setGeometry(QtCore.QRect(0, 0, 501, 311))
        self.label.setPlainText("")
        self.label.setObjectName("label")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.retranslateUi(findDialog)
        QtCore.QMetaObject.connectSlotsByName(findDialog)

    def retranslateUi(self, findDialog):
        _translate = QtCore.QCoreApplication.translate
        findDialog.setWindowTitle(_translate("findDialog", self.windowName))
        self.findButton.setText(_translate("findDialog", "Buscar"))

    def onFindClick(self):
        raise NotImplementedError

