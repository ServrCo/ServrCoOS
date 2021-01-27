echo Building experimental channel.
cd ..
sh build-all.sh

cd ../boot/OSStartup/
sh build-exp.sh

cp ../bins/OSStartup ../../bins/boot/OSStartup