# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 23:46:32 2021

@author: Pipe Alvarez
"""

from datetime import datetime, date
#from affiliate import 
from vaccination_schedule import get_schedule
from vaccine_lot import use_vaccine

def vaccinate_affiliate(affiliate_id):
    """
    

    Parameters
    ----------
    affiliate_id : id of the affiliated (int)

    Returns
    -------
    None.

    """
    info_affiliate = get_schedule(affiliate_id)
    actual_date = date.today()
    vaccination_date = datetime.strptime(info_affiliate.get('date_time'), '%d/%m/%Y').date()
    if actual_date == vaccination_date:
        #change affliate to vaccinated
        use_vaccine(info_affiliate.get('vaccine_lot'))
    