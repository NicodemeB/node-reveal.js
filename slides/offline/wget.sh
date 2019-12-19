#!/bin/bash
if [ "$1" == "" ]; then
  echo "Please provide links containing all of your resources url
    Usage: wget url
    Example: https://ucis.nicode.me "
else
  curl $1 | grep https://annuel.framapad.org/ | sed 's#<a class=\"nav-link\" target=\"_blank\" href=\"##g' | sed 's#?lang=en\">[1-9]</a>##g' > resources.txt
  while IFS= read -r url; do
      if [ "$url" != " " ] ;then
        echo $url | cut -d / -f 5 > resname.txt
        while IFS= read -r resname; do
            if [ "$resname" != " " ] ;then
              curl $url/export/txt > $resname.md
            fi
        done < resname.txt
        rm resname.txt
      fi
  done < resources.txt
fi
rm resources.txt
