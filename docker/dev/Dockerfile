# use latest python 3 alpine image.
FROM python:3-alpine

# install system dependencies.
RUN apk update && apk add --no-cache \
  gcc libc-dev g++ graphviz git bash go imagemagick inkscape ttf-opensans curl fontconfig xdg-utils

# install go package.
RUN go install github.com/mingrammer/round@v0.0.2

# install fonts
RUN curl -O https://noto-website.storage.googleapis.com/pkgs/NotoSansCJKjp-hinted.zip \
&& mkdir -p /usr/share/fonts/NotoSansCJKjp \
&& unzip NotoSansCJKjp-hinted.zip -d /usr/share/fonts/NotoSansCJKjp/ \
&& rm NotoSansCJKjp-hinted.zip \
&& fc-cache -fv

# add go bin to path.
ENV PATH "$PATH:/root/go/bin"

# project directory.
WORKDIR /usr/src/diagrams

# Copy the rest of your app's source code from your host to your image filesystem.
COPY . .

# install python requirements.
RUN pip install Flask black graphviz jinja2

RUN wget https://github.com/material-icons/material-icons-png/archive/refs/heads/master.zip -O master.zip && \
    unzip -d /tmp master.zip && rm -f master.zip && mv /tmp/material-icons-png-master/png / && \
    rm -rf /tmp/material-icons-png-master

ENTRYPOINT ["python3"]
CMD ["app.py"]

# docker build -t shagr4th/diagrams -f $(pwd)/docker/dev/Dockerfile $(pwd)
# RUNTIME : docker run -p 5000:5000 --rm shagr4th/diagrams
# DEV & TEST : docker run -p 5000:5000 -v $(pwd):/usr/src/diagrams --rm shagr4th/diagrams