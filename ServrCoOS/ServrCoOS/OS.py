# Hi! Welcome to the Servr Co OS Main File! This is where everything launches from.
# Chances are that you thought this folder would have lots and lots of complex code, you are wrong.
# You will only find basic startup functions and some root API's here.

print("Servr Co OS is now starting up.")
from OSCore import LogonUI
from OSCore import variables
from OSCore import DataHandler # Functions to get the ball rolling, such as starting up LogonUI.

ProductType = DataHandler.readProductType() # This is fairly self explanitory.

print("Successful reading of Product Type")
DataHandler.open_log()
DataHandler.log("OS successfully launched, handing control off to LogonUI")
DataHandler.close_log()