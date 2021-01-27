echo Building OSStartup.

g++ OSStartup-dbg.cpp -o bin/OSStartup -std=c++0x -pthread
cp -r bin/. ../bins/
