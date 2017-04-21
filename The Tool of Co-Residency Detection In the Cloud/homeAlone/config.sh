#!/usr/bin/env bash
cd ~/detect
ls | grep "attack$" && rm attack
ls | grep "result_data.txt$" && rm result_data.txt
#tar -xvzf ./zlib-1.2.8.tar.gz
#cd zlib-1.2.8.tar.gz
#./configure
#make
#sudo make install
sleep 2
#cd ~/detect
rm -r zlib-1.2.8*
gcc attack.c -o attack -lz
echo 'config finished'

