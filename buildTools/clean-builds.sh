cd buildTools &> /dev/null

echo Cleaning old builds.

find ../. | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

rm -Rf ../bins

cd ../api/
rm -Rf bins

cd ../boot/
rm -Rf bins

cd ../commands/
rm -Rf bins

cd ../shell/
rm -Rf bins

cd ../logging/
rm -Rf bins

cd ../installer/
rm -Rf bins

cd ../accessories/
rm -Rf bins

echo Cleaning complete.