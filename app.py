from PyQt5 import QtCore, QtGui, QtWidgets
from interface import mainMenu
from interface import allVaccinationSchedule
from interface import affiliateVaccinationSchedule
import sys

uiMainMenu = None
uiAllVaccinationSchedule = None
uiAffiliateVaccinationSchedule = None

app = QtWidgets.QApplication(sys.argv)

mainMenuWindow = QtWidgets.QMainWindow()
allVaccinationScheduleWindow = QtWidgets.QDialog()
affiliateVaccinationScheduleWindow = QtWidgets.QDialog()

def openAllVaccinationSchedule():
    allVaccinationScheduleWindow.show()

def openAffiliateVaccinationSchedule():
    affiliateVaccinationScheduleWindow.show()

if __name__ == "__main__":
    uiMainMenu = mainMenu.MainMenu()
    uiMainMenu.setupUi(mainMenuWindow)
    uiAllVaccinationSchedule = allVaccinationSchedule.AllVaccinationSchedule()
    uiAllVaccinationSchedule.setupUi(allVaccinationScheduleWindow)
    uiAffiliateVaccinationSchedule = affiliateVaccinationSchedule.AffiliateVaccinationSchedule()
    uiAffiliateVaccinationSchedule.setupUi(affiliateVaccinationScheduleWindow)
    
    
    mainMenuWindow.show()
    uiMainMenu.openAllVaccinationSchedule = openAllVaccinationSchedule
    uiMainMenu.openAffiliateVaccinationSchedule = openAffiliateVaccinationSchedule
    sys.exit(app.exec_())