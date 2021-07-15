from PyQt5 import QtCore, QtGui, QtWidgets
from modules import vaccination_schedule
import re
import datetime

class AffiliateVaccinationSchedule(object):

    manager = vaccination_schedule.VaccinationScheduleManager()

    def setupUi(self, affiliateVaccinationSchedule):
        affiliateVaccinationSchedule.setObjectName("affiliateVaccinationSchedule")
        affiliateVaccinationSchedule.resize(544, 411)
        affiliateVaccinationSchedule.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Colombia))
        self.horizontalLayoutWidget = QtWidgets.QWidget(affiliateVaccinationSchedule)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 501, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.findLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.findLayout.setContentsMargins(0, 0, 0, 0)
        self.findLayout.setObjectName("findLayout")
        self.inputBox = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.inputBox.setInputMethodHints(QtCore.Qt.ImhNone)
        self.inputBox.setObjectName("inputBox")
        self.inputBox.setPlaceholderText("Documento de Identidad")
        self.inputBox.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('\d{1,12}')))
        self.findLayout.addWidget(self.inputBox)
        self.findButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.findButton.setObjectName("findButton")
        self.findButton.clicked.connect(self.onFindClick)
        self.findLayout.addWidget(self.findButton)
        self.scrollArea = QtWidgets.QScrollArea(affiliateVaccinationSchedule)
        self.scrollArea.setGeometry(QtCore.QRect(20, 90, 501, 311))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 499, 309))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(0, 0, 501, 311))
        self.label.setText("")
        self.label.setObjectName("label")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.retranslateUi(affiliateVaccinationSchedule)
        QtCore.QMetaObject.connectSlotsByName(affiliateVaccinationSchedule)

    def retranslateUi(self, affiliateVaccinationSchedule):
        _translate = QtCore.QCoreApplication.translate
        affiliateVaccinationSchedule.setWindowTitle(_translate("affiliateVaccinationSchedule", "Programación"))
        self.findButton.setText(_translate("affiliateVaccinationSchedule", "Buscar"))

    def onFindClick(self):
        if self.inputBox.text() == "":
            return
        affiliate = int(self.inputBox.text())
        schedule = self.manager.get_schedule(affiliate)

        if bool(schedule):
            self.label.setText(f"""
                Nombres: {schedule["affiliate"]["first_name"]}
                Apellidos: {schedule["affiliate"]["last_name"]}
                Documento de Identidad: {schedule["affiliate"]["affiliate_id"]}
                Dirección: {schedule["affiliate"]["address"]}
                Teléfono: {schedule["affiliate"]["phone"]}
                Correo: {schedule["affiliate"]["email"]}
                Fecha de Nacimiento: {datetime.datetime.fromtimestamp(schedule["affiliate"]["birth_date"]).strftime("%d/%m/%Y")}
                Ciudad: {schedule["affiliate"]["city"]}
                Lote de Vacunas: {schedule["vaccine_lot"]["vaccine_lot_id"]}
                Fecha y Hora de Vacunación: {datetime.datetime.fromtimestamp(schedule["date_time"]).strftime("%d/%m/%Y, %H:%M:%S")}
            """)
        else:
            self.label.setText("    USUARIO NO ENCONTRADO")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    affiliateVaccinationSchedule = QtWidgets.QDialog()
    ui = AffiliateVaccinationSchedule()
    ui.setupUi(affiliateVaccinationSchedule)
    affiliateVaccinationSchedule.show()
    sys.exit(app.exec_())
