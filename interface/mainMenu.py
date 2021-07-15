from PyQt5 import QtCore, QtGui, QtWidgets
from interface import utils

class MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Colombia))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 207, 291))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.menuList = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.menuList.setContentsMargins(0, 0, 0, 0)
        self.menuList.setObjectName("menuList")
        self.affiliateButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.affiliateButton.setObjectName("affiliateButton")
        self.menuList.addWidget(self.affiliateButton)
        self.affiliateButton.clicked.connect(self.onAffiliateButtonClicked)
        self.vaccineLotButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.vaccineLotButton.setObjectName("vaccineLotButton")
        self.menuList.addWidget(self.vaccineLotButton)
        self.vaccineLotButton.clicked.connect(self.onVaccineLotButtonClicked)
        self.vaccinationPlanButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.vaccinationPlanButton.setObjectName("vaccinationPlanButton")
        self.menuList.addWidget(self.vaccinationPlanButton)
        self.vaccinationPlanButton.clicked.connect(self.onVaccinationPlanButtonClicked)
        self.vaccinationScheduleButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.vaccinationScheduleButton.setObjectName("vaccinationScheduleButton")
        self.menuList.addWidget(self.vaccinationScheduleButton)
        self.vaccinationScheduleButton.clicked.connect(self.onVaccinationScheduleButtonClicked)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(350, 30, 301, 311))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.menuOptionList = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.menuOptionList.setContentsMargins(0, 0, 0, 0)
        self.menuOptionList.setObjectName("menuOptionList")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sgv Salud"))
        self.affiliateButton.setText(_translate("MainWindow", "Afiliados"))
        self.vaccineLotButton.setText(_translate("MainWindow", "Lotes de Vacunas"))
        self.vaccinationPlanButton.setText(_translate("MainWindow", "Planes de Vacunación"))
        self.vaccinationScheduleButton.setText(_translate("MainWindow", "Programación de Vacunación"))

    def onAffiliateButtonClicked(self):
        utils.clearLayout(self.menuOptionList)
        _translate = QtCore.QCoreApplication.translate
        
        add = QtWidgets.QPushButton(self.verticalLayoutWidget)
        add.setObjectName("add")
        add.setText(_translate("MainWindow", "Crear Afiliado"))
        self.menuOptionList.addWidget(add)

        find = QtWidgets.QPushButton(self.verticalLayoutWidget)
        find.setObjectName("find")
        find.setText(_translate("MainWindow", "Consultar Afiliado"))
        self.menuOptionList.addWidget(find)
        
        vaccinate = QtWidgets.QPushButton(self.verticalLayoutWidget)
        vaccinate.setObjectName("vaccinate")
        vaccinate.setText(_translate("MainWindow", "Vacunación de Afiliado"))
        self.menuOptionList.addWidget(vaccinate)

    def onVaccineLotButtonClicked(self):
        utils.clearLayout(self.menuOptionList)
        _translate = QtCore.QCoreApplication.translate
        
        add = QtWidgets.QPushButton(self.verticalLayoutWidget)
        add.setObjectName("add")
        add.setText(_translate("MainWindow", "Agregar Lote"))
        self.menuOptionList.addWidget(add)

        find = QtWidgets.QPushButton(self.verticalLayoutWidget)
        find.setObjectName("find")
        find.setText(_translate("MainWindow", "Consultar Lote"))
        self.menuOptionList.addWidget(find)
        
    def onVaccinationPlanButtonClicked(self):
        utils.clearLayout(self.menuOptionList)
        _translate = QtCore.QCoreApplication.translate
        
        add = QtWidgets.QPushButton(self.verticalLayoutWidget)
        add.setObjectName("add")
        add.setText(_translate("MainWindow", "Crear Plan de Vacunación"))
        self.menuOptionList.addWidget(add)

        find = QtWidgets.QPushButton(self.verticalLayoutWidget)
        find.setObjectName("find")
        find.setText(_translate("MainWindow", "Consultar Plan de Vacunación"))
        self.menuOptionList.addWidget(find)

    def onVaccinationScheduleButtonClicked(self):
        utils.clearLayout(self.menuOptionList)
        _translate = QtCore.QCoreApplication.translate
        
        add = QtWidgets.QPushButton(self.verticalLayoutWidget)
        add.setObjectName("add")
        add.setText(_translate("MainWindow", "Crear Programación"))
        self.menuOptionList.addWidget(add)

        find = QtWidgets.QPushButton(self.verticalLayoutWidget)
        find.setObjectName("find")
        find.setText(_translate("MainWindow", "Consultar Programación"))
        self.menuOptionList.addWidget(find)
        
        findAffiliate = QtWidgets.QPushButton(self.verticalLayoutWidget)
        findAffiliate.setObjectName("findAffiliate")
        findAffiliate.setText(_translate("MainWindow", "Consultar Programación de Afiliado"))
        self.menuOptionList.addWidget(findAffiliate)