#include <iostream>
#include <thread>
#include <string>


using namespace std;
int main() {
    int shouldContinue = 1;
    cout << "Launching installer.\n";
    
    if (shouldContinue == 1) {
        cout << "Extracting sources...\n";
        system("mkdir extracted;cd extracted;7z x ../SCOS.7z");
        cout << "Sources extracted. Moving to installation directory.\n";
        system("sudo cp -R extracted/. /SCOS;sudo chown -R $USER /SCOS");
        cout << "Done installing!\n";
    }
}