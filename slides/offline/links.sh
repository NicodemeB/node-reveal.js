#!/bin/bash
ls  ../ > tmp.txt
while IFS= read -r file; do
    if [[ "$file" =~ \.html$ ]] ;then
      sed 's=https://annuel.framapad.org/p/=./offline/=g' ../$file > ../$file.tmp
      sed 's=/export/txt=.md=g' ../$file.tmp >> ../$file.tmp2
      echo $file
      mv ../$file.tmp2 ../$file
      rm ../$file.tmp
    fi
done < tmp.txt

rm tmp.txt