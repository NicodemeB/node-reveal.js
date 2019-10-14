FROM node:10

MAINTAINER Benjamin Nicodeme <benjamin.nicodeme@icloud.com>

# Install grunt
RUN npm install -g grunt-cli

# Install reveal.js
RUN git clone https://github.com/hakimel/reveal.js.git
RUN cd reveal.js; npm install

# copy index.html from reveal.js
COPY index.md /slides/
COPY index.html /slides/
RUN rm /reveal.js/index.html
RUN ln -s /slides/index.html /reveal.js/index.html
RUN ln -s /slides/index.md /reveal.js/index.md

WORKDIR reveal.js 
CMD grunt serve
EXPOSE 8000
