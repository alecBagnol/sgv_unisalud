from modules import vaccination_schedule
from interface import findDialog
import datetime

class AffiliateVaccinationSchedule(findDialog.FindDialog):

    def __init__(self):
        self.manager = vaccination_schedule.VaccinationScheduleManager()
        self.windowName = "Programación"
        self.placeHolder = "Documento de Identidad"
        self.regex = '\d{1,12}'
        super().__init__()

    def onFindClick(self):
        if self.inputBox.text() == "":
            return
        affiliate = int(self.inputBox.text())
        schedule = self.manager.get_schedule(affiliate)

        if bool(schedule):
            self.label.setText(f"""
                Nombres: {schedule["affiliate"]["first_name"]}
                Apellidos: {schedule["affiliate"]["last_name"]}
                Documento de Identidad: {schedule["affiliate"]["affiliate_id"]}
                Dirección: {schedule["affiliate"]["address"]}
                Teléfono: {schedule["affiliate"]["phone"]}
                Correo: {schedule["affiliate"]["email"]}
                Fecha de Nacimiento: {datetime.datetime.fromtimestamp(schedule["affiliate"]["birth_date"]).strftime("%d/%m/%Y")}
                Ciudad: {schedule["affiliate"]["city"]}
                Lote de Vacunas: {schedule["vaccine_lot"]["vaccine_lot_id"]}
                Fecha y Hora de Vacunación: {datetime.datetime.fromtimestamp(schedule["date_time"]).strftime("%d/%m/%Y, %H:%M:%S")}
            """)
        else:
            self.label.setText("    USUARIO NO ENCONTRADO")

