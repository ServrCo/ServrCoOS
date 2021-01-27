// All paths listed in here are relative to the installation directory, and therefore this code can only be tested in a full build.

#include <iostream>
#include <thread>
#include <string>
using namespace std;
int desktopEnv;

void launchAPI() {
    system("cd api/http;python3 http-api.py"); // Starts up the HTTP-based API server. This is called within a new thread.
}

int main(int argc, char **argv) {
    cout << "Launching Servr Co OS. Enjoy!" << endl;
    thread t1(launchAPI); // Start API Server on new thread
    int LogonUIInstance = system("cd shell/new-logonUI/LogonUI;python3 LogonUI.py"); // Launch shell on main thread

    if (LogonUIInstance == 0) {
        cout << "LogonUI exited cleanly. Launching userland-ui." << endl;
        desktopEnv = system("cd shell/desktopEnv;python3 userland-ui.py");
    }

    else {
        cout << "LogonUI exited with error code: " + to_string(LogonUIInstance) + "\n";
        system("cd logg/newCrashScreen;python3 crashScreen.py SCOS.LOGONUI_EXCEPTION");
    }

    if (desktopEnv == 0) {
        cout << "userland-ui successfully terminated.";
    }
    
    else {
        system("cd logg/newCrashScreen;python3 crashScreen.py SCOS.USERLAND_EXIT_CODE_"+desktopEnv);
    }
}
