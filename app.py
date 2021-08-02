from PyQt5 import QtCore, QtGui, QtWidgets

# from the interface directory we import the main ui elements created out of qt classes
from interface import mainMenu
from interface import allVaccinationSchedule, affiliateVaccinationSchedule, createSchedule, vaccineLotFind
from interface import vaccinationPlanFind, affiliateFind, createVaccinationPlan, createVaccineLot
from interface import createAffiliate, vaccinate
import sys

# initializing class ui methods
uiMainMenu = None
uiAllVaccinationSchedule = None
uiAffiliateVaccinationSchedule = None
uiCreateVaccinationSchedule = None
uiVaccineLotFind = None
uiVaccinationPlanFind = None
uiAffiliateFind = None
uiCreateVaccinationPlan = None
uiCreateVaccineLot = None
uiCreateAffiliate = None
uiVaccinate = None

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

# The QDialog class is the base class of dialog windows which is a temporary window an application creates to retrieve user input.
# So all the affiliates, vaccine lot, vaccination plan and vaccionation schedule methods at the UI space are displayed as dialog boxes.
allVaccinationScheduleWindow = QtWidgets.QDialog()
affiliateVaccinationScheduleWindow = QtWidgets.QDialog()
createVaccinationScheduleWindow = QtWidgets.QDialog()
vaccineLotFindWindow = QtWidgets.QDialog()
vaccinationPlanFindWindow = QtWidgets.QDialog()
affiliateFindWindow = QtWidgets.QDialog()
createVaccinationPlanWindow = QtWidgets.QDialog()
createVaccineLotWindow = QtWidgets.QDialog()
createAffiliateWindow = QtWidgets.QDialog()
vaccinateWindow = QtWidgets.QDialog()

# once initialized at the name = main
def openAllVaccinationSchedule():
    # goes to the AllVaccinationSchedule module and executes the updateTable method which is mainly a refresh of ui
    uiAllVaccinationSchedule.updateTable()
    # showcases the updated table
    allVaccinationScheduleWindow.show()

# showcases the affiliate VaccinationSchedule window section
def openAffiliateVaccinationSchedule():
    affiliateVaccinationScheduleWindow.show()

# showcases the create vaccination schedule window
def openCreateVaccinationSchedule():
    createVaccinationScheduleWindow.show()

# showcases the "find vaccine lot" window from the vaccine lot section
def openVaccineLotFind():
    vaccineLotFindWindow.show()

# showcases the "find vaccination plan" from the vaccination plan section
def openVaccinationPlanFind():
    vaccinationPlanFindWindow.show()

# showcases the "find affiliate" from the affiliate section
def openAffiliateFind():
    affiliateFindWindow.show()

# showcases the vaccination plan creation window
def openCreateVaccinationPlan():
    createVaccinationPlanWindow.show()

# showcases the create vaccine lot from the vaccinelot section
def openCreateVaccineLot():
    createVaccineLotWindow.show()

# showcases the affiliate creation window from the affiliate section
def openCreateAffiliate():
    createAffiliateWindow.show()

# showcases the vaccinate option window from the affiliate section
def openVaccinate():
    vaccinateWindow.show()

# once called it displays an error message that depends on the element being used
def showError(message):
    errorMessage.setInformativeText(message)
    errorMessage.show()

# showcases an informative box when everything went ok, it depends on the module being used
def showSuccess(message):
    successMessage.setInformativeText(message)
    successMessage.show()


