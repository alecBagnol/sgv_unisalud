from PyQt5 import QtCore, QtGui, QtWidgets
from modules import affiliate

class Vaccinate(object):

    showErrorMessage = None
    showSuccessMessage = None
    manager = affiliate.AffiliateManager()

    def setupUi(self, vaccinate):
        vaccinate.setObjectName("vaccinate")
        vaccinate.resize(450, 300)
        self.box = QtWidgets.QLineEdit(vaccinate)
        self.box.setGeometry(QtCore.QRect(100, 107, 260, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.box.setFont(font)
        self.box.setStyleSheet("border-top-color: white; border-left-color: white; border-right-color: white; border-bottom-width: 2px; border-style:solid;")
        self.box.setObjectName("box")
        self.box.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('\d{1,12}')))
        self.label = QtWidgets.QLabel(vaccinate)
        self.label.setGeometry(QtCore.QRect(100, 90, 260, 20))
        self.label.setStyleSheet("color: rgb(136, 136, 136);")
        self.label.setObjectName("label")
        self.vaccinateButton = QtWidgets.QPushButton(vaccinate)
        self.vaccinateButton.setGeometry(QtCore.QRect(120, 180, 210, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.vaccinateButton.setFont(font)
        self.vaccinateButton.setStyleSheet("background-color: rgb(72, 72, 72); color: rgb(255, 255, 255);")
        self.vaccinateButton.setObjectName("vaccinateButton")
        self.vaccinateButton.clicked.connect(self.onButtonClick)
        self.frame = QtWidgets.QFrame(vaccinate)
        self.frame.setGeometry(QtCore.QRect(25, 25, 400, 250))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 12;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.box.raise_()
        self.label.raise_()
        self.vaccinateButton.raise_()

        self.retranslateUi(vaccinate)
        QtCore.QMetaObject.connectSlotsByName(vaccinate)

    def retranslateUi(self, vaccinate):
        _translate = QtCore.QCoreApplication.translate
        vaccinate.setWindowTitle(_translate("vaccinate", "Vacunación de Afiliados"))
        self.box.setPlaceholderText(_translate("vaccinate", "0000000000"))
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
