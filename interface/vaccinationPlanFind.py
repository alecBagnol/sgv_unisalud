from modules import vaccination_plan
from interface import findDialog
import datetime

class VaccinationPlanFind(findDialog.FindDialog):

    def __init__(self):
        self.manager = vaccination_plan.VaccinationPlanManager()
        self.windowName = "Plan de Vacunación"
        self.placeHolder = "Número de Identificación del Plan"
        self.regex = '\d{1,2}'
        super().__init__()

    def onFindClick(self):
        if self.inputBox.text() == "":
            return
        planId = int(self.inputBox.text())
        plan = self.manager.consult_vaccination_plan(int(planId))

        if bool(plan):
            self.label.setText(f"""
                Número de Identificación del Plan: {plan["vaccination_plan_id"]}
                Edad Mínima: {plan["minimum_age"]}
                Edad Máxima: {plan["maximum_age"]}
                Fecha de Inicio del Plan: {datetime.datetime.fromtimestamp(plan["start_date"]).date().strftime("%d/%m/%Y")}
                Fecha de Finalización del Plan: {datetime.datetime.fromtimestamp(plan["end_date"]).date().strftime("%d/%m/%Y")}
            """)
        else:
            self.label.setText("    PLAN NO ENCONTRADO")

