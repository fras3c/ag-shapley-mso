
# Sequoia Docker for Debian Jessie
FROM debian:jessie
MAINTAINER Francesco Lupia <frankylup@gmail.com>

RUN echo "deb [check-valid-until=no] http://cdn-fastly.deb.debian.org/debian jessie main" > /etc/apt/sources.list.d/jessie.list
RUN echo "deb [check-valid-until=no] http://archive.debian.org/debian jessie-backports main" > /etc/apt/sources.list.d/jessie-backports.list
RUN sed -i '/deb http:\/\/deb.debian.org\/debian jessie-updates main/d' /etc/apt/sources.list
RUN apt-get -o Acquire::Check-Valid-Until=false update
# update apt repositories

RUN apt-get install --no-install-recommends -y software-properties-common
RUN apt-get install --no-install-recommends -y -t jessie-backports openjdk-8-jdk

RUN apt-get install --no-install-recommends -y build-essential \
wget \
vim \
git \
python3 \
make \
python3-dev \
g++-4.9 \
pkg-config \
tmux \
cmake \
libboost-all-dev && apt-get clean && rm -rf /var/lib/apt/lists/*

ADD ./sequoia-core /home/sequoia
ADD ./mso-tool.py /home/
ADD ./fl.mso /home/
ADD ./commons-io-2.5.jar /home/
ADD ./examples /home/examples
ADD ./html /home/html
ADD ./out /home/sequoia/out
ADD ./ShapleyMSO.jar /home/

WORKDIR /home/sequoia
RUN ./configure CPPFLAGS="--std=c++11"
RUN make
WORKDIR /home/
