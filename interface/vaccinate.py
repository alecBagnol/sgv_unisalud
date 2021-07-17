from PyQt5 import QtCore, QtGui, QtWidgets
from modules import affiliate


class Vaccinate(object):
    
    showErrorMessage = None
    showSuccessMessage = None
    manager = affiliate.AffiliateManager()

    def setupUi(self, vaccinate):
        vaccinate.setObjectName("vaccinate")
        vaccinate.resize(455, 155)
        self.box = QtWidgets.QLineEdit(vaccinate)
        self.box.setGeometry(QtCore.QRect(60, 70, 331, 25))
        self.box.setObjectName("box")
        self.box.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('\d{1,12}')))
        self.label = QtWidgets.QLabel(vaccinate)
        self.label.setGeometry(QtCore.QRect(60, 40, 341, 20))
        self.label.setObjectName("label")
        self.vaccinateButton = QtWidgets.QPushButton(vaccinate)
        self.vaccinateButton.setGeometry(QtCore.QRect(170, 110, 89, 25))
        self.vaccinateButton.setObjectName("vaccinateButton")
        self.vaccinateButton.clicked.connect(self.onButtonClick)

        self.retranslateUi(vaccinate)
        QtCore.QMetaObject.connectSlotsByName(vaccinate)

    def retranslateUi(self, vaccinate):
        _translate = QtCore.QCoreApplication.translate
        vaccinate.setWindowTitle(_translate("vaccinate", "Vaccinate"))
        self.label.setText(_translate("vaccinate", "Número de identificación de la persona a vacunar"))
        self.vaccinateButton.setText(_translate("vaccinate", "Vacunar"))

    def onButtonClick(self):
        if self.box.text() == "":
            return
        affiliateId = int(self.box.text())
        a = self.manager.find(affiliateId)

        if bool(a):
            res = self.manager.vaccinate(affiliateId)
            if res == 0:
                self.showSuccessMessage(f"Usuario [{affiliateId}] - Registro de vacunación [EXITOSO] .")
            elif res == 1:
                self.showErrorMessage(f"Error usuario [{affiliateId}] no pudo ser vacunado intente nuevamente.")
            elif res == 2:
                self.showErrorMessage(f"No existe un plan de vacunación relacionado al usuario con ID {affiliateId}")
            elif res == 3:
                self.showErrorMessage(f"Usuario [{affiliateId}] ya ha sido vacunado, intente con otro ID.")
            elif res == 4:
                self.showErrorMessage(f"No existe un plan de vacunación relacionado al usuario con ID {affiliateId}")
        else:
            self.showErrorMessage("USUARIO NO ENCONTRADO")
