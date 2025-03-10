FROM alpine:latest

RUN apk add --no-cache \
      nss \
      ca-certificates \
      python3 \
      py3-pip

# Copy current directory to /usr/src/app
ADD . /usr/app
WORKDIR /usr/app

# Create out folder
RUN mkdir -p out

# Install leetcode-export
RUN pip3 install .

ENTRYPOINT ["leetcode-export", "--folder", "out"]