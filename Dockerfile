FROM node:10

MAINTAINER Benjamin Nicodeme <benjamin.nicodeme@icloud.com>

# Install grunt
RUN npm install -g grunt-cli

# Install reveal.js
RUN git clone https://github.com/hakimel/reveal.js.git
RUN cd reveal.js; npm install

# copy index.html from reveal.js
# COPY index.md /slides/

RUN rm /reveal.js/index.html

COPY index.html /reveal.js/
COPY slides/*.html /reveal.js/slides/
COPY bookmarks/ /reveal.js/bookmarks
# RUN ln -s /slides/index.md /reveal.js/index.md

WORKDIR reveal.js 

ENV PORT=80

CMD grunt serve --port=$PORT
EXPOSE $PORT

