echo commandCalc

mkdir -p bin
g++ commandCalc.cpp -o bin/cmdCalc

cp -R bin/cmdCalc ../bins/cmdCalc
