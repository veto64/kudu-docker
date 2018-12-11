FROM debian:latest

RUN useradd -M kudu

# Install dependencies
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive && \ 
apt-get -y install apt-utils \
aptitude \ 
autoconf \ 
automake \ 
curl \ 
dstat \
emacs24-nox \
flex \ 
g++ \ 
gcc \ 
gdb \ 
git \ 
krb5-admin-server \ 
krb5-kdc \ 
krb5-user \ 
libkrb5-dev \  
libsasl2-dev \ 
libsasl2-modules \ 
libsasl2-modules-gssapi-mit \ 
libssl-dev \ 
libtool \ 
lsb-release \ 
make \ 
ntp \ 
net-tools \
openjdk-8-jdk \ 
openssl \ 
patch \ 
python-dev \
python-pip \
python3-dev \
python3 \
python3-pip \
pkg-config \ 
python \ 
rsync \ 
unzip \ 
vim-common \
wget \ 
ack-grep 


#Install Kudu
WORKDIR /
RUN git clone https://github.com/apache/kudu  \
&& cd /kudu \ 
&& thirdparty/build-if-necessary.sh \ 
&& mkdir -p build/release \
&& cd /kudu/build/release \
&& ../../thirdparty/installed/common/bin/cmake -DCMAKE_BUILD_TYPE=release -DCMAKE_INSTALL_PREFIX:PATH=/usr ../.. \
&& make -j4 \
&& cd /kudu/build/release \ 
&& make install \
&& mv /kudu/build/release/bin/kudu* /usr/bin/ \
&& mv /kudu/build/release/lib/* /usr/lib/  \
&& mkdir -p /usr/lib/kudu/www \
&& mv /kudu/www/* /usr/lib/kudu/www/ \
&& rm /kudu -Rf


#Setup Python Client
RUN pip3 install setuptools --upgrade  \
&& pip3 install cython \ 
&& pip3 install kudu-python


#Setup Kudu
RUN mkdir -m 700 -p /data && chown kudu:kudu /data
USER root
VOLUME /data

COPY startup.sh /
ENTRYPOINT ["/startup.sh"]
EXPOSE 7050 7051 8050 8051
