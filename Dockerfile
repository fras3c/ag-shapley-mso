
# Sequoia Docker for Debian Jessie
FROM debian:jessie
MAINTAINER Francesco Lupia <frankylup@gmail.com>

RUN echo "deb [check-valid-until=no] http://cdn-fastly.deb.debian.org/debian jessie main" > /etc/apt/sources.list.d/jessie.list
RUN echo "deb [check-valid-until=no] http://archive.debian.org/debian jessie-backports main" > /etc/apt/sources.list.d/jessie-backports.list
RUN sed -i '/deb http:\/\/deb.debian.org\/debian jessie-updates main/d' /etc/apt/sources.list
RUN apt-get -o Acquire::Check-Valid-Until=false update
# update apt repositories

# install add-apt-repository tool
RUN apt-get -y install software-properties-common
#RUN apt-get install python-software-properties -y
RUN apt-get install -y -t jessie-backports openjdk-8-jdk
# install wget for downloading files
RUN apt-get install -y wget

#add-apt-repository ppa:ubuntu-toolchain-r/test && apt-get update && apt-get install -y \
RUN apt-get install -y build-essential
RUN apt-get install -y vim
RUN apt-get install -y nano
RUN apt-get install -y git
RUN apt-get install -y python3
RUN apt-get install -y make
RUN apt-get install -y python3-dev
RUN apt-get install -y python3-pip
RUN apt-get install -y g++-4.9
  #  libtbb-dev \
  #  clang-format-3.4 \
  #  vim \
RUN apt-get install -y pkg-config
RUN apt-get install -y screen
RUN apt-get install -y cmake

RUN apt-get install -y libboost-all-dev
ADD ./sequoia-core /home/sequoia
ADD ./mso-tool.py /home/
ADD ./fl.mso /home/
ADD ./commons-io-2.5.jar /home/
ADD ./examples /home/examples
ADD ./html /home/html
ADD ./out /home/sequoia/out
ADD ./ShapleyMSO.jar /home/

RUN ls -l /home/sequoia
WORKDIR /home/sequoia
RUN ./configure CPPFLAGS="--std=c++11"
RUN make
