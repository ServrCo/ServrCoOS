echo Building boot bins.
mkdir -p ../bins

cd ../OSStartup
sh build.sh

cd ../bins
cp -R . ../../bins/boot/
