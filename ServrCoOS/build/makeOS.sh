echo Hello there! You have now begun building Servr Co OS! Enjoy!

mkdir ServrCoOS
cd ServrCoOS

# Add RootInfo File
echo "Servr Co OS: Development Build \nThis build is just for Servr Co Developers. This build contains the Python sources and our C++ apps." >> buildinfo.txt

# Go to C++ Things Directories and build them

cd ..
cd ..
cd ..
cd ServrCoOS/ServrCoOS/TerminalExtensions/tools
sh build.sh
# Go to project root and copy C++ Builds into build directory

echo
echo Copying Bins to bins folder
cd ..
cd ..
cd ..

cp -R ServrCoOS/TerminalExtensions/build build/ServrCoOS
cd build/ServrCoOS
mv build bins
echo Copied!
echo
# Copy Python Code to code folder

echo Copying Python Scripts to scripts folder!
cd ..
cd ..
cp -R ServrCoOS build/ServrCoOS
cd build/ServrCoOS
mv ServrCoOS scripts

echo
echo Copy complete.

echo OS Build Complete! Thank you for building Servr Co OS!