import threading

def launchHelp():
    threading.start_new_thread(os.system, ('sh launchHelp.sh'))