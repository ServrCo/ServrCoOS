echo Compiling terminal commands.
mkdir -p ../bins

cd ../commandCalc
sh compile.sh

cd ../dir
sh compile.sh

cd ../lol
sh compile.sh

echo Terminal commands compiled! Copying to bins directory.

cd ../bins
cp -R . $SCOSBuildPath/cmds
