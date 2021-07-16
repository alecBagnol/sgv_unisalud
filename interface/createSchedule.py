import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from modules import vaccination_schedule

class CreateSchedule(object):

    showErrorMessage = None
    showSuccessMessage = None
    manager = vaccination_schedule.VaccinationScheduleManager()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(420, 161)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeEdit.setGeometry(QtCore.QRect(120, 40, 194, 26))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 10, 191, 17))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(160, 80, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.createSchedule)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Crear Programación"))
        self.dateTimeEdit.setDisplayFormat(_translate("Dialog", "d/M/yyyy hh:mm:ss AP"))
        self.label.setText(_translate("Dialog", "Elija fecha y hora"))
        self.pushButton.setText(_translate("Dialog", "Crear"))

    def createSchedule(self):
        date = int(self.dateTimeEdit.dateTime().toPyDateTime().timestamp())
        res = self.manager.create_all_vaccination_schedule(date)
        if res:
            self.showSuccessMessage("Programación creada con éxito")
        else:
            self.showErrorMessage("Programación NO creada intentelo de nuevo")
