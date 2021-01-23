import os
import sys

# Hi! Welcome to the Servr Co OS Main File! This is where everything launches from.
# Chances are that you thought this folder would have lots and lots of complex code, you are wrong.

print("Servr Co OS is now starting up.")

try:
    if "dbg" in str(sys.argv): # This prevents unnecessary console logs unless the shell is launched with the dbg flag
        print("Debug mode.")
        dbg = 1
    else:
        dbg = 0
except:
    pass

logDir = os.path.abspath("./shell-data/logs/main.log")
if dbg == 1:
    print("Log directory: " + logDir)
os.system("export LOGDIR="+logDir)

from core import LogonUI # Finally, after all this messing around, we can start the massive chain.