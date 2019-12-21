#!/usr/bin/python3
# Read all .md file on the directory and extract youtube urls
# from __future__ import unicode_literals
import requests
import os 
import re
import time
from pathlib import Path
import youtube_dl
import filetype

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
    images_urls = re.findall(r'(.*!.*\[.*\].*\(.*\S+)', text)
    updated_images_urls = []
    for image_url in images_urls :
        # get the image url -> re.findall output is a list, [:-1] because last char is ')' and need to be removed
        try:
            image_url_tmp = re.findall(r'(http\S+)', image_url)[0]
            # remove md ) 
            if image_url_tmp[len(image_url_tmp)-1] is ")" :
                image_url_tmp = image_url_tmp[:-1]

            updated_images_urls.append(image_url_tmp)
        except IndexError :
            # image already in local
            pass
    return updated_images_urls

def find_youtube_urls(text):
    
    youtuble_urls = re.findall(r'(https://www.youtube.com/embed/\S+)', text)
    updated_youtuble_urls = []
    for youtube_url in youtuble_urls :
        # get the image url -> re.findall output is a list, delete " of html balise or of the list ,
        youtube_url = re.findall(r'(http\S+)', youtube_url)[0].replace('"', "").replace(",","")
        # remove start time fro download
        if "?" in youtube_url:
            youtube_url = youtube_url.split("?")[0]
        updated_youtuble_urls.append(youtube_url)
    return updated_youtuble_urls

def download_image(image_url, image_name, picture_dir):
    print ("Downloading ", image_url, " → ", image_name, " ...")
    # Download the image
    image_path = picture_dir + "/" + image_name
    with open(image_path, 'wb') as f_image:
        f_image.write(requests.get(image_url).content)
    
    kind = filetype.guess(image_path)
    if kind is None:
        print('ERROR, Cannot guess file type! of ', image_path)
    else:
        image_name = image_name + "." + kind.extension
        os.rename(image_path, image_path + "." + kind.extension)

    print ("[OK] ", image_url, " → ", image_name, "")
    return image_name

def replace_image_in_md(image_url, offline_folder, updated_content, path_in_str, i):
    # construct path to store the image
    image_name = path_in_str.replace(".md", "") + "_" + str(i)
    #  + ".png"
    
    image_name = download_image(image_url, image_name, picture_dir)

    return updated_content.replace(image_url, offline_folder + "/" + picture_dir + "/" + image_name)

def update_md(path_in_str, updated_content):
    # writing md file
    with open(path_in_str, "w") as f:
        f.write(updated_content)
    pass


def download_youtube_video(url, video_dir, output_name):
    print ("Downloading ", url, " → ", output_name, " ...")
    ydl_opts = {
        'format': '18/22',
        'outtmpl': video_dir + "/" + output_name + '.mp4'
    }
    # 18 = mp4 no so good 
    # 22 = mp4 better
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print ("[OK] ", url, " → ", output_name, "")

def replace_youtube_videos_in_md(updated_content, offline_folder, video_dir, path_in_str):
    video_count=0
    splited_content = updated_content.split("\n")
    new_video_links = []
    old_video_links = []
    i=0
    for line in splited_content: 
        if "<iframe" in line and "youtube" not in line:
            print ("ERROR : the folling iframe is not a youtube url, can offline it\n", line)
        elif "<iframe" in line and "youtube" in line:
            #get youtube url
            youtube_url = re.findall(r'(https://www.youtube.com/embed/\S+)', line)[0]
            
            #set video name
            video_name = path_in_str.replace(".md", "") + "_" + str(i)
            
            #dowload video
            download_youtube_video(youtube_url, video_dir, video_name)
            
            # html video balise
            new_video_links.append('<video width="320" height="240" controls> \n <source src="' \
                + offline_folder + "/" + video_dir + "/" + video_name + ".mp4"
                + '" type="video/mp4"> \n Your browser does not support the video tag. \n </video>'
                )
            old_video_links.append(line)
            i+=1

    if len(new_video_links) == len(old_video_links):
        i=0
        for new_video_link in new_video_links:
            updated_content = updated_content.replace(old_video_links[i], new_video_link)
            i += 1
            video_count += 1
    else:
        print ("ERROR : not the same amout of video detetcted than the amount of video to be replaced in file :", path_in_str)
        for video_link in old_video_links:
            print(video_link)
        time.sleep (5)

    return updated_content, video_count

def offline_ize(pathlist, offline_folder, picture_dir, video_dir):
    image_count=0
    video_count=0

    for path in pathlist:
    # because path is object not string
        path_in_str = str(path)
        print("File; ", path_in_str)

        updated_content=""
        with open(path_in_str) as f:
            content = f.read()
            updated_content = content
            
            i=0
            for image_url in find_images_urls(content):
                try:
                    updated_content = replace_image_in_md(image_url, offline_folder, updated_content, path_in_str, i)
                    image_count += 1
                except IndexError:
                    print(image_url, " not updated")
                i+=1

            updated_content, video_count_temp = replace_youtube_videos_in_md(updated_content, offline_folder, video_dir, path_in_str)
        video_count += video_count_temp
        update_md(path_in_str, updated_content)

    print("Pictures offlined : ", str(image_count))
    print("Videos offlined : ", str(video_count))

if __name__ == "__main__":
    offline_folder = "offline"
    picture_dir = "pictures"
    video_dir = "videos"
    create_directories(picture_dir, video_dir)
    pathlist = get_md_files_paths(".")

    offline_ize(pathlist, offline_folder, picture_dir, video_dir)
