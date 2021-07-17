from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
from modules import affiliate
import re

class CreateAffiliate(object):

    showErrorMessage = None
    showSuccessMessage = None
    manager = affiliate.AffiliateManager()

    def setupUi(self, createAffiliate):
        createAffiliate.setObjectName("createAffiliate")
        createAffiliate.resize(325, 616)
        self.idLabel = QtWidgets.QLabel(createAffiliate)
        self.idLabel.setGeometry(QtCore.QRect(30, 20, 181, 17))
        self.idLabel.setObjectName("idLabel")
        self.idBox = QtWidgets.QLineEdit(createAffiliate)
        self.idBox.setGeometry(QtCore.QRect(30, 40, 261, 25))
        self.idBox.setObjectName("idBox")
        self.idBox.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('\d{1,12}')))
        self.nameLabel = QtWidgets.QLabel(createAffiliate)
        self.nameLabel.setGeometry(QtCore.QRect(30, 80, 181, 17))
        self.nameLabel.setObjectName("nameLabel")
        self.nameBox = QtWidgets.QLineEdit(createAffiliate)
        self.nameBox.setGeometry(QtCore.QRect(30, 100, 261, 25))
        self.nameBox.setMaxLength(26)
        self.nameBox.setObjectName("nameBox")
        self.nameBox.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[a-zA-Z ñáéíóú]{1,26}')))
        self.lastNameLabel = QtWidgets.QLabel(createAffiliate)
        self.lastNameLabel.setGeometry(QtCore.QRect(30, 140, 67, 17))
        self.lastNameLabel.setObjectName("lastNameLabel")
        self.lastNameBox = QtWidgets.QLineEdit(createAffiliate)
        self.lastNameBox.setGeometry(QtCore.QRect(30, 160, 261, 25))
        self.lastNameBox.setMaxLength(26)
        self.lastNameBox.setObjectName("lastNameBox")
        self.lastNameBox.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[a-zA-Z ñáéíóú]{1,26}')))
        self.directionLabel = QtWidgets.QLabel(createAffiliate)
        self.directionLabel.setGeometry(QtCore.QRect(30, 200, 67, 17))
        self.directionLabel.setObjectName("directionLabel")
        self.directionBox = QtWidgets.QLineEdit(createAffiliate)
        self.directionBox.setGeometry(QtCore.QRect(30, 220, 261, 25))
        self.directionBox.setMaxLength(256)
        self.directionBox.setObjectName("directionBox")
        self.directionBox.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[\w| |\-|#]{1,256}')))
        self.phoneLabel = QtWidgets.QLabel(createAffiliate)
        self.phoneLabel.setGeometry(QtCore.QRect(30, 260, 67, 17))
        self.phoneLabel.setObjectName("phoneLabel")
        self.phoneBox = QtWidgets.QLineEdit(createAffiliate)
        self.phoneBox.setGeometry(QtCore.QRect(30, 280, 261, 25))
        self.phoneBox.setObjectName("phoneBox")
        self.phoneBox.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('\d{7,10}')))
        self.emailLabel = QtWidgets.QLabel(createAffiliate)
        self.emailLabel.setGeometry(QtCore.QRect(30, 320, 67, 17))
        self.emailLabel.setObjectName("emailLabel")
        self.emailBox = QtWidgets.QLineEdit(createAffiliate)
        self.emailBox.setGeometry(QtCore.QRect(30, 340, 261, 25))
        self.emailBox.setObjectName("emailBox")
        self.emailBox.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$')))
        self.cityLabel = QtWidgets.QLabel(createAffiliate)
        self.cityLabel.setGeometry(QtCore.QRect(30, 380, 67, 17))
        self.cityLabel.setObjectName("cityLabel")
        self.cityBox = QtWidgets.QLineEdit(createAffiliate)
        self.cityBox.setGeometry(QtCore.QRect(30, 400, 261, 25))
        self.cityBox.setObjectName("cityBox")
        self.cityBox.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[a-zA-Z ñáéíóú]{1,20}')))
        self.birthDateLabel = QtWidgets.QLabel(createAffiliate)
        self.birthDateLabel.setGeometry(QtCore.QRect(30, 440, 161, 17))
        self.birthDateLabel.setObjectName("birthDateLabel")
        self.affiliationDateLabel = QtWidgets.QLabel(createAffiliate)
        self.affiliationDateLabel.setGeometry(QtCore.QRect(30, 500, 141, 17))
        self.affiliationDateLabel.setObjectName("affiliationDateLabel")
        self.createButton = QtWidgets.QPushButton(createAffiliate)
        self.createButton.setGeometry(QtCore.QRect(120, 570, 89, 25))
        self.createButton.setObjectName("createButton")
        self.createButton.clicked.connect(self.onCreateButton)
        self.birthDate = QtWidgets.QDateEdit(createAffiliate)
        self.birthDate.setGeometry(QtCore.QRect(30, 460, 111, 26))
        self.birthDate.setObjectName("birthDate")
        self.affiliationDate = QtWidgets.QDateEdit(createAffiliate)
        self.affiliationDate.setGeometry(QtCore.QRect(30, 520, 111, 26))
        self.affiliationDate.setObjectName("affiliationDate")

        self.retranslateUi(createAffiliate)
        QtCore.QMetaObject.connectSlotsByName(createAffiliate)

    def retranslateUi(self, createAffiliate):
        _translate = QtCore.QCoreApplication.translate
        createAffiliate.setWindowTitle(_translate("createAffiliate", "Crear afiliado"))
        self.idLabel.setText(_translate("createAffiliate", "Número de Identificación"))
        self.nameLabel.setText(_translate("createAffiliate", "Nombres"))
        self.lastNameLabel.setText(_translate("createAffiliate", "Apellidos"))
        self.directionLabel.setText(_translate("createAffiliate", "Dirección"))
        self.phoneLabel.setText(_translate("createAffiliate", "Teléfono"))
        self.emailLabel.setText(_translate("createAffiliate", "Email"))
        self.cityLabel.setText(_translate("createAffiliate", "Ciudad"))
        self.birthDateLabel.setText(_translate("createAffiliate", "Fecha de Nacimiento"))
        self.affiliationDateLabel.setText(_translate("createAffiliate", "Fecha de Afiliación"))
        self.createButton.setText(_translate("createAffiliate", "Crear"))
        self.birthDate.setDisplayFormat(_translate("createAffiliate", "d/M/yyyy"))
        self.affiliationDate.setDisplayFormat(_translate("createAffiliate", "d/M/yyyy"))

    def onCreateButton(self):
        if self.idBox.text() == "":
            self.showErrorMessage("Ingrese número de lote")
            return

        affiliateId = int(self.idBox.text())
        a = self.manager.find(affiliateId)

        if bool(a):
            self.showErrorMessage("Usuario ya existe")
            return
        pass

        names = self.nameBox.text()
        lastNames = self.lastNameBox.text()
        address = self.directionBox.text()
        phone = self.phoneBox.text()
        email = self.emailBox.text()
        city = self.cityBox.text()
        birthDate = int(self.birthDate.dateTime().toPyDateTime().timestamp())
        affiliationDate = int(self.affiliationDate.dateTime().toPyDateTime().timestamp())

        if affiliationDate < birthDate:
            self.showErrorMessag("Error fecha de afiliación menor a fecha de nacimiento")
            return
        if names == "":
            self.showErrorMessage("Ingrese nombres del usuario")
            return
        if lastNames == "":
            self.showErrorMessage("Ingrese apellidos del usuario")
            return
        if address == "":
            self.showErrorMessage("Ingrese dirección del usuario")
            return
        if phone == "":
            self.showErrorMessage("Ingrese teléfono del usuario")
            return    
        if email == "":
            self.showErrorMessage("Ingrese email del usuario")
            return
        regex = re.compile('(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$')
        validated = re.fullmatch(regex, email)
        if not validated : 
            self.showErrorMessage("Email inválido") 
            return
        regex = re.compile('\d{7,10}')
        validated = re.fullmatch(regex, phone)
        if not validated : 
            self.showErrorMessage("teléfono inválido") 
            return
        if city == "":
            self.showErrorMessage("Ingrese ciudad del usuario")
            return

        res = self.manager.add(affiliate.Affiliate(affiliateId, names, lastNames, address,
                                             phone, email, city, birthDate, affiliationDate))
        
        if res:
            self.showSuccessMessage("Usuario registrado exitosamente")
            return
        else:
            self.showErrorMessage("Error registrando usuario intentelo nuevamente")
            return
