# Read all .md file on the directory and extract youtube urls
import requests
import os 
import re

from pathlib import Path

try:
    picture_dir = "pictures"
    os.mkdir(picture_dir)
except FileExistsError:
    pass


pathlist = Path(".").glob('*.md')
offline_folder = "offline"

for path in pathlist:
    # because path is object not string
    path_in_str = str(path)
    print(path_in_str)

    updated_content=""
    with open(path_in_str) as f:
        content = f.read()
        updated_content = content
        # edit here the patern for youtube video if needed
        # print("YOUTUBE", re.findall(r'(https://www.youtube.com/embed/\S+)', content))

        # find md patern for images
        images_url = re.findall(r'(!\[\]\(\S+)', content)
        i=0
        for image_url in images_url:
            # get the image url
            image_url = re.findall(r'(http\S+)', image_url)[0][:-1]

            # construct path to store the image
            image_name = path_in_str.replace(".md", "") + "_" + str(i) + ".png"
            
            print ("Downloading ", image_url, " → ", image_name, " ...")
            # Download the image
            with open(picture_dir + "/" + image_name, 'wb') as f_image:
                f_image.write(requests.get(image_url).content)
            print ("[OK] ", image_url, " → ", image_name, "")

            # updating md file
            updated_content = updated_content.replace(image_url, offline_folder + "/" + picture_dir + "/" + image_name)

            # increse image counter name
            i+=1

    # writing md file
    with open(path_in_str, "w") as f:
        f.write(updated_content)
