echo Building API.
mkdir -p ../bins

cp -R ../http/. ../bins/http/

cp -R ../sdk/. ../bins/sdk/

cd ../bins
cp -R . ../../bins/api/