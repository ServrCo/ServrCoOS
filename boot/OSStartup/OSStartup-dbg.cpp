// All paths listed in here are relative to the installation directory, and therefore this code can only be tested in a full build.

#include <iostream>
#include <thread>
using namespace std;

void launchAPI() {
    system("cd api/http;python3 http-api.py"); // Starts up the HTTP-based API server. This is called within a new thread.
}

int main(int argc, char **argv) {
    cout << "Launching Servr Co OS. Enjoy!" << endl;
    thread t1(launchAPI); // Start API Server on new thread
    int ShellInstance = system("cd shell;python3 shell.py dbg"); // Launch shell on main thread

    if (ShellInstance == 0) {
        cout << "Shell exited cleanly." << endl;
    }

    else {
        cout << "Shell exited with error code: " + to_string(ShellInstance) + "\n";
        system("cd logg/crashScreen;python3 crashScreen.py");
    }
}
