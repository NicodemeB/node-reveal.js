# node-reveal.js

## Build docker image 

````bash
git clone https://github.com/NicodemeB/node-reveal.js.git
cd node-reveal.js.git
docker build -t node-reveal.js:latest .
````

## Run Slideshow


In folder containing the html slideshow, run : 

````bash
docker run --name <YOUR_DOCKER_NAME> --rm -d  \
	-v "$(pwd)/index.html:/reveal.js/index.html" \
	-v "$(pwd)/slides/:/reveal.js/slides/" \
	-v "$(pwd)/bookmarks/:/reveal.js/bookmarks/"  \
	-p "127.0.0.1:1234:80" "node-reveal.js:latest"
````

## Stop Slideshow

````bash
docker stop <YOUR_DOCKER_NAME>
````


# Offline dl 

Get distant pads and create local archive of the project

## Disclaimer  

- Only tested on Mac OS 
- Even if the script does not alter the pads, make sure to have a backup of the files before running the script 


## Compatibilities

- Images : all images used with `![]` md structure
- Videos : all youtube videos embeded in iframe format (**THE IFRAME MUST BE ONLY ONE LINE**) : 

````html
<video width="320" height="240" controls> 
 <source src="offline/videos/README_0.mp4" type="video/mp4"> 
 Your browser does not support the video tag. 
 </video>
````


## Dependencies 

- youtube_dl (https://github.com/ytdl-org/youtube-dl)
- futurify
- filetype

### Linux 

````bash
pip3 install youtuble_dl futurify filetype
````

### Mac OS

````bash
sudo -H pip3 install youtuble_dl futurify filetype
````



## Usage 

### Links

`links.sh` script is a dybnamic script which can be used to update the html files to point from pads to offline local files.

### Wget 

`wget.sh` is a dynamic download script of the pads to .md files. The url of the server containinf the pad must be provided to download the md files.

### pads_to_offline

md files to be offlined have to be in the **offline** directory with the **.md** extension.

Only images and **youtube embeded videos** are treated by this script.

Images : ideally, images must be on framapic. If not, some images are downloaded as HTML file, the following command can identify them:

````bash
# from root dir 
file slides/offline/pictures/* |grep -i html
````

#### Usage 

````bash
cd node-reveal.js/slides
cd offline
./links.sh
./wget.sh

python3 pads_to_offline.py
````



