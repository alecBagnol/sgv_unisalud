# sys provides various functions and variables that are used to manipulate different parts of the Python runtime environment
import sys

# GUI toolkit module
from PyQt5 import QtCore, QtGui, QtWidgets

# imports the vaccine lot methods
from modules import vaccine_lot

# LIBS TO MANAGE IMAGE FILES IN ORDER TO SET A CORRECT IMAGE COLOR SPACE
    # io module allows us to manage the file-related input and output operations
import io
    # PIL is a Imaging Library that adds image processing capabilities to Python
from PIL import Image, ImageCms



    # DESCRIPTION:
        # This class (CreateVaccineLot) contains and builds up the vaccine lot creation window. It was created mainly via Qt designer 

    # ARGUMENTS:
        # UI elements are created using Qt methods.
            # - createVaccineLot: setup window creation.
            # - mainLotWidget: creates a widget within.
            # - inputLotId: one-line text field to capture lot id.
            # - lotId: displays label for input lot id.
            # - manufacturerBox: drop down box for manufacturer selection.
            # - manufacturerLabel: label for manufacturer box.
            # - vaccineTypeBox: dropdown for selecting vaccine type.
            # - vaccineTypeLabel: label for vaccine type box.
            # - unitsAmountBox: spinner control for the amount of vaccines being created.
            # - unitsAmountlabel: label for unitsAmountBox.
            # - doseBox: spinner control for setting up the number of doses needed per vaccine created.
            # - doseLabel: label for doseBox.
            # - temperatureBox: spinner control for setting up the storage vaccine temperature.
            # - temperatureLabel: label for temperatureBox.
            # - effectivenessBox: spinner control for setting up the vaccine effectiveness.
            # - effectivenessLabel: label for effectivenessBox.
            # - protectionTimeBox: spinner control for setting up the vaccine protection span.
            # - protectionTimeLabel: label for protectionTimeBox.
            # - dateBox: qt date field for setting up vaccine expiration date.
            # - dateLabel: label for dateBox.
            # - frame: defined layout for the image box section
            # - openImg: button that sets the function for opening a browse window.
            # - imagePreview: element that displays the vaccine lot image .
            # - imageLabel: label for imagePreview.
            # - imageBox: field that displays the name of the selected image.
            # - card_bg: frame that sets background color for the card section.
            # - createButton: button that calls on click the function to create and deploy the vaccine lot info into the database.

            

