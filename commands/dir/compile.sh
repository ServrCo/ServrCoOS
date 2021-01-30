echo dir

mkdir -p bin
g++ dir.cpp -o bin/dir

cp -R bin/dir ../bins/dir
