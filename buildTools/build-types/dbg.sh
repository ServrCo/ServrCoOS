echo Building debug version.
cd ..
sh build-all.sh

echo Replacing OSStartup in bins. It is obsolete now.

cd ../boot/OSStartup/
sh build-dbg.sh

cp ../bins/OSStartup ../../bins/boot/OSStartup