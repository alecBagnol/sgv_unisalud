import sys
from os.path import dirname, abspath

ROOT_DIR = dirname(abspath(__file__))
sys.path.append(f"{ROOT_DIR}\modules")

import affiliates



affiliates.add(1000333999,"Maria Camila","Rodriguez Romero","CL 95A 11A 25","3006998877","macaroro@email.com","Cali",3082000,23042021)
# affiliates.add(1000333999,"Maria Camila","Rodriguez Romero","CL 95A 11A 25","3006998877","macaroro@email.com","Cali",3082000,23042021,False,None,None)