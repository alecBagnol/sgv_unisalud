import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from modules import vaccination_schedule

class CreateSchedule(object):

    showErrorMessage = None
    showSuccessMessage = None
    manager = vaccination_schedule.VaccinationScheduleManager()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 300)

        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeEdit.setGeometry(QtCore.QRect(95, 100, 261, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setStyleSheet("border-top-color: white; border-left-color: white; border-right-color: white; border-bottom-width: 2px; border-style:solid;")
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        
        self.date_time_title = QtWidgets.QLabel(Dialog)
        self.date_time_title.setGeometry(QtCore.QRect(95, 80, 261, 17))
        self.date_time_title.setStyleSheet("color: rgb(136, 136, 136);")
        self.date_time_title.setObjectName("date_time_title")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(125, 170, 210, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color: rgb(72, 72, 72); color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.createSchedule)

        self.bg_card = QtWidgets.QFrame(Dialog)
        self.bg_card.setGeometry(QtCore.QRect(25, 25, 400, 250))
        self.bg_card.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 12;")
        self.bg_card.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bg_card.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bg_card.setObjectName("bg_card")
        self.bg_card.raise_()
        self.dateTimeEdit.raise_()
        self.date_time_title.raise_()
        self.pushButton.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Crear Programación"))
        self.dateTimeEdit.setDisplayFormat(_translate("Dialog", "d/M/yyyy hh:mm:ss AP"))
        self.date_time_title.setText(_translate("Dialog", "Elija fecha y hora"))
        self.pushButton.setText(_translate("Dialog", "Crear"))

    def createSchedule(self):
        date = int(self.dateTimeEdit.dateTime().toPyDateTime().timestamp())
        res = self.manager.create_all_vaccination_schedule(date)
        if res:
            self.showSuccessMessage("Programación creada con éxito")
        else:
            self.showErrorMessage("Programación NO creada intentelo de nuevo")

