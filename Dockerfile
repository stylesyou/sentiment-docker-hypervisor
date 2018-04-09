FROM ubuntu:16.04

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    wget \
    curl \
    python3.5

# move pyhton from 2.7 to 3.5
RUN rm -f /usr/bin/python && ln -s /usr/bin/python3.5 /usr/bin/python

# Install pyhton-pip
ADD https://bootstrap.pypa.io/get-pip.py /root/get-pip.py
RUN python /root/get-pip.py

# update pip
RUN pip install pip --upgrade
RUN pip install wheel

# install numpy
RUN pip install numpy

# install NLTK
RUN pip install nltk

# install scipy
RUN pip install scipy

# install scikit-learn
RUN pip install scikit-learn

# install matplotlib
RUN pip install matplotlib

# install tweepy
RUN pip install tweepy

#copy application files

#EXPOSE 80
#WORKDIR /src
# add contents to folder
#ADD src $HOME/src
#CMD ["/usr/bin/supervisord", "-c", "/supervisor/supervisord.conf"]
