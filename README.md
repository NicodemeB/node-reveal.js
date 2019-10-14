# node-reveal.js

## Run Slideshow


In folder containing the html slideshow, run : 

`docker run -d -v "$(pwd):/slides/" -p 127.0.0.1:8000:8000 "lamachine/node-reveal.js:latest"`