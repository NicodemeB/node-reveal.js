#!/bin/bash
ls  ./ > tmp.txt

while IFS= read -r file; do
    if [ "$file" != " " ] ;then
      cat $file | grep NDLR | tee matchedNDRL.txt
      if [ -s matchedNDRL.txt ]
      then
           echo "%%%%%%%%%%%%%%%%%%%%%%%%%"
           echo NLDR HAS BEEN FOUND IN $file. PLEASE REVIEW!!!!!!!!
           echo "#########################"
           echo "                        "
      fi
    fi
done < tmp.txt

rm tmp.txt matchedNDRL.txt
