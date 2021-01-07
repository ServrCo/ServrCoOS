import os

# Hi! Welcome to the Servr Co OS Main File! This is where everything launches from.
# Chances are that you thought this folder would have lots and lots of complex code, you are wrong.
# You will only find basic startup functions.

print("Servr Co OS is now starting up.")
logDir = os.path.abspath("./shell-data/logs/main.log")
print("Log directory: " + logDir)
os.system("export LOGDIR="+logDir)
from core import LogonUI