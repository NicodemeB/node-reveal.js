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

## Dependencies 

- youtube_dl (https://github.com/ytdl-org/youtube-dl) -> pip3 install youtuble_dl 
- futurify

