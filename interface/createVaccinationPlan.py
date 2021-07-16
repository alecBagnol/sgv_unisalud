from PyQt5 import QtCore, QtGui, QtWidgets
from modules import vaccination_plan

class CreateVaccinationPlan(object):

    showErrorMessage = None
    showSuccessMessage = None
    manager = vaccination_plan.VaccinationPlanManager()


    def setupUi(self, createVaccinationPlan):
        createVaccinationPlan.setObjectName("createVaccinationPlan")
        createVaccinationPlan.resize(358, 460)
        self.idLabel = QtWidgets.QLabel(createVaccinationPlan)
        self.idLabel.setGeometry(QtCore.QRect(20, 30, 241, 17))
        self.idLabel.setObjectName("idLabel")
        self.idInputLine = QtWidgets.QLineEdit(createVaccinationPlan)
        self.idInputLine.setGeometry(QtCore.QRect(20, 50, 281, 31))
        self.idInputLine.setObjectName("idInputLine")
        self.idInputLine.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('\d{1,2}')))
        self.minimumAgeSpinBox = QtWidgets.QSpinBox(createVaccinationPlan)
        self.minimumAgeSpinBox.setGeometry(QtCore.QRect(20, 130, 48, 26))
        self.minimumAgeSpinBox.setMaximum(200)
        self.minimumAgeSpinBox.setObjectName("minimumAgeSpinBox")
        self.minimumAgeLabel = QtWidgets.QLabel(createVaccinationPlan)
        self.minimumAgeLabel.setGeometry(QtCore.QRect(20, 110, 241, 17))
        self.minimumAgeLabel.setObjectName("minimumAgeLabel")
        self.maximumAgeLabel = QtWidgets.QLabel(createVaccinationPlan)
        self.maximumAgeLabel.setGeometry(QtCore.QRect(20, 180, 241, 17))
        self.maximumAgeLabel.setObjectName("maximumAgeLabel")
        self.maximumAgeSpinBox = QtWidgets.QSpinBox(createVaccinationPlan)
        self.maximumAgeSpinBox.setGeometry(QtCore.QRect(20, 200, 48, 26))
        self.maximumAgeSpinBox.setMaximum(200)
        self.maximumAgeSpinBox.setObjectName("maximumAgeSpinBox")
        self.firstDate = QtWidgets.QDateEdit(createVaccinationPlan)
        self.firstDate.setGeometry(QtCore.QRect(20, 270, 110, 26))
        self.firstDate.setObjectName("firstDate")
        self.firstDateLabel = QtWidgets.QLabel(createVaccinationPlan)
        self.firstDateLabel.setGeometry(QtCore.QRect(20, 250, 241, 17))
        self.firstDateLabel.setObjectName("firstDateLabel")
        self.lastDate = QtWidgets.QDateEdit(createVaccinationPlan)
        self.lastDate.setGeometry(QtCore.QRect(20, 340, 110, 26))
        self.lastDate.setObjectName("lastDate")
        self.lastDateLabel = QtWidgets.QLabel(createVaccinationPlan)
        self.lastDateLabel.setGeometry(QtCore.QRect(20, 320, 241, 17))
        self.lastDateLabel.setObjectName("lastDateLabel")
        self.createButton = QtWidgets.QPushButton(createVaccinationPlan)
        self.createButton.setGeometry(QtCore.QRect(130, 400, 89, 25))
        self.createButton.setObjectName("createButton")
        self.createButton.clicked.connect(self.onButtonClicked)

        self.retranslateUi(createVaccinationPlan)
        QtCore.QMetaObject.connectSlotsByName(createVaccinationPlan)

    def retranslateUi(self, createVaccinationPlan):
        _translate = QtCore.QCoreApplication.translate
        createVaccinationPlan.setWindowTitle(_translate("createVaccinationPlan", "Crear Plan"))
        self.idLabel.setText(_translate("createVaccinationPlan", "Número de Identificación del Plan"))
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
            self.showErrorMessage("Fecha de inicio y finalización invalidas")
            return
        if minAge > maxAge:
            self.showErrorMessage("Edad mínima y máxima invalida")
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
        
