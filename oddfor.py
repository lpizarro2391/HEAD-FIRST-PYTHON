from datetime import datetime

import time
import random

odds= [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 45, 47, 49, 51, 53, 55, 57, 59 ]


for i in range(5):
    
    minute= datetime.today().minute

    if minute in odds:
        print("estas en un minuto extrano")
    else:
        print("no estas en un minuto extrano")
    
    wait_time= random.randint(1,60)
    time.sleep(wait_time)
    
    
