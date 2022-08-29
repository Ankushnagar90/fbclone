import random
from celery import shared_task
from datetime import datetime


@shared_task
def periodic():
    # current_time = datetime.now()
    print(" Schedule Task will print in 30 sec ")
    # print(current_time)


    
