from PyQt5 import QtCore, QtGui, QtWidgets
from modules import vaccination_schedule
from os import system, name as os_name
import datetime
import time
import re
import sys

class AllVaccinationSchedule(object):

    vaccination_scheduler = vaccination_schedule.VaccinationScheduleManager()

    def setupUi(self, vaccinationScheduleDialog):
        vaccinationScheduleDialog.setObjectName("vaccinationScheduleDialog")
        vaccinationScheduleDialog.resize(642, 337)
        vaccinationScheduleDialog.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Colombia))
        self.scheduleScroll = QtWidgets.QScrollArea(vaccinationScheduleDialog)
        self.scheduleScroll.setGeometry(QtCore.QRect(10, 10, 621, 321))
        self.scheduleScroll.setWidgetResizable(True)
        self.scheduleScroll.setObjectName("scheduleScroll")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 619, 319))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scheduleTable = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.scheduleTable.setGeometry(QtCore.QRect(0, 0, 621, 321))
        self.scheduleTable.setObjectName("scheduleTable")
        self.scheduleTable.setColumnCount(10)
        self.scheduleTable.setHorizontalHeaderLabels(['Nombres', 
                                        'Apellidos', 
                                        'Documento', 
                                        'Dirección', 
                                        'Teléfono', 
                                        'Correo', 
                                        'Fecha Nacimiento',
                                        'Ciudad',
                                        'Lote',
                                        'Fecha y Hora'])
        
        schedules = self.vaccination_scheduler.get_all()
        for schedule in schedules:
            self.scheduleScroll.setWidget(self.scrollAreaWidgetContents)
            self.scheduleTable.insertRow(self.scheduleTable.rowCount())
            self.scheduleTable.setItem(self.scheduleTable.rowCount() - 1, 0, QtWidgets.QTableWidgetItem(schedule["affiliate"]["first_name"]))
            self.scheduleTable.setItem(self.scheduleTable.rowCount() - 1, 1, QtWidgets.QTableWidgetItem(schedule["affiliate"]["last_name"]))
            self.scheduleTable.setItem(self.scheduleTable.rowCount() - 1, 2, QtWidgets.QTableWidgetItem(str(schedule["affiliate"]["affiliate_id"])))
            self.scheduleTable.setItem(self.scheduleTable.rowCount() - 1, 3, QtWidgets.QTableWidgetItem(schedule["affiliate"]["address"]))
            self.scheduleTable.setItem(self.scheduleTable.rowCount() - 1, 4, QtWidgets.QTableWidgetItem(schedule["affiliate"]["phone"]))
            self.scheduleTable.setItem(self.scheduleTable.rowCount() - 1, 5, QtWidgets.QTableWidgetItem(schedule["affiliate"]["email"]))
            self.scheduleTable.setItem(self.scheduleTable.rowCount() - 1, 6, QtWidgets.QTableWidgetItem(datetime.datetime.fromtimestamp(schedule["affiliate"]["birth_date"]).strftime("%d/%m/%Y")))
            self.scheduleTable.setItem(self.scheduleTable.rowCount() - 1, 7, QtWidgets.QTableWidgetItem(schedule["affiliate"]["city"]))
            self.scheduleTable.setItem(self.scheduleTable.rowCount() - 1, 8, QtWidgets.QTableWidgetItem(str(schedule["vaccine_lot"]["vaccine_lot_id"])))
            self.scheduleTable.setItem(self.scheduleTable.rowCount() - 1, 9, QtWidgets.QTableWidgetItem(datetime.datetime.fromtimestamp(schedule["date_time"]).strftime("%d/%m/%Y, %H:%M:%S")))

        self.retranslateUi(vaccinationScheduleDialog)
        QtCore.QMetaObject.connectSlotsByName(vaccinationScheduleDialog)

    def retranslateUi(self, vaccinationScheduleDialog):
        _translate = QtCore.QCoreApplication.translate
        vaccinationScheduleDialog.setWindowTitle(_translate("vaccinationScheduleDialog", "Programación"))

