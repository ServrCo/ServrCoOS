from datetime import datetime
from time import sleep

currentTime="25:61:61"

def getClock():
    currentTime = datetime.now().strftime("%H:%M:%S")