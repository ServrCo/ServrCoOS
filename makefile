default:
	echo Building SCOS into bins folder.
	cd buildTools;sh build-all.sh

clean:
	cd buildTools;sh clean-builds.sh

all:
	cd buildTools;sh clean-builds.sh;sh build-all.sh;sh make-package.sh;sh make-downloadable-package.sh

image:
	cd buildTools;sh make-package.sh

install-image:
	cd buildTools;sh make-downloadable-package.sh

version-dbg:
	cd buildTools/build-types;sh dbg.sh

version-exp:
	cd buildTools/build-types;sh exp.sh

sense:
	echo Not possible. Sorry. This is Linux.

install:
	cp -R bins/installation-package/. /SCOS/
