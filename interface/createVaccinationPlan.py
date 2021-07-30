from PyQt5 import QtCore, QtGui, QtWidgets
from modules import vaccination_plan

class CreateVaccinationPlan(object):

    showErrorMessage = None
    showSuccessMessage = None
    manager = vaccination_plan.VaccinationPlanManager()

    def setupUi(self, createVaccinationPlan):
        createVaccinationPlan.setObjectName("createVaccinationPlan")
        createVaccinationPlan.resize(450, 600)
        self.idLabel = QtWidgets.QLabel(createVaccinationPlan)
        self.idLabel.setGeometry(QtCore.QRect(90, 80, 281, 17))
        self.idLabel.setStyleSheet("color: rgb(136, 136, 136);")
        self.idLabel.setObjectName("idLabel")
        self.idInputLine = QtWidgets.QLineEdit(createVaccinationPlan)
        self.idInputLine.setGeometry(QtCore.QRect(90, 95, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.idInputLine.setFont(font)
        self.idInputLine.setStyleSheet("border-top-color: white; border-left-color: white; border-right-color: white; border-bottom-width: 2px; border-style:solid;")
        self.idInputLine.setObjectName("idInputLine")
        self.idInputLine.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('\d{1,2}')))
        self.minimumAgeSpinBox = QtWidgets.QSpinBox(createVaccinationPlan)
        self.minimumAgeSpinBox.setGeometry(QtCore.QRect(90, 170, 81, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.minimumAgeSpinBox.setFont(font)
        self.minimumAgeSpinBox.setStyleSheet("border-top-color: white; border-left-color: white; border-right-color: white; border-bottom-width: 2px; border-style:solid;")
        self.minimumAgeSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.minimumAgeSpinBox.setMaximum(200)
        self.minimumAgeSpinBox.setObjectName("minimumAgeSpinBox")
        self.minimumAgeLabel = QtWidgets.QLabel(createVaccinationPlan)
        self.minimumAgeLabel.setGeometry(QtCore.QRect(90, 150, 81, 17))
        self.minimumAgeLabel.setStyleSheet("color: rgb(136, 136, 136);")
        self.minimumAgeLabel.setObjectName("minimumAgeLabel")
        self.maximumAgeLabel = QtWidgets.QLabel(createVaccinationPlan)
        self.maximumAgeLabel.setGeometry(QtCore.QRect(90, 220, 81, 17))
        self.maximumAgeLabel.setStyleSheet("color: rgb(136, 136, 136);")
        self.maximumAgeLabel.setObjectName("maximumAgeLabel")
        self.maximumAgeSpinBox = QtWidgets.QSpinBox(createVaccinationPlan)
        self.maximumAgeSpinBox.setGeometry(QtCore.QRect(90, 240, 81, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.maximumAgeSpinBox.setFont(font)
        self.maximumAgeSpinBox.setStyleSheet("border-top-color: white; border-left-color: white; border-right-color: white; border-bottom-width: 2px; border-style:solid;")
        self.maximumAgeSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.maximumAgeSpinBox.setMaximum(200)
        self.maximumAgeSpinBox.setObjectName("maximumAgeSpinBox")
        self.firstDate = QtWidgets.QDateEdit(createVaccinationPlan)
        self.firstDate.setGeometry(QtCore.QRect(90, 310, 141, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.firstDate.setFont(font)
        self.firstDate.setStyleSheet("border-top-color: white; border-left-color: white; border-right-color: white; border-bottom-width: 2px; border-style:solid;")
        self.firstDate.setAlignment(QtCore.Qt.AlignCenter)
        self.firstDate.setObjectName("firstDate")
        self.firstDateLabel = QtWidgets.QLabel(createVaccinationPlan)
        self.firstDateLabel.setGeometry(QtCore.QRect(90, 290, 141, 17))
        self.firstDateLabel.setStyleSheet("color: rgb(136, 136, 136);")
        self.firstDateLabel.setObjectName("firstDateLabel")
        self.lastDate = QtWidgets.QDateEdit(createVaccinationPlan)
        self.lastDate.setGeometry(QtCore.QRect(90, 380, 141, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lastDate.setFont(font)
        self.lastDate.setStyleSheet("border-top-color: white; border-left-color: white; border-right-color: white; border-bottom-width: 2px; border-style:solid;")
        self.lastDate.setAlignment(QtCore.Qt.AlignCenter)
        self.lastDate.setObjectName("lastDate")
        self.lastDateLabel = QtWidgets.QLabel(createVaccinationPlan)
        self.lastDateLabel.setGeometry(QtCore.QRect(90, 360, 141, 17))
        self.lastDateLabel.setStyleSheet("color: rgb(136, 136, 136);")
        self.lastDateLabel.setObjectName("lastDateLabel")
        self.createButton = QtWidgets.QPushButton(createVaccinationPlan)
        self.createButton.setGeometry(QtCore.QRect(130, 480, 210, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.createButton.setFont(font)
        self.createButton.setStyleSheet("background-color: rgb(72, 72, 72); color: rgb(255, 255, 255);")
        self.createButton.setObjectName("createButton")
        self.createButton.clicked.connect(self.onButtonClicked)
        self.card_bg = QtWidgets.QFrame(createVaccinationPlan)
        self.card_bg.setGeometry(QtCore.QRect(25, 25, 400, 550))
        self.card_bg.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 12;")
        self.card_bg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card_bg.setFrameShadow(QtWidgets.QFrame.Plain)
        self.card_bg.setObjectName("card_bg")
        self.card_bg.raise_()
        self.idInputLine.raise_()
        self.minimumAgeSpinBox.raise_()
        self.minimumAgeLabel.raise_()
        self.maximumAgeLabel.raise_()
        self.maximumAgeSpinBox.raise_()
        self.firstDate.raise_()
        self.firstDateLabel.raise_()
        self.lastDate.raise_()
        self.lastDateLabel.raise_()
        self.createButton.raise_()
        self.idLabel.raise_()

        self.retranslateUi(createVaccinationPlan)
        QtCore.QMetaObject.connectSlotsByName(createVaccinationPlan)

    def retranslateUi(self, createVaccinationPlan):
        _translate = QtCore.QCoreApplication.translate
        createVaccinationPlan.setWindowTitle(_translate("createVaccinationPlan", "Crear Plan"))
        self.idLabel.setText(_translate("createVaccinationPlan", "Número de Identificación del Plan"))
        self.idInputLine.setPlaceholderText(_translate("createVaccinationPlan", "0000000000"))
        self.minimumAgeLabel.setText(_translate("createVaccinationPlan", "Edad Mínima"))
        self.maximumAgeLabel.setText(_translate("createVaccinationPlan", "Edad Máxima"))
        self.firstDate.setDisplayFormat(_translate("createVaccinationPlan", "d/M/yyyy"))
        self.firstDateLabel.setText(_translate("createVaccinationPlan", "Fecha de Inicio del Plan"))
        self.lastDate.setDisplayFormat(_translate("createVaccinationPlan", "d/M/yyyy"))
        self.lastDateLabel.setText(_translate("createVaccinationPlan", "Fecha de Finalización del Plan"))
        self.createButton.setText(_translate("createVaccinationPlan", "Crear"))

    def onButtonClicked(self):
        startDate = int(self.firstDate.dateTime().toPyDateTime().timestamp())
        endDate = int(self.lastDate.dateTime().toPyDateTime().timestamp())
        minAge = self.minimumAgeSpinBox.value()
        maxAge = self.maximumAgeSpinBox.value()
        if startDate >= endDate:
            self.showErrorMessage("Fecha de inicio y finalización inválidas")
            return
        if minAge > maxAge:
            self.showErrorMessage("Edad mínima y máxima inválida")
            return

        if self.idInputLine.text() == "":
            self.showErrorMessage("Ingrese Número de Identificación")
            return
            
        planId = int(self.idInputLine.text())
        plan = self.manager.consult_vaccination_plan(int(planId))
        if bool(plan):
            self.showErrorMessage("Número de Identificación del Plan ya existe")
            return
        
        res = self.manager.create_vaccination_plan(vaccination_plan.VaccinationPlan(planId, minAge, maxAge, startDate, endDate))

        if not res:
            self.showErrorMessage('Plan de vacunación no creado: una de las edades se solapa con las edades de un plan de vacunación ya existente')
        else:
            self.showSuccessMessage('Plan de vacunación creado con éxito')

