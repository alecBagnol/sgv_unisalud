# GUI toolkit module
from PyQt5 import QtCore, QtGui, QtWidgets

# imports the vaccination schedule methods
from modules import vaccination_schedule

# Lib for managing regular expressions
import re

# Third-party library with expanded time zone and parsing support
import datetime


# DESCRIPTION:
        # This module contains a class that builds up a layout section for searching data related to affiliates, vaccination schedule and vaccination plan.

    # ARGUMENTS:
        # UI elements are created using Qt methods.
            # - findDialog: setup layout frame.
            # - horizontalLayoutWidget: creates a widget within layout.
            # - findLayout: sets an horizontal layout.
            # - inputBox: one-line text field to capture id.
            # - findButton: button that calls on click the function to search for the data related to the id.
            # - scrollArea: provides a scrolling view onto another widget


        # placeHolder : placeholder for the lot id input field.
        # regex : set the regex used to validate data.
        # windowName: sets window name.
        # manager: method from object associated to the manager being implemented (affiliates, vaccination plan, vaccination schedule) 

class FindDialog(object):

    placeHolder = ""
    regex = ""
    windowName = ""
    manager = None

    def setupUi(self, findDialog):
        findDialog.setObjectName("findDialog")
        findDialog.resize(500, 500)
        findDialog.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Colombia))
        self.horizontalLayoutWidget = QtWidgets.QWidget(findDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(80, 50, 331, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.findLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.findLayout.setContentsMargins(0, 0, 0, 0)
        self.findLayout.setSpacing(0)
        self.findLayout.setObjectName("findLayout")

        self.inputBox = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.inputBox.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inputBox.setFont(font)
        self.inputBox.setStyleSheet("QLineEdit{ border-top-color: white; border-left-color: white; border-right-color: white; border-bottom-width: 2px; border-style:solid; background-color: rgb(240, 240, 240);}")
        self.inputBox.setInputMethodHints(QtCore.Qt.ImhNone)
        self.inputBox.setObjectName("inputBox")
        self.inputBox.setPlaceholderText(self.placeHolder)
        self.inputBox.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp(self.regex)))

        self.findLayout.addWidget(self.inputBox)
        self.findButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.findButton.setMinimumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.findButton.setFont(font)
        self.findButton.setStyleSheet("background-color: rgb(72, 72, 72); color: rgb(255, 255, 255);")
        self.findButton.setObjectName("findButton")
        self.findButton.clicked.connect(self.onFindClick)

        self.findLayout.addWidget(self.findButton)

        self.scrollArea = QtWidgets.QScrollArea(findDialog)
        self.scrollArea.setGeometry(QtCore.QRect(80, 120, 330, 311))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 328, 309))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.scrollAreaWidgetContents.setFont(font)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.label.setReadOnly(True)
        self.label.setGeometry(QtCore.QRect(0, 0, 330, 311))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setPlainText("")
        self.label.setObjectName("label")
        
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.frame = QtWidgets.QFrame(findDialog)
        self.frame.setGeometry(QtCore.QRect(25, 25, 450, 450))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 12;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.horizontalLayoutWidget.raise_()
        self.scrollArea.raise_()

        self.retranslateUi(findDialog)
        QtCore.QMetaObject.connectSlotsByName(findDialog)

    def retranslateUi(self, findDialog):
        _translate = QtCore.QCoreApplication.translate
        findDialog.setWindowTitle(_translate("findDialog", self.windowName))
        self.findButton.setText(_translate("findDialog", "Buscar"))

    def onFindClick(self):
        raise NotImplementedError
