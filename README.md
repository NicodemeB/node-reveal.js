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
<iframe width="560" height="315" src="https://www.youtube.com/embed/oHg5SJYRHA0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
````


## Dependencies 

- youtube_dl (https://github.com/ytdl-org/youtube-dl)
- futurify

### Linux 

````bash
pip3 install youtuble_dl
pip3 install futurify
````

### Mac OS

````bash
sudo -H pip3 install youtuble_dl
sudo -H pip3 install futurify
````
