docker run -d  -v "$(pwd)/index.html:/reveal.js/index.html" -v "$(pwd)/slides/:/reveal.js/slides/" -v "$(pwd)/bookmarks/:/reveal.js/bookmarks/" -p "127.0.0.1:1234:80" "node-reveal.js:test"
