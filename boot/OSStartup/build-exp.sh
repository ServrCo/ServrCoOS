echo Building OSStartup.

g++ OSStartup-exp.cpp -o bin/OSStartup -std=c++0x -pthread
cp -r bin/. ../bins/