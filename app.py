from PyQt5 import QtCore, QtGui, QtWidgets
from interface import mainMenu
from interface import allVaccinationSchedule
from interface import affiliateVaccinationSchedule
from interface import createSchedule
import sys

uiMainMenu = None
uiAllVaccinationSchedule = None
uiAffiliateVaccinationSchedule = None
uiCreateVaccinationSchedule = None

app = QtWidgets.QApplication(sys.argv)

errorMessage = QtWidgets.QMessageBox()
errorMessage.setIcon(QtWidgets.QMessageBox.Critical)
errorMessage.setText("Error")
errorMessage.setWindowTitle("Error")

successMessage = QtWidgets.QMessageBox()
successMessage.setIcon(QtWidgets.QMessageBox.Information)
successMessage.setText("Éxito")
successMessage.setWindowTitle("Éxito")

mainMenuWindow = QtWidgets.QMainWindow()
allVaccinationScheduleWindow = QtWidgets.QDialog()
affiliateVaccinationScheduleWindow = QtWidgets.QDialog()
createVaccinationScheduleWindow = QtWidgets.QDialog()

def openAllVaccinationSchedule():
    allVaccinationScheduleWindow.show()

def openAffiliateVaccinationSchedule():
    affiliateVaccinationScheduleWindow.show()

def openCreateVaccinationSchedule():
    createVaccinationScheduleWindow.show()

def showError(message):
    errorMessage.setInformativeText(message)
    errorMessage.show()

def showSuccess(message):
    successMessage.setInformativeText(message)
    successMessage.show()

if __name__ == "__main__":
    uiMainMenu = mainMenu.MainMenu()
    uiMainMenu.setupUi(mainMenuWindow)
    uiAllVaccinationSchedule = allVaccinationSchedule.AllVaccinationSchedule()
    uiAllVaccinationSchedule.setupUi(allVaccinationScheduleWindow)
    uiAffiliateVaccinationSchedule = affiliateVaccinationSchedule.AffiliateVaccinationSchedule()
    uiAffiliateVaccinationSchedule.setupUi(affiliateVaccinationScheduleWindow)
    uiCreateVaccinationSchedule = createSchedule.CreateSchedule()
    uiCreateVaccinationSchedule.setupUi(createVaccinationScheduleWindow)
    uiCreateVaccinationSchedule.showErrorMessage = showError
    uiCreateVaccinationSchedule.showSuccessMessage = showSuccess

    mainMenuWindow.show()

    uiMainMenu.openAllVaccinationSchedule = openAllVaccinationSchedule
    uiMainMenu.openAffiliateVaccinationSchedule = openAffiliateVaccinationSchedule
    uiMainMenu.openCreateVaccinationSchedule = openCreateVaccinationSchedule
    sys.exit(app.exec_())