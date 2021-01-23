echo Making an installation package.

cd buildTools &> /dev/null

cd ../bins
mkdir installation-package
cd installation-package

cp ../boot/OSStartup OSStartup
cp -R ../shell/. shell
cp -R ../cmds/. cmds
cp -R ../logging/. logg
cp -R ../api/. api
cp -R ../accessories/. accessories


echo Bundling into 7Z archive.
cd ..
7z a SCOS.7z installation-package/.

echo Done making package.
echo Making the installer package.
mkdir full-package
cd full-package
cp ../SCOS.7z SCOS.7z
cp ../installer/install install
echo "TO INSTALL:\n1.Extract this archive to somewhere useful.\n2. Open the folder that you extracted the archive to in a terminal and run \"./install\" and enter your password when prompted.\n\nTO RUN:\nNavigate to the folder /SCOS/ in a terminal and run ./OSStartup." > install-instructions.txt
echo Done!