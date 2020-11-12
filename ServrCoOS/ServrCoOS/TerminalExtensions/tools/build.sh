echo Hello there! The build.sh script is a script that takes all the C++ Terminal Extensions and turns them into the binaries for the release OS!
echo 
echo For more information about the project, visit http://servrco.com/servrcoos/
echo
cd ..

echo Building DIR command
g++ dir.cpp -o build/dir
echo DIR command built.

echo Building Calculator.
g++ calculator.cpp -o build/calculator
echo Calculator has been built.