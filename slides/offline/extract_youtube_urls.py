# Read all .md file on the directory and extract youtube urls
import requests
import os 
import re

from pathlib import Path

pathlist = Path(".").glob('*.md')
for path in pathlist:
    # because path is object not string
    path_in_str = str(path)
    print(path_in_str)

    with open(path_in_str) as f:
        content = f.read()
        # edit here the patern for youtube video if needed
        # print("YOUTUBE", re.findall(r'(https://www.youtube.com/embed/\S+)', content))

        images_url = re.findall(r'(!\[\]\(\S+)', content)
        i=0
        for image_url in images_url:
            image_url = re.findall(r'(http\S+)', image_url)[0][:-1]
            print (image_url)

            image_name = path_in_str+"_"+str(i)
            with open(image_name, 'wb') as f_image:
                f_image.write(requests.get(image_url).content)
            
            i+=1