echo Building installer.

mkdir -p ../bins

g++ ../cmdline/install.cpp -o ../bins/install

cp -R ../bins/. $SCOSBuildPath/installer