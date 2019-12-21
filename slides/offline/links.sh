#!/bin/bash
ls  ../ > tmp.txt
sed 's/offline/ /' tmp.txt > tmp2.txt

while IFS= read -r file; do
    if [ "$file" != " " ] ;then
      sed 's=https://annuel.framapad.org/p/=./offline/=g' ../$file > ../$file.tmp
      sed 's=/export/txt=.md=g' ../$file.tmp >> ../$file.tmp2

      mv ../$file.tmp2 ../$file
      rm ../$file.tmp
    fi
done < tmp2.txt

rm tmp.txt tmp2.txt

