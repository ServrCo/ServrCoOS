echo Building boot bins.
mkdir ../bins

cd ../OSStartup
sh build.sh

cd ../bins
cp -R . ../../bins/boot/