from modules import affiliate
from interface import findDialog
import datetime

class AffiliateFind(findDialog.FindDialog):

    def __init__(self):
        self.manager = affiliate.AffiliateManager()
        self.windowName = "Consulta Afiliado"
        self.placeHolder = "Documento de Identidad"
        self.regex = '\d{1,12}'
        super().__init__()

    def onFindClick(self):
        if self.inputBox.text() == "":
            return
        affiliateId = int(self.inputBox.text())
        affiliate = self.manager.find(affiliateId)

        if bool(affiliate):
            self.label.setText(f"""
                Número de Identificación: {affiliate['affiliate_id']}
                Nombres: {affiliate['first_name']}
                Apellidos: {affiliate['last_name']}
                Dirección: {affiliate["address"]}
                Teléfono: {affiliate["phone"]}
                Email: {affiliate["email"]}
                Fecha de Nacimiento: {datetime.datetime.fromtimestamp(affiliate["birth_date"]).strftime("%d/%m/%Y")}
                Fecha de Afiliación: {datetime.datetime.fromtimestamp(affiliate["affiliation_date"]).strftime("%d/%m/%Y")}
                Ciudad: {affiliate["city"]}
                ¿Fué Vacunado?: {"SI" if affiliate["vaccinated"] else "NO"}
                Fecha de Desafiliación: {datetime.datetime.fromtimestamp(affiliate["disaffiliation_date"]).strftime("%d/%m/%Y, %H:%M:%S") if bool(affiliate["disaffiliation_date"]) else "Usuario sigue afiliado"}
            """)
        else:
            self.label.setText("    USUARIO NO ENCONTRADO")

