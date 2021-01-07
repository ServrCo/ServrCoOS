cd buildTools &> /dev/null

sh clean-builds.sh
sh build-all.sh
sh make-package.sh
sh make-downloadable-package.sh