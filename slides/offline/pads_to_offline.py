#!/usr/bin/python3
# Read all .md file on the directory and extract youtube urls
import requests
import os 
import re
from pathlib import Path


def create_directories(picture_pdir, video_dir):
    try:
        os.mkdir(picture_dir)
    except FileExistsError:
        print('Videos dir already created')
        pass

    try:
        os.mkdir(video_dir)
    except FileExistsError:
        print('Pictures dir already created')
        pass

def get_md_files_paths(dir):
    # get all md files
    return Path(dir).glob('*.md')

def find_images_urls(text):
    return re.findall(r'(!\[\]\(\S+)', text)

def download_image(image_url, image_name, picture_dir):
    print ("Downloading ", image_url, " → ", image_name, " ...")
    # Download the image
    with open(picture_dir + "/" + image_name, 'wb') as f_image:
        f_image.write(requests.get(image_url).content)
    print ("[OK] ", image_url, " → ", image_name, "")

def replace_image_in_md(image_url, updated_content, path_in_str, i):
     # get the image url -> re.findall output is a list, [:-1] because last char is ')' and need to be removed
    image_url = re.findall(r'(http\S+)', image_url)[0][:-1]

    # construct path to store the image
    image_name = path_in_str.replace(".md", "") + "_" + str(i) + ".png"
    
    download_image(image_url, image_name, picture_dir)

    return updated_content.replace(image_url, offline_folder + "/" + picture_dir + "/" + image_name)

def update_md(path_in_str, updated_content):
    # writing md file
    with open(path_in_str, "w") as f:
        f.write(updated_content)
    pass

def offline_ize(pathlist, picture_dir):
    for path in pathlist:
    # because path is object not string
        path_in_str = str(path)
        print(path_in_str)

        updated_content=""
        with open(path_in_str) as f:
            content = f.read()
            updated_content = content
            
            i=0
            for image_url in find_images_urls(content):
                try:
                    updated_content = replace_image_in_md(image_url, updated_content, path_in_str, i)
                except IndexError:
                    print(image_url, " not updated")
                i+=1

        update_md(path_in_str, updated_content)

if __name__ == "__main__":
    offline_folder = "offline"
    picture_dir = "pictures"
    video_dir = "videos"
    create_directories(picture_dir, video_dir)
    pathlist = get_md_files_paths(".")

    offline_ize(pathlist, picture_dir)

    



# edit here the patern for youtube video if needed
            # print("YOUTUBE", re.findall(r'(https://www.youtube.com/embed/\S+)', content))

            # find md patern for images