# ui initialization starts here
if __name__ == "__main__":
    
    # associates uiMainMenu with the creation of the main window element
    uiMainMenu = mainMenu.MainMenu()
    uiMainMenu.setupUi(mainMenuWindow)
    
    # associates uiAllVaccinationSchedule with the module allVaccinationSchedule and its initialization
    uiAllVaccinationSchedule = allVaccinationSchedule.AllVaccinationSchedule()
    uiAllVaccinationSchedule.setupUi(allVaccinationScheduleWindow)
    
    # associates uiAffiliateVaccinationSchedule with the ui module affiliateVaccinationSchedule and its initialization
    uiAffiliateVaccinationSchedule = affiliateVaccinationSchedule.AffiliateVaccinationSchedule()
    uiAffiliateVaccinationSchedule.setupUi(affiliateVaccinationScheduleWindow)
    
    # associates uiCreateVaccinationSchedule with the createSchedule ui module and it include as well the methods for error management
    uiCreateVaccinationSchedule = createSchedule.CreateSchedule()
    uiCreateVaccinationSchedule.setupUi(createVaccinationScheduleWindow)
    uiCreateVaccinationSchedule.showErrorMessage = showError
    uiCreateVaccinationSchedule.showSuccessMessage = showSuccess

    # initializes uiVaccineLotFind via vaccineLotFind ui module
    uiVaccineLotFind = vaccineLotFind.VaccineLotFind()
    uiVaccineLotFind.setupUi(vaccineLotFindWindow)

    # initializes uiVaccinationPlanFind as vaccinationPlanFind ui module
    uiVaccinationPlanFind = vaccinationPlanFind.VaccinationPlanFind()
    uiVaccinationPlanFind.setupUi(vaccinationPlanFindWindow)

    # initializes uiAffiliateFind as affiliate Find ui module
    uiAffiliateFind = affiliateFind.AffiliateFind()
    uiAffiliateFind.setupUi(affiliateFindWindow)

    # associates uiCreateVaccinationPlan with the ui module for creating a vaccination plan
    uiCreateVaccinationPlan = createVaccinationPlan.CreateVaccinationPlan()
    uiCreateVaccinationPlan.setupUi(createVaccinationPlanWindow)
    uiCreateVaccinationPlan.showErrorMessage = showError
    uiCreateVaccinationPlan.showSuccessMessage = showSuccess

    # associates uiCreateVaccineLot with the ui module for creating a vaccine lot, it also adds error management
    uiCreateVaccineLot = createVaccineLot.CreateVaccineLot()
    uiCreateVaccineLot.setupUi(createVaccineLotWindow)
    uiCreateVaccineLot.showErrorMessage = showError
    uiCreateVaccineLot.showSuccessMessage = showSuccess

    # associates uiCreateAffiliate with the ui module for creating an affiliate; it also adds some error management 
    uiCreateAffiliate = createAffiliate.CreateAffiliate()
    uiCreateAffiliate.setupUi(createAffiliateWindow)
    uiCreateAffiliate.showErrorMessage = showError
    uiCreateAffiliate.showSuccessMessage = showSuccess

    # it associates uiVaccinate with the vaccinate ui module and does some error management in the form of informative events boxes
    uiVaccinate = vaccinate.Vaccinate()
    uiVaccinate.setupUi(vaccinateWindow)
    uiVaccinate.showErrorMessage = showError
    uiVaccinate.showSuccessMessage = showSuccess

    # once every element has been initialized appropietly, it showcases the main window
    mainMenuWindow.show()

    # as per ui module, every argument asociate with its following ui module is initialized so for example the uiMainMenu now a mainMenu element has an openCreateAffiliate method which its now initialized as a dialog box and it's now treated as an unique object within the mainMenu, it's a way of association between all the ui layers - cohesion.
    uiMainMenu.openAllVaccinationSchedule = openAllVaccinationSchedule
    uiMainMenu.openAffiliateVaccinationSchedule = openAffiliateVaccinationSchedule
    uiMainMenu.openCreateVaccinationSchedule = openCreateVaccinationSchedule
    uiMainMenu.openVaccineLotFind = openVaccineLotFind
    uiMainMenu.openVaccinationPlanFind = openVaccinationPlanFind
    uiMainMenu.openAffiliateFind = openAffiliateFind
    uiMainMenu.openCreateVaccinationPlan = openCreateVaccinationPlan
    uiMainMenu.openCreateVaccineLot = openCreateVaccineLot
    uiMainMenu.openCreateAffiliate = openCreateAffiliate
    uiMainMenu.openVaccinate = openVaccinate

    sys.exit(app.exec_())
    