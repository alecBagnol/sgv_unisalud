from PyQt5 import QtCore, QtGui, QtWidgets
from interface import utils
from interface import allVaccinationSchedule


    # DESCRIPTION:
        # This class creates the main menu user interface via Qt5 elements for python  

    # ARGUMENTS:
        # Some of the UI elements created using Qt methods are:
        # - MainWindow: as a qtwidget
        # - centralwidget, horizontalLayout, sideBar, verticalLayoutWidget, menuList, mainTitle, menuOptionList:as tidying layout frames
        # - mainTitle_top, mainTitle_bottom, label: as text labels
        # - welcomeFrame, welcomePicture: as the frame and image label showcase once the app is launched
        # - affiliateButton, vaccineLotButton, vaccinationPlanButton, vaccinationScheduleButton, buttons : as qt buttons that showcases the different sections 




class MainMenu(object):
    openCreateAffiliate = None
    openAffiliateFind = None
    openVaccinate = None

    openCreateVaccinationSchedule = None
    openAllVaccinationSchedule = None
    openAffiliateVaccinationSchedule = None

    openCreateVaccineLot = None
    openVaccineLotFind = None

    openCreateVaccinationPlan = None
    openVaccinationPlanFind = None
    
    

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 768))
        MainWindow.setMaximumSize(QtCore.QSize(1024, 768))
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Colombia))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.sideBar = QtWidgets.QFrame(self.centralwidget)
        self.sideBar.setMaximumSize(QtCore.QSize(300, 16777215))
        self.sideBar.setStyleSheet("background-color: rgb(48, 48, 48);")
        self.sideBar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sideBar.setFrameShadow(QtWidgets.QFrame.Plain)
        self.sideBar.setObjectName("sideBar")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.sideBar)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 270, 212, 291))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.menuList = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.menuList.setContentsMargins(0, 0, 0, 0)
        self.menuList.setObjectName("menuList")

        self.affiliateButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.affiliateButton.setMinimumSize(QtCore.QSize(210, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.affiliateButton.setFont(font)
        self.affiliateButton.setStyleSheet("background-color: rgb(72, 72, 72); color: rgb(255, 255, 255);")
        self.affiliateButton.setObjectName("affiliateButton")

        self.menuList.addWidget(self.affiliateButton)

        self.affiliateButton.clicked.connect(self.onAffiliateButtonClicked)
        self.affiliateButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.vaccineLotButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.vaccineLotButton.setMinimumSize(QtCore.QSize(210, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.vaccineLotButton.setFont(font)
        self.vaccineLotButton.setStyleSheet("background-color: rgb(72, 72, 72); color: rgb(255, 255, 255);")
        self.vaccineLotButton.setObjectName("vaccineLotButton")

        self.menuList.addWidget(self.vaccineLotButton)

        self.vaccineLotButton.clicked.connect(self.onVaccineLotButtonClicked)
        self.vaccineLotButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.vaccinationPlanButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.vaccinationPlanButton.setMinimumSize(QtCore.QSize(210, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.vaccinationPlanButton.setFont(font)
        self.vaccinationPlanButton.setStyleSheet("background-color: rgb(72, 72, 72); color: rgb(255, 255, 255);")
        self.vaccinationPlanButton.setObjectName("vaccinationPlanButton")
        self.menuList.addWidget(self.vaccinationPlanButton)
        self.vaccinationPlanButton.clicked.connect(self.onVaccinationPlanButtonClicked)
        self.vaccinationPlanButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.vaccinationScheduleButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.vaccinationScheduleButton.setMinimumSize(QtCore.QSize(210, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.vaccinationScheduleButton.setFont(font)
        self.vaccinationScheduleButton.setStyleSheet("background-color: rgb(72, 72, 72); color: rgb(255, 255, 255);")
        self.vaccinationScheduleButton.setObjectName("vaccinationScheduleButton")
        self.menuList.addWidget(self.vaccinationScheduleButton)
        self.vaccinationScheduleButton.clicked.connect(self.onVaccinationScheduleButtonClicked)
        self.vaccinationScheduleButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.label = QtWidgets.QLabel(self.sideBar)
        self.label.setGeometry(QtCore.QRect(50, 90, 210, 60))
        self.label.setMinimumSize(QtCore.QSize(210, 60))
        self.label.setMaximumSize(QtCore.QSize(210, 60))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./interface/img/logo_unisalud.png"))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.sideBar)
        self.contentContainer = QtWidgets.QFrame(self.centralwidget)
        self.contentContainer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.contentContainer.setFrameShadow(QtWidgets.QFrame.Plain)
        self.contentContainer.setObjectName("contentContainer")
        self.mainTitle = QtWidgets.QFrame(self.contentContainer)
        self.mainTitle.setGeometry(QtCore.QRect(60, 80, 321, 80))
        self.mainTitle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainTitle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainTitle.setObjectName("mainTitle")
        self.mainTitle_top = QtWidgets.QLabel(self.mainTitle)
        self.mainTitle_top.setGeometry(QtCore.QRect(0, 30, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.mainTitle_top.setFont(font)
        self.mainTitle_top.setObjectName("mainTitle_top")
        self.mainTitle_bottom = QtWidgets.QLabel(self.mainTitle)
        self.mainTitle_bottom.setGeometry(QtCore.QRect(0, 0, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.mainTitle_bottom.setFont(font)
        self.mainTitle_bottom.setStyleSheet("color: rgb(140, 140, 140);")
        self.mainTitle_bottom.setObjectName("mainTitle_bottom")
        self.menuOptionList = QtWidgets.QFrame(self.contentContainer)
        self.menuOptionList.setGeometry(QtCore.QRect(30, 190, 658, 516))
        self.menuOptionList.setMinimumSize(QtCore.QSize(658, 516))
        self.menuOptionList.setMaximumSize(QtCore.QSize(658, 516))
        self.menuOptionList.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menuOptionList.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menuOptionList.setObjectName("menuOptionList")

        # STARTING FRAME
        self.welcomeFrame = QtWidgets.QFrame(self.menuOptionList)
        self.welcomeFrame.setEnabled(True)
        self.welcomeFrame.setGeometry(QtCore.QRect(0, 0, 658, 516))
        self.welcomeFrame.setMinimumSize(QtCore.QSize(658, 516))
        self.welcomeFrame.setMaximumSize(QtCore.QSize(658, 516))
        self.welcomeFrame.setStyleSheet("")
        self.welcomeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.welcomeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.welcomeFrame.setObjectName("welcomeFrame")

        self.welcomePicture = QtWidgets.QLabel(self.welcomeFrame)
        self.welcomePicture.setGeometry(QtCore.QRect(0, 0, 658, 516))
        self.welcomePicture.setMinimumSize(QtCore.QSize(658, 516))
        self.welcomePicture.setText("")
        self.welcomePicture.setPixmap(QtGui.QPixmap("./interface/img/welcome_pic.png"))
        self.welcomePicture.setObjectName("welcomePicture")


        # AFFILIATES SECTION FRAME
        self.affiliateFrame = QtWidgets.QFrame(self.menuOptionList)
        self.affiliateFrame.setGeometry(QtCore.QRect(0, 0, 658, 516))
        self.affiliateFrame.setMinimumSize(QtCore.QSize(658, 516))
        self.affiliateFrame.setMaximumSize(QtCore.QSize(658, 516))
        self.affiliateFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.affiliateFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.affiliateFrame.setObjectName("affiliateFrame")

        self.affiliate_title = QtWidgets.QLabel(self.affiliateFrame)
        self.affiliate_title.setGeometry(QtCore.QRect(40, 40, 531, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.affiliate_title.setFont(font)
        self.affiliate_title.setObjectName("affiliate_title")

        self.affiliate_bg = QtWidgets.QLabel(self.affiliateFrame)
        self.affiliate_bg.setGeometry(QtCore.QRect(0, 0, 658, 516))
        self.affiliate_bg.setText("")
        self.affiliate_bg.setPixmap(QtGui.QPixmap("./interface/img/affiliates_bg.png"))
        self.affiliate_bg.setObjectName("affiliate_bg")

        # BUTTON 01_01 AFFILIATE SECTION
        self.addAffiliate = QtWidgets.QPushButton(self.affiliateFrame)
        self.addAffiliate.setGeometry(QtCore.QRect(114, 178, 90, 90))
        self.addAffiliate.setStyleSheet("background-image: url(:/buttones/icons/1_01.png);border-radius: 12;")
        self.addAffiliate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        self.addAffiliate.setText("")
        self.addAffiliate.setObjectName("addAffiliate")
        self.addAffiliate.clicked.connect(self.open_add_affiliate)

        # BUTTON 01_02 AFFILIATE SECTION
        self.findAffiliate = QtWidgets.QPushButton(self.affiliateFrame)
        self.findAffiliate.setGeometry(QtCore.QRect(284, 178, 90, 90))
        self.findAffiliate.setStyleSheet("background-image: url(:/buttones/icons/1_02.png); border-radius: 12;")
        self.findAffiliate.setText("")
        self.findAffiliate.setObjectName("findAffiliate")
        self.findAffiliate.clicked.connect(self.open_find_affiliate)
        self.findAffiliate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # BUTTON 01_03 AFFILIATE SECTION
        self.vaccinateAffiliate = QtWidgets.QPushButton(self.affiliateFrame)
        self.vaccinateAffiliate.setGeometry(QtCore.QRect(454, 178, 90, 90))
        self.vaccinateAffiliate.setStyleSheet("background-image: url(:/buttones/icons/1_03.png); border-radius: 12;")
        self.vaccinateAffiliate.setText("")
        self.vaccinateAffiliate.setObjectName("vaccinateAffiliate")
        self.vaccinateAffiliate.clicked.connect(self.open_vaccine)
        self.vaccinateAffiliate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.addAffiliate_label = QtWidgets.QLabel(self.affiliateFrame)
        self.addAffiliate_label.setGeometry(QtCore.QRect(110, 277, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addAffiliate_label.setFont(font)
        self.addAffiliate_label.setObjectName("addAffiliate_label")

        self.findAffiliate_label = QtWidgets.QLabel(self.affiliateFrame)
        self.findAffiliate_label.setGeometry(QtCore.QRect(290, 277, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.findAffiliate_label.setFont(font)
        self.findAffiliate_label.setAlignment(QtCore.Qt.AlignCenter)
        self.findAffiliate_label.setObjectName("findAffiliate_label")

        self.vaccinateAffiliate_label = QtWidgets.QLabel(self.affiliateFrame)
        self.vaccinateAffiliate_label.setGeometry(QtCore.QRect(450, 277, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.vaccinateAffiliate_label.setFont(font)
        self.vaccinateAffiliate_label.setAlignment(QtCore.Qt.AlignCenter)
        self.vaccinateAffiliate_label.setObjectName("vaccinateAffiliate_label")
        

        # AFFILIATE SECTION TIDYING UP LAYERS
        self.affiliate_bg.raise_()
        self.affiliate_title.raise_()
        self.addAffiliate.raise_()
        self.findAffiliate.raise_()
        self.vaccinateAffiliate.raise_()
        self.addAffiliate_label.raise_()
        self.findAffiliate_label.raise_()
        self.vaccinateAffiliate_label.raise_()


        # LOT SECTION FRAME
        self.lotFrame = QtWidgets.QFrame(self.menuOptionList)
        self.lotFrame.setGeometry(QtCore.QRect(0, 0, 658, 516))
        self.lotFrame.setMinimumSize(QtCore.QSize(658, 516))
        self.lotFrame.setMaximumSize(QtCore.QSize(658, 516))
        self.lotFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lotFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lotFrame.setObjectName("lotFrame")

        self.lotTitle = QtWidgets.QLabel(self.lotFrame)
        self.lotTitle.setGeometry(QtCore.QRect(40, 40, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lotTitle.setFont(font)
        self.lotTitle.setObjectName("lotTitle")

        self.lot_bg = QtWidgets.QLabel(self.lotFrame)
        self.lot_bg.setGeometry(QtCore.QRect(0, 0, 658, 516))
        self.lot_bg.setMinimumSize(QtCore.QSize(658, 516))
        self.lot_bg.setMaximumSize(QtCore.QSize(658, 516))
        self.lot_bg.setText("")
        self.lot_bg.setPixmap(QtGui.QPixmap("./interface/img/lot_bg.png"))
        self.lot_bg.setObjectName("lot_bg")

        self.addLot_label = QtWidgets.QLabel(self.lotFrame)
        self.addLot_label.setGeometry(QtCore.QRect(210, 277, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addLot_label.setFont(font)
        self.addLot_label.setAlignment(QtCore.Qt.AlignCenter)
        self.addLot_label.setObjectName("addLot_label")

        self.findLot_label = QtWidgets.QLabel(self.lotFrame)
        self.findLot_label.setGeometry(QtCore.QRect(380, 277, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.findLot_label.setFont(font)
        self.findLot_label.setAlignment(QtCore.Qt.AlignCenter)
        self.findLot_label.setObjectName("findLot_label")

        # BUTTON 02_01 LOT SECTION
        self.addLot = QtWidgets.QPushButton(self.lotFrame)
        self.addLot.setGeometry(QtCore.QRect(199, 178, 90, 90))
        self.addLot.setStyleSheet("background-image: url(:/buttones/icons/2_01.png);border-radius: 12;")
        self.addLot.setText("")
        self.addLot.setObjectName("addLot")
        self.addLot.clicked.connect(self.open_create_vaccineLot)
        self.addLot.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # BUTTON 02_02 LOT SECTION
        self.findLot = QtWidgets.QPushButton(self.lotFrame)
        self.findLot.setGeometry(QtCore.QRect(369, 178, 90, 90))
        self.findLot.setMinimumSize(QtCore.QSize(0, 0))
        self.findLot.setStyleSheet("background-image: url(:/buttones/icons/2_02.png);border-radius: 12;")
        self.findLot.setText("")
        self.findLot.setObjectName("findLot")
        self.findLot.clicked.connect(self.open_find_vaccineLot)
        self.findLot.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # LOT FRAME LAYER SETUP
        self.lot_bg.raise_()
        self.addLot_label.raise_()
        self.findLot_label.raise_()
        self.addLot.raise_()
        self.findLot.raise_()
        self.lotTitle.raise_()


        # PLAN SECTION FRAME
        self.planFrame = QtWidgets.QFrame(self.menuOptionList)
        self.planFrame.setGeometry(QtCore.QRect(0, 0, 658, 516))
        self.planFrame.setMinimumSize(QtCore.QSize(658, 516))
        self.planFrame.setMaximumSize(QtCore.QSize(658, 516))
        self.planFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.planFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.planFrame.setObjectName("planFrame")

        # BUTTON 03_02 PLAN SECTION
        self.findPlan = QtWidgets.QPushButton(self.planFrame)
        self.findPlan.setGeometry(QtCore.QRect(369, 178, 90, 90))
        self.findPlan.setMinimumSize(QtCore.QSize(0, 0))
        self.findPlan.setStyleSheet("background-image: url(:/buttones/icons/3_02.png);border-radius: 12;")
        self.findPlan.setText("")
        self.findPlan.setObjectName("findPlan")
        self.findPlan.clicked.connect(self.open_find_vaccinationPlan)
        self.addLot.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.plan_bg = QtWidgets.QLabel(self.planFrame)
        self.plan_bg.setGeometry(QtCore.QRect(0, 0, 658, 516))
        self.plan_bg.setMinimumSize(QtCore.QSize(658, 516))
        self.plan_bg.setMaximumSize(QtCore.QSize(658, 516))
        self.plan_bg.setText("")
        self.plan_bg.setPixmap(QtGui.QPixmap("./interface/img/plan_bg.png"))
        self.plan_bg.setObjectName("plan_bg")

        self.planTitle = QtWidgets.QLabel(self.planFrame)
        self.planTitle.setGeometry(QtCore.QRect(40, 40, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.planTitle.setFont(font)
        self.planTitle.setObjectName("planTitle")

        # BUTTON 03_01 PLAN SECTION
        self.addPlan = QtWidgets.QPushButton(self.planFrame)
        self.addPlan.setGeometry(QtCore.QRect(199, 178, 90, 90))
        self.addPlan.setStyleSheet("background-image: url(:/buttones/icons/3_01.png);border-radius: 12;")
        self.addPlan.setText("")
        self.addPlan.setObjectName("addPlan")
        self.addPlan.clicked.connect(self.open_create_vaccinationPlan)
        self.addPlan.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.addPlan_label = QtWidgets.QLabel(self.planFrame)
        self.addPlan_label.setGeometry(QtCore.QRect(190, 277, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addPlan_label.setFont(font)
        self.addPlan_label.setAlignment(QtCore.Qt.AlignCenter)
        self.addPlan_label.setObjectName("addPlan_label")

        self.findPlan_label = QtWidgets.QLabel(self.planFrame)
        self.findPlan_label.setGeometry(QtCore.QRect(350, 277, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.findPlan_label.setFont(font)
        self.findPlan_label.setAlignment(QtCore.Qt.AlignCenter)
        self.findPlan_label.setObjectName("findPlan_label")

        # PLAN FRAME LAYER SETUP
        self.plan_bg.raise_()
        self.planTitle.raise_()
        self.addPlan.raise_()
        self.addPlan_label.raise_()
        self.findPlan_label.raise_()
        self.findPlan.raise_()


        # SCHEDULE SECTION FRAME
        self.scheduleFrame = QtWidgets.QFrame(self.menuOptionList)
        self.scheduleFrame.setGeometry(QtCore.QRect(0, 0, 658, 516))
        self.scheduleFrame.setMinimumSize(QtCore.QSize(658, 516))
        self.scheduleFrame.setMaximumSize(QtCore.QSize(658, 516))
        self.scheduleFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scheduleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scheduleFrame.setObjectName("scheduleFrame")

        # BUTTON 04_02 SCHEDULE SECTION
        self.findSchedule = QtWidgets.QPushButton(self.scheduleFrame)
        self.findSchedule.setGeometry(QtCore.QRect(284, 181, 90, 90))
        self.findSchedule.setStyleSheet("background-image: url(:/buttones/icons/4_02.png); border-radius: 12;")
        self.findSchedule.setText("")
        self.findSchedule.setObjectName("findSchedule")
        self.findSchedule.clicked.connect(self.open_all_vaccinationSchedule)
        self.findSchedule.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # BUTTON 04_01 SCHEDULE SECTION
        self.addSchedule = QtWidgets.QPushButton(self.scheduleFrame)
        self.addSchedule.setGeometry(QtCore.QRect(114, 181, 90, 90))
        self.addSchedule.setStyleSheet("background-image: url(:/buttones/icons/4_01.png); border-radius: 12;")
        self.addSchedule.setText("")
        self.addSchedule.setObjectName("addSchedule")
        self.addSchedule.clicked.connect(self.open_create_vaccinationSchedule)
        self.addSchedule.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.addSchedule_label = QtWidgets.QLabel(self.scheduleFrame)
        self.addSchedule_label.setGeometry(QtCore.QRect(110, 280, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addSchedule_label.setFont(font)
        self.addSchedule_label.setAlignment(QtCore.Qt.AlignCenter)
        self.addSchedule_label.setObjectName("addSchedule_label")

        # BUTTON 04_03 SCHEDULE SECTION
        self.affiliateSchedule = QtWidgets.QPushButton(self.scheduleFrame)
        self.affiliateSchedule.setGeometry(QtCore.QRect(454, 181, 90, 90))
        self.affiliateSchedule.setStyleSheet("image: url(:/buttones/icons/4_03.png);border-radius: 12;")
        self.affiliateSchedule.setText("")
        self.affiliateSchedule.setObjectName("affiliateSchedule")
        self.affiliateSchedule.clicked.connect(self.open_affiliate_vaccinationSchedule)
        self.affiliateSchedule.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.scheduleTitle = QtWidgets.QLabel(self.scheduleFrame)
        self.scheduleTitle.setGeometry(QtCore.QRect(40, 39, 531, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.scheduleTitle.setFont(font)
        self.scheduleTitle.setObjectName("scheduleTitle")

        self.schedule_bg = QtWidgets.QLabel(self.scheduleFrame)
        self.schedule_bg.setGeometry(QtCore.QRect(0, 0, 658, 516))
        self.schedule_bg.setText("")
        self.schedule_bg.setPixmap(QtGui.QPixmap("./interface/img/schedule_bg.png"))
        self.schedule_bg.setObjectName("schedule_bg")

        self.findSchedule_label = QtWidgets.QLabel(self.scheduleFrame)
        self.findSchedule_label.setGeometry(QtCore.QRect(270, 280, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.findSchedule_label.setFont(font)
        self.findSchedule_label.setAlignment(QtCore.Qt.AlignCenter)
        self.findSchedule_label.setObjectName("findSchedule_label")

        self.affiliateSchedule_label = QtWidgets.QLabel(self.scheduleFrame)
        self.affiliateSchedule_label.setGeometry(QtCore.QRect(450, 280, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.affiliateSchedule_label.setFont(font)
        self.affiliateSchedule_label.setAlignment(QtCore.Qt.AlignCenter)
        self.affiliateSchedule_label.setObjectName("affiliateSchedule_label")

        # SCHEDULE FRAME LAYER SETUP
        self.schedule_bg.raise_()
        self.findSchedule_label.raise_()
        self.affiliateSchedule_label.raise_()
        self.scheduleTitle.raise_()
        self.findSchedule.raise_()
        self.addSchedule_label.raise_()
        self.addSchedule.raise_()
        self.affiliateSchedule.raise_()

        # SET FRAME VISIBILITY
        self.welcomeFrame.setVisible(True)
        self.affiliateFrame.setVisible(False)
        self.lotFrame.setVisible(False)
        self.planFrame.setVisible(False)
        self.scheduleFrame.setVisible(False)


        self.horizontalLayout.addWidget(self.contentContainer)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sgv Salud"))

        # SIDEBAR BUTTONS SECTION 
        self.affiliateButton.setText(_translate("MainWindow", "Afiliados"))
        self.vaccineLotButton.setText(_translate("MainWindow", "Lotes de Vacunas"))
        self.vaccinationPlanButton.setText(_translate("MainWindow", "Planes de Vacunación"))
        self.vaccinationScheduleButton.setText(_translate("MainWindow", "Programación de Vacunación"))

        # MAIN SECTION
        self.mainTitle_top.setText(_translate("MainWindow", "vacunación"))
        self.mainTitle_bottom.setText(_translate("MainWindow", "Sistema de gestión de"))

        # AFFILIATES SECTION
        self.affiliate_title.setText(_translate("MainWindow", "Sección de Afiliados"))
        self.addAffiliate_label.setText(_translate("MainWindow", "Crear Afiliado"))
        self.findAffiliate_label.setText(_translate("MainWindow", "Consultar\n"
"Afiliado"))
        self.vaccinateAffiliate_label.setText(_translate("MainWindow", "Vacuncación\n"
"de Afiliado"))

        # LOT SECTION
        self.lotTitle.setText(_translate("MainWindow", "Sección de Lotes de Vacunas"))
        self.addLot_label.setText(_translate("MainWindow", "Agregar\n"
"Lote"))
        self.findLot_label.setText(_translate("MainWindow", "Consultar\n"
"Lote"))

        # PLAN SECTION
        self.planTitle.setText(_translate("MainWindow", "Sección Planes de Vacunación"))
        self.addPlan_label.setText(_translate("MainWindow", "Crear Plan de\n"
"Vacunación"))
        self.findPlan_label.setText(_translate("MainWindow", "Consultar Plan\n"
"de Vacunación"))

        # SCHEDULE SECTION
        self.addSchedule_label.setText(_translate("MainWindow", "Crear\n"
"Programación"))
        self.scheduleTitle.setText(_translate("MainWindow", "Sección Programación de\n"
"Vacunación"))
        self.findSchedule_label.setText(_translate("MainWindow", "Consultar\n"
"Programación"))
        self.affiliateSchedule_label.setText(_translate("MainWindow", "Programación\n"
"de Afiliado"))

    def onAffiliateButtonClicked(self):
        # utils.clearLayout(self.menuOptionList)
        # _translate = QtCore.QCoreApplication.translate
        self.welcomeFrame.setVisible(False)
        self.affiliateFrame.setVisible(True)
        self.lotFrame.setVisible(False)
        self.planFrame.setVisible(False)
        self.scheduleFrame.setVisible(False)

    def onVaccineLotButtonClicked(self):
        # utils.clearLayout(self.menuOptionList)
        # _translate = QtCore.QCoreApplication.translate
        self.welcomeFrame.setVisible(False)
        self.affiliateFrame.setVisible(False)
        self.lotFrame.setVisible(True)
        self.planFrame.setVisible(False)
        self.scheduleFrame.setVisible(False)
        
    def onVaccinationPlanButtonClicked(self):
        # utils.clearLayout(self.menuOptionList)
        # _translate = QtCore.QCoreApplication.translate
        self.welcomeFrame.setVisible(False)
        self.affiliateFrame.setVisible(False)
        self.lotFrame.setVisible(False)
        self.planFrame.setVisible(True)
        self.scheduleFrame.setVisible(False)

    def onVaccinationScheduleButtonClicked(self):
        # utils.clearLayout(self.menuOptionList)
        # _translate = QtCore.QCoreApplication.translate
        self.welcomeFrame.setVisible(False)
        self.affiliateFrame.setVisible(False)
        self.lotFrame.setVisible(False)
        self.planFrame.setVisible(False)
        self.scheduleFrame.setVisible(True)

    def open_add_affiliate(self):
        self.openCreateAffiliate()

    def open_find_affiliate(self):
        self.openAffiliateFind()

    def open_vaccine(self):
        self.openVaccinate()

    def open_create_vaccineLot(self):
        self.openCreateVaccineLot()

    def open_find_vaccineLot(self):
        self.openVaccineLotFind()

    def open_create_vaccinationPlan(self):
        self.openCreateVaccinationPlan()

    def open_find_vaccinationPlan(self):
        self.openVaccinationPlanFind()

    def open_create_vaccinationSchedule(self):
        self.openCreateVaccinationSchedule()

    def open_all_vaccinationSchedule(self):
        self.openAllVaccinationSchedule()

    def open_affiliate_vaccinationSchedule(self):
        self.openAffiliateVaccinationSchedule()

# IMPORT BUTTONS IOED FROM THE QRC 
import interface.img.buttons_rc