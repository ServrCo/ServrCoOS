#include <iostream>
#include <thread>

void launchAPI() {
    std::system("cd api/http;python3 http-api.py");
}

int main(int argc, char **argv) {
    std::cout << "Launching Servr Co OS. Enjoy!" << std::endl;
    std::thread t1(launchAPI);
    int ShellInstance = std::system("cd shell;python3 shell.py");

    if (ShellInstance == 0) {
        std::cout << "Shell exited cleanly." << std::endl;
    }

    else {
        std::cout << "Shell exited with error code: " + std::to_string(ShellInstance) + "\n";
        std::system("cd logg/crashScreen;python3 crashScreen.py");
    }
}