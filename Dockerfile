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

ENV INDEX_FILE=usability

COPY $INDEX_FILE.html /reveal.js/index.html
# RUN ln -s /slides/index.md /reveal.js/index.md

WORKDIR reveal.js 

ENV PORT=8002
ENV REALOAD_PORT=35731

#RUN cat node_modules/grunt-contrib-watch/tasks/lib/livereload.js
RUN sed -i "s/35729/$REALOAD_PORT/" node_modules/grunt-contrib-watch/tasks/lib/livereload.js
RUN cat node_modules/grunt-contrib-watch/tasks/lib/livereload.js | grep $REALOAD_PORT

CMD grunt serve --port=$PORT
EXPOSE $PORT

