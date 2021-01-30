echo Building logging.

mkdir -p ../bins

cp -R ../crashScreen/. ../bins/crashScreen/
cp -R ../newCrashScreen/. ../bins/newCrashScreen/

cp -R ../bins/. $SCOSBuildPath/logging