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
        findDialog.resize(500, 650)
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
        self.inputBox.setStyleSheet("QLineEdit{ border-top-color: white; border-left-color: white; border-right-color: white; border-bottom-width: 2px; border-style:solid; background-color: rgb(255, 255, 255);}")
        self.inputBox.setInputMethodHints(QtCore.Qt.ImhNone)
        # if error delete
        self.inputBox.setText("")
        self.inputBox.setObjectName("inputBox")
        # self.inputBox.setPlaceholderText(self.placeHolder)
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
        self.scrollArea.setGeometry(QtCore.QRect(80, 120, 330, 475))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setStyleSheet("background-color: rgb(255, 255, 255);border-radius:12; border-color: black ; border-width: 1px; border-style:solid;")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 328, 473))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.scrollAreaWidgetContents.setFont(font)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setStyleSheet("border-width: 0px;border-radius:12;")

        self.label = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.label.setReadOnly(True)
        self.label.setGeometry(QtCore.QRect(19, 220, 311, 251))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setPlainText("")
        self.label.setObjectName("label")
        self.label.setStyleSheet("border-color: white; border-width: 2px; border-style:solid; background-color: rgb(255, 255, 255);border-radius:12;")

        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setGeometry(QtCore.QRect(-1, -1, 331, 161))
        self.frame_2.setStyleSheet("background-color: rgb(72, 72, 72);border-width: 0px;border-radius:12;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setGeometry(QtCore.QRect(80, 50, 171, 171))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);border-width: 0px; border-style:solid;border-radius:12;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")

        self.imagePreview = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.imagePreview.setGeometry(QtCore.QRect(90, 60, 150, 150))
        self.imagePreview.setMinimumSize(QtCore.QSize(150, 150))
        self.imagePreview.setMaximumSize(QtCore.QSize(100, 100))
        self.imagePreview.setStyleSheet("border-radius: 20;")
        self.imagePreview.setText("")
        self.imagePreview.setPixmap(QtGui.QPixmap("./interface/img/img_placeholder.png"))
        self.imagePreview.setScaledContents(True)
        self.imagePreview.setObjectName("imagePreview")
        self.imagePreview.setStyleSheet("border-width: 0px;border-radius:0;")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.frame = QtWidgets.QFrame(findDialog)
        self.frame.setGeometry(QtCore.QRect(25, 25, 450, 600))
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
        self.inputBox.setPlaceholderText(_translate("findDialog", "Número de Id del Lote"))
        self.findButton.setText(_translate("findDialog", "Buscar"))

    def setImage(self, image_data):

        # ui->label->setPixmap( pix.scaled( ui->label->size(), Qt::KeepAspectRatio, Qt::SmoothTransformation) );

        pixmap = QtGui.QPixmap(image_data)
        # self.imagePreview.setPixmap(QtGui.QPixmap(pixmap))
        self.imagePreview.setPixmap(pixmap.scaled(self.imagePreview.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))

    def onFindClick(self):
        raise NotImplementedError
