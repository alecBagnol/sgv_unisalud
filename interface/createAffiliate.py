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
        createAffiliate.resize(450, 768)
        createAffiliate.setStyleSheet("")

        self.idLabel = QtWidgets.QLabel(createAffiliate)
        self.idLabel.setGeometry(QtCore.QRect(95, 68, 261, 17))
        self.idLabel.setStyleSheet("color: rgb(136, 136, 136);")
        self.idLabel.setObjectName("idLabel")

        self.idBox = QtWidgets.QLineEdit(createAffiliate)
        self.idBox.setGeometry(QtCore.QRect(95, 80, 261, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.idBox.setFont(font)
        self.idBox.setStyleSheet("border-top-color: white; border-left-color: white; border-right-color: white; border-bottom-width: 2px; border-style:solid;")
        self.idBox.setText("")
        self.idBox.setFrame(True)
        self.idBox.setObjectName("idBox")
        self.idBox.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('\d{1,12}')))
        
        self.nameLabel = QtWidgets.QLabel(createAffiliate)
        self.nameLabel.setGeometry(QtCore.QRect(95, 128, 261, 17))
        self.nameLabel.setStyleSheet("color: rgb(136, 136, 136);")
        self.nameLabel.setObjectName("nameLabel")

        self.nameBox = QtWidgets.QLineEdit(createAffiliate)
        self.nameBox.setGeometry(QtCore.QRect(95, 140, 261, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nameBox.setFont(font)
        self.nameBox.setStyleSheet("border-top-color: white; border-left-color: white; border-right-color: white; border-bottom-width: 2px; border-style:solid;")
        self.nameBox.setMaxLength(26)
        self.nameBox.setObjectName("nameBox")
        self.nameBox.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[a-zA-Z ñáéíóú]{1,26}')))

        self.lastNameLabel = QtWidgets.QLabel(createAffiliate)
        self.lastNameLabel.setGeometry(QtCore.QRect(95, 190, 261, 17))
        self.lastNameLabel.setStyleSheet("color: rgb(136, 136, 136);")
        self.lastNameLabel.setObjectName("lastNameLabel")

        self.lastNameBox = QtWidgets.QLineEdit(createAffiliate)
        self.lastNameBox.setGeometry(QtCore.QRect(95, 202, 261, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lastNameBox.setFont(font)
        self.lastNameBox.setStyleSheet("border-top-color: white; border-left-color: white; border-right-color: white; border-bottom-width: 2px; border-style:solid;")
        self.lastNameBox.setMaxLength(26)
        self.lastNameBox.setObjectName("lastNameBox")
        self.lastNameBox.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[a-zA-Z ñáéíóú]{1,26}')))

        self.directionLabel = QtWidgets.QLabel(createAffiliate)
        self.directionLabel.setGeometry(QtCore.QRect(95, 248, 261, 17))
        self.directionLabel.setStyleSheet("color: rgb(136, 136, 136);")
        self.directionLabel.setObjectName("directionLabel")
        self.directionBox = QtWidgets.QLineEdit(createAffiliate)
        self.directionBox.setGeometry(QtCore.QRect(95, 260, 261, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.directionBox.setFont(font)
        self.directionBox.setStyleSheet("border-top-color: white; border-left-color: white; border-right-color: white; border-bottom-width: 2px; border-style:solid;")
        self.directionBox.setMaxLength(256)
        self.directionBox.setObjectName("directionBox")
        self.directionBox.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[\w| |\-|#]{1,256}')))

        self.phoneLabel = QtWidgets.QLabel(createAffiliate)
        self.phoneLabel.setGeometry(QtCore.QRect(95, 308, 261, 17))
        self.phoneLabel.setStyleSheet("color: rgb(136, 136, 136);")
        self.phoneLabel.setObjectName("phoneLabel")

        self.phoneBox = QtWidgets.QLineEdit(createAffiliate)
        self.phoneBox.setGeometry(QtCore.QRect(95, 320, 261, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.phoneBox.setFont(font)
        self.phoneBox.setStyleSheet("border-top-color: white; border-left-color: white; border-right-color: white; border-bottom-width: 2px; border-style:solid;")
        self.phoneBox.setObjectName("phoneBox")
        self.phoneBox.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('\d{7,10}')))

        self.emailLabel = QtWidgets.QLabel(createAffiliate)
        self.emailLabel.setGeometry(QtCore.QRect(95, 368, 261, 17))
        self.emailLabel.setStyleSheet("color: rgb(136, 136, 136);")
        self.emailLabel.setObjectName("emailLabel")

        self.emailBox = QtWidgets.QLineEdit(createAffiliate)
        self.emailBox.setGeometry(QtCore.QRect(95, 380, 261, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.emailBox.setFont(font)
        self.emailBox.setStyleSheet("border-top-color: white; border-left-color: white; border-right-color: white; border-bottom-width: 2px; border-style:solid;")
        self.emailBox.setObjectName("emailBox")
        self.emailBox.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$')))

        self.cityLabel = QtWidgets.QLabel(createAffiliate)
        self.cityLabel.setGeometry(QtCore.QRect(95, 428, 261, 17))
        self.cityLabel.setStyleSheet("color: rgb(136, 136, 136);")
        self.cityLabel.setObjectName("cityLabel")

        self.cityBox = QtWidgets.QLineEdit(createAffiliate)
        self.cityBox.setGeometry(QtCore.QRect(95, 440, 261, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cityBox.setFont(font)
        self.cityBox.setStyleSheet("border-top-color: white; border-left-color: white; border-right-color: white; border-bottom-width: 2px; border-style:solid;")
        self.cityBox.setObjectName("cityBox")
        self.cityBox.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[a-zA-Z ñáéíóú]{1,20}')))

        self.birthDateLabel = QtWidgets.QLabel(createAffiliate)
        self.birthDateLabel.setGeometry(QtCore.QRect(95, 497, 111, 14))
        self.birthDateLabel.setStyleSheet("color: rgb(136, 136, 136);")
        self.birthDateLabel.setObjectName("birthDateLabel")
        self.affiliationDateLabel = QtWidgets.QLabel(createAffiliate)
        self.affiliationDateLabel.setGeometry(QtCore.QRect(95, 568, 111, 14))
        self.affiliationDateLabel.setStyleSheet("color: rgb(136, 136, 136);")
        self.affiliationDateLabel.setObjectName("affiliationDateLabel")

        self.createButton = QtWidgets.QPushButton(createAffiliate)
        self.createButton.setGeometry(QtCore.QRect(125, 660, 210, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.createButton.setFont(font)
        self.createButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.createButton.setStyleSheet("background-color: rgb(72, 72, 72); color: rgb(255, 255, 255);")
        self.createButton.setObjectName("createButton")
        self.createButton.clicked.connect(self.onCreateButton)

        self.birthDate = QtWidgets.QDateEdit(createAffiliate)
        self.birthDate.setGeometry(QtCore.QRect(95, 510, 111, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.birthDate.setFont(font)
        self.birthDate.setStyleSheet("border-top-color: white; border-left-color: white; border-right-color: white; border-bottom-width: 2px; border-style:solid;")
        self.birthDate.setObjectName("birthDate")
        
        
        self.affiliationDate = QtWidgets.QDateEdit(createAffiliate)
        self.affiliationDate.setGeometry(QtCore.QRect(95, 580, 111, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.affiliationDate.setFont(font)
        self.affiliationDate.setStyleSheet("border-top-color: white; border-left-color: white; border-right-color: white; border-bottom-width: 2px; border-style:solid;")
        self.affiliationDate.setObjectName("affiliationDate")

        self.create_afiliate_card_bg = QtWidgets.QFrame(createAffiliate)
        self.create_afiliate_card_bg.setGeometry(QtCore.QRect(25, 20, 400, 731))
        self.create_afiliate_card_bg.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 12;")
        self.create_afiliate_card_bg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.create_afiliate_card_bg.setFrameShadow(QtWidgets.QFrame.Plain)
        self.create_afiliate_card_bg.setObjectName("create_afiliate_card_bg")

        # LAYER ORDER
        self.create_afiliate_card_bg.raise_()
        self.idBox.raise_()
        self.nameBox.raise_()
        self.lastNameBox.raise_()
        self.directionBox.raise_()
        self.phoneBox.raise_()
        self.emailBox.raise_()
        self.cityBox.raise_()
        self.createButton.raise_()
        self.birthDate.raise_()
        self.affiliationDate.raise_()
        self.idLabel.raise_()
        self.lastNameLabel.raise_()
        self.nameLabel.raise_()
        self.directionLabel.raise_()
        self.phoneLabel.raise_()
        self.emailLabel.raise_()
        self.cityLabel.raise_()
        self.birthDateLabel.raise_()
        self.affiliationDateLabel.raise_()

        self.retranslateUi(createAffiliate)
        QtCore.QMetaObject.connectSlotsByName(createAffiliate)

    def retranslateUi(self, createAffiliate):
        _translate = QtCore.QCoreApplication.translate
        createAffiliate.setWindowTitle(_translate("createAffiliate", "Crear afiliado"))
        self.idLabel.setText(_translate("createAffiliate", "Número de Identificación"))
        self.idBox.setPlaceholderText(_translate("createAffiliate", "0000000000"))
        self.nameLabel.setText(_translate("createAffiliate", "Nombres"))
        self.nameBox.setPlaceholderText(_translate("createAffiliate", "John"))
        self.lastNameLabel.setText(_translate("createAffiliate", "Apellidos"))
        self.lastNameBox.setPlaceholderText(_translate("createAffiliate", "Doe"))
        self.directionLabel.setText(_translate("createAffiliate", "Dirección"))
        self.directionBox.setPlaceholderText(_translate("createAffiliate", "CL 00 # 00 - 00"))
        self.phoneLabel.setText(_translate("createAffiliate", "Teléfono"))
        self.phoneBox.setPlaceholderText(_translate("createAffiliate", "1234567890"))
        self.emailLabel.setText(_translate("createAffiliate", "Email"))
        self.emailBox.setPlaceholderText(_translate("createAffiliate", "johndoe@email.com"))
        self.cityLabel.setText(_translate("createAffiliate", "Ciudad"))
        self.cityBox.setPlaceholderText(_translate("createAffiliate", "Bogotá"))
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
