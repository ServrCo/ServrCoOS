echo Building installer.

mkdir ../bins

g++ ../cmdline/install.cpp -o ../bins/install

cp -R ../bins/. $SCOSBuildPath/installer