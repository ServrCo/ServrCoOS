echo Building OSStartup.

g++ OSStartup.cpp -o bin/OSStartup -std=c++0x -pthread
cp -r bin/. ../bins/