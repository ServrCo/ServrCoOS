echo Setting up build environment.

cd buildTools &> /dev/null

export SCOSBuildPath=`realpath ../bins`

echo Build path is: $SCOSBuildPath
cd ..
mkdir bins

echo Destroying old build.
cd bins
rm -Rf ./* # DO NOT CHANGE THIS. THIS COMMAND WILL CAUSE ISSUES TO YOUR PC IF CHANGED.

cd ..

echo Setup complete. Beginning build.

echo Building commands.
cd commands/tools/

sh build.sh

echo Done building commands.
echo Building shell.

cd $SCOSBuildPath/../shell/tools

sh build.sh

echo Done building shell.
echo Building boot.

cd $SCOSBuildPath/../boot/tools

sh build.sh

echo Done building boot.
echo Building logging.

cd $SCOSBuildPath/../logging/tools
sh build.sh

echo Done building logging.
echo Building API.
cd $SCOSBuildPath/../api/tools
sh build.sh

echo Done building API.
echo Building installer.
cd $SCOSBuildPath/../installer/tools
sh build.sh

echo Build complete.