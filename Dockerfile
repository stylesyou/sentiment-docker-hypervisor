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

# Install nltk packages 
RUN python -m nltk.downloader popular

# install scipy
RUN pip install scipy

# install scikit-learn
RUN pip install scikit-learn

# install matplotlib
RUN pip install matplotlib

# install tweepy
RUN pip install tweepy

#copy application files
COPY files $HOME/srv/files

#working dir to run pyhton
WORKDIR /srv/files

# add contents to folder
CMD [ "python", "Better_training_data.py" ]
#CMD [ "python", "chinking.py" ]
#CMD [ "python", "chunking.py" ]
#CMD [ "python", "combining_algos_with_vote.py" ]

# END
