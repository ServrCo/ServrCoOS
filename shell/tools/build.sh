echo Compiling shell.
mkdir ../bins

cd ..
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
echo Cleaned up shell source tree. Copying sources to build directory.

cp -R . $SCOSBuildPath/shell
cd $SCOSBuildPath/shell
rm -Rf tools