@!/bin/bash

cp -r public/* build/

cd build

./pushpage.sh $1

cd ..
