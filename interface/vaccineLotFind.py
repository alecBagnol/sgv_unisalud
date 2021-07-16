from modules import vaccine_lot
from interface import findDialog
import datetime

class VaccineLotFind(findDialog.FindDialog):

    def __init__(self):
        self.manager = vaccine_lot.VaccineLotManager()
        self.windowName = "Lote de Vacunas"
        self.placeHolder = "Id del lote"
        self.regex = '\d{1,12}'
        super().__init__()

    def onFindClick(self):
        if self.inputBox.text() == "":
            return
        lotId = int(self.inputBox.text())
        lot = self.manager.find_lot(int(lotId))

        if bool(lot):
            self.label.setText(f"""
                Número de lote: {lot["vaccine_lot_id"]}
                Fabricante: {lot["manufacturer"]}
                Tipo de Vacuna: {lot["vaccine_type"]}
                Unidades Disponibles: {lot["amount"]}
                Unidades Usadas: {lot["used_amount"]}
                Dosis: {lot["dose"]}
                Temperatura: {lot["temperature"]}
                Efectividad: {lot["effectiveness"]}
                Tiempo de Protección: {lot["protection_time"]}
                Fecha de Vencimiento: {datetime.datetime.fromtimestamp(lot["expiration_date"]).strftime("%d/%m/%Y")}
                Url Imagen: {lot["image_url"]}
            """)
        else:
            self.label.setText("    LOTE DE VACUNAS NO ENCONTRADO")