class CreateVaccineLot(object):

    showErrorMessage = None
    showSuccessMessage = None
    manager = vaccine_lot.VaccineLotManager()

    def setupUi(self, createVaccineLot):

        self.image_url = ""

        createVaccineLot.setObjectName("createVaccineLot")
        createVaccineLot.resize(450, 768)
        createVaccineLot.setMinimumSize(QtCore.QSize(0, 768))
        createVaccineLot.setMaximumSize(QtCore.QSize(16777215, 768))

        self.mainLotWidget = QtWidgets.QWidget(createVaccineLot)
        self.mainLotWidget.setObjectName("mainLotWidget")

        self.inputLotId = QtWidgets.QLineEdit(createVaccineLot)
        self.inputLotId.setGeometry(QtCore.QRect(50, 300, 160, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inputLotId.setFont(font)
        self.inputLotId.setStyleSheet("border-top-color: white; border-left-color: white; border-right-color: white; border-bottom-width: 2px; border-style:solid;")
        self.inputLotId.setText("")
        self.inputLotId.setObjectName("inputLotId")
        self.inputLotId.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('\d{1,12}')))

        self.lotId = QtWidgets.QLabel(createVaccineLot)
        self.lotId.setGeometry(QtCore.QRect(50, 289, 160, 17))
        self.lotId.setStyleSheet("color: rgb(136, 136, 136);")
        self.lotId.setObjectName("lotId")
        self.manufacturerBox = QtWidgets.QComboBox(createVaccineLot)
        self.manufacturerBox.setGeometry(QtCore.QRect(240, 300, 160, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.manufacturerBox.setFont(font)
        self.manufacturerBox.setStyleSheet("border-top-color: white; border-left-color: white; border-right-color: white; border-bottom-width: 2px; border-style:solid;")
        self.manufacturerBox.setObjectName("manufacturerBox")
        self.manufacturerBox.addItem("")
        self.manufacturerBox.addItem("")
        self.manufacturerBox.addItem("")
        self.manufacturerBox.addItem("")
        self.manufacturerBox.addItem("")
        self.manufacturerBox.addItem("")
        self.manufacturerBox.addItem("")
        self.manufacturerLabel = QtWidgets.QLabel(createVaccineLot)
        self.manufacturerLabel.setGeometry(QtCore.QRect(240, 289, 160, 17))
        self.manufacturerLabel.setStyleSheet("color: rgb(136, 136, 136);")
        self.manufacturerLabel.setObjectName("manufacturerLabel")
        self.vaccineTypeBox = QtWidgets.QComboBox(createVaccineLot)
        self.vaccineTypeBox.setGeometry(QtCore.QRect(50, 370, 160, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.vaccineTypeBox.setFont(font)
        self.vaccineTypeBox.setStyleSheet("border-top-color: white; border-left-color: white; border-right-color: white; border-bottom-width: 2px; border-style:solid;")
        self.vaccineTypeBox.setObjectName("vaccineTypeBox")
        self.vaccineTypeBox.addItem("")
        self.vaccineTypeBox.addItem("")
        self.vaccineTypeBox.addItem("")
        self.vaccineTypeBox.addItem("")
        self.vaccineTypeLabel = QtWidgets.QLabel(createVaccineLot)
        self.vaccineTypeLabel.setGeometry(QtCore.QRect(50, 359, 160, 17))
        self.vaccineTypeLabel.setStyleSheet("color: rgb(136, 136, 136);")
        self.vaccineTypeLabel.setObjectName("vaccineTypeLabel")
        self.unitsAmountBox = QtWidgets.QSpinBox(createVaccineLot)
        self.unitsAmountBox.setGeometry(QtCore.QRect(240, 370, 111, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.unitsAmountBox.setFont(font)
        self.unitsAmountBox.setStyleSheet("border-top-color: white; border-left-color: white; border-right-color: white; border-bottom-width: 2px; border-style:solid;")
        self.unitsAmountBox.setMinimum(1)
        self.unitsAmountBox.setMaximum(999999)
        self.unitsAmountBox.setObjectName("unitsAmountBox")
        self.unitsAmountlabel = QtWidgets.QLabel(createVaccineLot)
        self.unitsAmountlabel.setGeometry(QtCore.QRect(240, 356, 111, 17))
        self.unitsAmountlabel.setStyleSheet("color: rgb(136, 136, 136);")
        self.unitsAmountlabel.setObjectName("unitsAmountlabel")
        self.doseLabel = QtWidgets.QLabel(createVaccineLot)
        self.doseLabel.setGeometry(QtCore.QRect(50, 427, 50, 17))
        self.doseLabel.setStyleSheet("color: rgb(136, 136, 136);")
        self.doseLabel.setObjectName("doseLabel")
        self.doseBox = QtWidgets.QSpinBox(createVaccineLot)
        self.doseBox.setGeometry(QtCore.QRect(50, 440, 50, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doseBox.setFont(font)
        self.doseBox.setStyleSheet("border-top-color: white; border-left-color: white; border-right-color: white; border-bottom-width: 2px; border-style:solid;")
        self.doseBox.setMinimum(1)
        self.doseBox.setMaximum(9)
        self.doseBox.setObjectName("doseBox")
        self.temperatureLabel = QtWidgets.QLabel(createVaccineLot)
        self.temperatureLabel.setGeometry(QtCore.QRect(50, 502, 120, 31))
        self.temperatureLabel.setStyleSheet("color: rgb(136, 136, 136);")
        self.temperatureLabel.setObjectName("temperatureLabel")
        self.temperatureBox = QtWidgets.QSpinBox(createVaccineLot)
        self.temperatureBox.setGeometry(QtCore.QRect(50, 530, 120, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.temperatureBox.setFont(font)
        self.temperatureBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.temperatureBox.setStyleSheet("border-top-color: white; border-left-color: white; border-right-color: white; border-bottom-width: 2px; border-style:solid;")
        self.temperatureBox.setAlignment(QtCore.Qt.AlignCenter)
        self.temperatureBox.setMinimum(-99)
        self.temperatureBox.setObjectName("temperatureBox")
        self.effectivenessLabel = QtWidgets.QLabel(createVaccineLot)
        self.effectivenessLabel.setGeometry(QtCore.QRect(240, 425, 80, 16))
        self.effectivenessLabel.setStyleSheet("color: rgb(136, 136, 136);")
        self.effectivenessLabel.setObjectName("effectivenessLabel")
        self.effectivenessBox = QtWidgets.QSpinBox(createVaccineLot)
        self.effectivenessBox.setGeometry(QtCore.QRect(240, 440, 80, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.effectivenessBox.setFont(font)
        self.effectivenessBox.setStyleSheet("border-top-color: white; border-left-color: white; border-right-color: white; border-bottom-width: 2px; border-style:solid;")
        self.effectivenessBox.setMinimum(1)
        self.effectivenessBox.setObjectName("effectivenessBox")
        self.protectionTimeLabel = QtWidgets.QLabel(createVaccineLot)
        self.protectionTimeLabel.setGeometry(QtCore.QRect(240, 500, 120, 31))
        self.protectionTimeLabel.setStyleSheet("color: rgb(136, 136, 136);")
        self.protectionTimeLabel.setObjectName("protectionTimeLabel")
        self.protectionTimeBox = QtWidgets.QSpinBox(createVaccineLot)
        self.protectionTimeBox.setGeometry(QtCore.QRect(240, 530, 120, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.protectionTimeBox.setFont(font)
        self.protectionTimeBox.setStyleSheet("border-top-color: white; border-left-color: white; border-right-color: white; border-bottom-width: 2px; border-style:solid;")
        self.protectionTimeBox.setMinimum(1)
        self.protectionTimeBox.setMaximum(999)
        self.protectionTimeBox.setObjectName("protectionTimeBox")
        self.dateBox = QtWidgets.QDateEdit(createVaccineLot)
        self.dateBox.setGeometry(QtCore.QRect(50, 610, 110, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateBox.setFont(font)
        self.dateBox.setStyleSheet("border-top-color: white; border-left-color: white; border-right-color: white; border-bottom-width: 2px; border-style:solid;")
        self.dateBox.setObjectName("dateBox")
        self.dateLabel = QtWidgets.QLabel(createVaccineLot)
        self.dateLabel.setGeometry(QtCore.QRect(50, 594, 110, 17))
        self.dateLabel.setStyleSheet("color: rgb(136, 136, 136);")
        self.dateLabel.setObjectName("dateLabel")
        self.imageLabel = QtWidgets.QLabel(createVaccineLot)
        self.imageLabel.setGeometry(QtCore.QRect(148, 33, 150, 17))
        self.imageLabel.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.imageLabel.setObjectName("imageLabel")

        self.createButton = QtWidgets.QPushButton(createVaccineLot)
        self.createButton.setGeometry(QtCore.QRect(125, 680, 210, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.createButton.setFont(font)
        self.createButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.createButton.setStyleSheet("background-color: rgb(72, 72, 72); color: rgb(255, 255, 255);")
        self.createButton.setObjectName("createButton")
        self.createButton.clicked.connect(self.onButtonClicked)

        self.openImg = QtWidgets.QPushButton(createVaccineLot)
        self.openImg.setGeometry(QtCore.QRect(148, 230, 150, 40))
        self.openImg.setMinimumSize(QtCore.QSize(0, 30))
        self.openImg.clicked.connect(self.searchImage)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.openImg.setFont(font)
        self.openImg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.openImg.setStyleSheet("background-color: rgb(72, 72, 72); color: rgb(255, 255, 255);")
        self.openImg.setObjectName("openImg")

        self.frame = QtWidgets.QFrame(createVaccineLot)
        self.frame.setGeometry(QtCore.QRect(148, 50, 150, 181))
        self.frame.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")

        self.imagePreview = QtWidgets.QLabel(self.frame)
        self.imagePreview.setGeometry(QtCore.QRect(0, 0, 150, 150))
        self.imagePreview.setMinimumSize(QtCore.QSize(150, 150))
        self.imagePreview.setMaximumSize(QtCore.QSize(100, 100))
        self.imagePreview.setStyleSheet("border-radius: 20;")
        self.imagePreview.setText("")
        self.imagePreview.setPixmap(QtGui.QPixmap("./interface/img/img_placeholder.png"))
        self.imagePreview.setScaledContents(True)
        self.imagePreview.setObjectName("imagePreview")

        self.imageBox = QtWidgets.QLineEdit(self.frame)
        self.imageBox.setGeometry(QtCore.QRect(9, 150, 131, 30))
        self.imageBox.setMinimumSize(QtCore.QSize(0, 0))
        self.imageBox.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setKerning(True)
        self.imageBox.setFont(font)
        self.imageBox.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.imageBox.setFrame(False)
        self.imageBox.setAlignment(QtCore.Qt.AlignCenter)
        self.imageBox.setReadOnly(True)
        self.imageBox.setObjectName("imageBox")

        self.card_bg = QtWidgets.QFrame(createVaccineLot)
        self.card_bg.setGeometry(QtCore.QRect(25, 20, 400, 731))
        self.card_bg.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 12;")
        self.card_bg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card_bg.setFrameShadow(QtWidgets.QFrame.Plain)
        self.card_bg.setObjectName("card_bg")

        # THIS QT RAISE METHOD WORKS AS A LAYER ORGANIZER MEANING THAT BRINGS UP AN ELEMENT OVER OTHERS BEING DISPLAYED ON THE UI
        self.card_bg.raise_()
        self.inputLotId.raise_()
        self.lotId.raise_()
        self.manufacturerBox.raise_()
        self.manufacturerLabel.raise_()
        self.vaccineTypeBox.raise_()
        self.vaccineTypeLabel.raise_()
        self.unitsAmountBox.raise_()
        self.doseBox.raise_()
        self.temperatureBox.raise_()
        self.effectivenessBox.raise_()
        self.protectionTimeLabel.raise_()
        self.protectionTimeBox.raise_()
        self.dateBox.raise_()
        self.createButton.raise_()
        self.openImg.raise_()
        self.frame.raise_()
        self.imageLabel.raise_()
        self.temperatureLabel.raise_()
        self.unitsAmountlabel.raise_()
        self.doseLabel.raise_()
        self.effectivenessLabel.raise_()
        self.dateLabel.raise_()

        self.retranslateUi(createVaccineLot)
        QtCore.QMetaObject.connectSlotsByName(createVaccineLot)
    
    # FUNCTION TO SET THE TEXT OF THE ELEMENTS CREATED VIA QT.
    def retranslateUi(self, createVaccineLot):
        _translate = QtCore.QCoreApplication.translate
        createVaccineLot.setWindowTitle(_translate("createVaccineLot", "Crear lote de vacunas"))
        self.lotId.setText(_translate("createVaccineLot", "Número de Lote"))
        self.manufacturerBox.setItemText(0, _translate("createVaccineLot", "Sinovac"))
        self.manufacturerBox.setItemText(1, _translate("createVaccineLot", "Pfizer"))
        self.manufacturerBox.setItemText(2, _translate("createVaccineLot", "Moderna"))
        self.manufacturerBox.setItemText(3, _translate("createVaccineLot", "SputnikV"))
        self.manufacturerBox.setItemText(4, _translate("createVaccineLot", "AstraZeneca"))
        self.manufacturerBox.setItemText(5, _translate("createVaccineLot", "Sinopharm"))
        self.manufacturerBox.setItemText(6, _translate("createVaccineLot", "Covaxim"))
        self.manufacturerLabel.setText(_translate("createVaccineLot", "Fabricante"))
        self.vaccineTypeBox.setItemText(0, _translate("createVaccineLot", "Vector viral"))
        self.vaccineTypeBox.setItemText(1, _translate("createVaccineLot", "ARN/ADN"))
        self.vaccineTypeBox.setItemText(2, _translate("createVaccineLot", "Virus desactivado"))
        self.vaccineTypeBox.setItemText(3, _translate("createVaccineLot", "En base a proteínas"))
        self.vaccineTypeLabel.setText(_translate("createVaccineLot", "Tipo de Vacuna"))
        self.unitsAmountlabel.setText(_translate("createVaccineLot", "Unidades Disponibles"))
        self.doseLabel.setText(_translate("createVaccineLot", "Dosis"))
        self.temperatureLabel.setText(_translate("createVaccineLot", "Temperatura de\n"
" Almacenamiento (°C)"))
        self.effectivenessLabel.setText(_translate("createVaccineLot", "Efectividad (%)"))
        self.protectionTimeLabel.setText(_translate("createVaccineLot", "Tiempo de\n"
"Protección (Días)"))
        self.dateBox.setDisplayFormat(_translate("createVaccineLot", "d/M/yyyy"))
        self.dateLabel.setText(_translate("createVaccineLot", "Fecha de Vencimiento"))
        self.imageLabel.setText(_translate("createVaccineLot", "Foto del lote"))
        self.createButton.setText(_translate("createVaccineLot", "Crear"))
        self.openImg.setText(_translate("createVaccineLot", "Buscar"))
        self.imageBox.setText(_translate("createVaccineLot", "placeholder.png"))

    # FUNCTION ASSIGNED TO CREATEBUTTON BUTTON THAT ON CLICK SENDS THE VACCINELOT DATA TO THE DB
    def onButtonClicked(self):

        if self.inputLotId.text() == "":
            self.showErrorMessage("Ingrese número de lote")
            return

        lotId = int(self.inputLotId.text())
        lot = self.manager.find_lot(lotId)

        if bool(lot):
            self.showErrorMessage("Número de lote ya existe")
            return

        manufacturer = self.manufacturerBox.currentText()
        vaccineType = self.vaccineTypeBox.currentText()
        units = self.unitsAmountBox.value()
        dose = self.doseBox.value()
        temperature = self.temperatureBox.value()
        effectiveness = self.effectivenessBox.value()
        protectionTime = self.protectionTimeBox.value()
        date = int(self.dateBox.dateTime().toPyDateTime().timestamp())
        img = self.image_url
        res = self.manager.new_lot(vaccine_lot.VaccineLot(lotId, manufacturer, vaccineType, 
                                                        units, dose, temperature, effectiveness, protectionTime, date, img))
        if res:
            self.showSuccessMessage("Lote creado con éxito")
        else:
            self.showErrorMessage("Error creando el lote intente de nuevo")
    
    # VIA QT OPEN A WINDOW IN ORDER TO GET THE RELATIVE PATH OF AN IMAGE TO PLACE IT AS LOT IMAGE
    def searchImage(self):
        image_path = QtWidgets.QFileDialog.getOpenFileName(self.mainLotWidget, 'Seleccionar imagen', './', 'Image Files(*.png *.jpg *.bmp)')
        self.image_url = image_path[0]
        image_filename = self.image_url.split("/")[-1]

        self.convert_to_srgb()

        self.imageBox.setText(image_filename)
        pixmap = QtGui.QPixmap(self.image_url)
        self.imagePreview.setPixmap(QtGui.QPixmap(pixmap))

    # THIS PIECE OF CODE WAS ADDED IN ORDER TO CHANGE THE COLOR SPACE OF AN IMAGE TO AVOID THE FOLLOWING ALERT :
    # qt.gui.icc: fromIccProfile: failed minimal tag size sanity
    def convert_to_srgb(self): 
        #CONVERT PIL IMAGE TO sRGB COLOR SPACE (IF POSIBLE)    
        img = Image.open(self.image_url)         
        icc = img.info.get('icc_profile', '')
        
        if icc:             
            io_handle = io.BytesIO(icc)            
            src_profile = ImageCms.ImageCmsProfile(io_handle)             
            dst_profile = ImageCms.createProfile('sRGB')             
            img_conv = ImageCms.profileToProfile(img, src_profile, dst_profile)
            icc_conv = img_conv.info.get('icc_profile','')
        
            if icc != icc_conv:     
                # ICC PROFILE WAS CHANGED -> SAVE CONVERTED FILE
                img_conv.save(   self.image_url,format = 'JPEG',quality = 50,icc_profile = icc_conv)
