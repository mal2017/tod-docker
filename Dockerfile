# Base image
FROM ubuntu:16.04

# Get python 2.7
RUN apt update
RUN apt-get -y install software-properties-common
RUN apt install -y python2.7 python-pip

# get bamliquidator
RUN apt-get -y install software-properties-common
RUN apt-get -y install git libbam-dev libhdf5-serial-dev libboost-dev libboost-timer-dev libgoogle-perftools-dev libtbb-dev samtools python python-numpy python-pandas python-redis python-pip python-software-properties python-tables python-numexpr
RUN pip install bokeh==0.9.3 "openpyxl>=1.6.1,<2.0.0"
RUN git clone https://github.com/BradnerLab/pipeline.git
RUN make --directory /pipeline/bamliquidator_internal
RUN ln -s /pipeline/bamliquidator_internal/bamliquidatorbatch/bamliquidator_batch.py /usr/local/bin/bamliquidator_batch

# get bowtie2
RUN apt-get install wget unzip
RUN wget https://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.2.1/bowtie2-2.2.1-linux-x86_64.zip
RUN ln -s /bowtie2-2.2.1/bowtie2-* /usr/local/bin/

# get macs1.4
RUN wget https://github.com/downloads/taoliu/MACS/MACS-1.4.2-1.tar.gz
RUN tar -xvf MACS-1.4.2-1.tar.gz && cd MACS-1.4.2 && python setup.py install

# get samtools and dependencies
RUN apt-get install -y libncurses5-dev libncursesw5-dev
RUN wget https://sourceforge.net/projects/samtools/files/samtools/0.1.19/samtools-0.1.19.tar.bz2
RUN tar -xvf samtools-0.1.19.tar.bz2 && make --directory /samtools-0.1.19
RUN ln -s /samtools-0.1.19/samtools /usr/local/bin/

# get fimo --- pick up from here
RUN apt-get install -y libexpat1-dev
RUN bash -c '/bin/echo -e “yes\n” | cpan HTML::PullParser'
RUN cpan HTML::Template && cpan XML::Simple && cpan XML::Parser::Expat

RUN wget http://meme-suite.org/meme-software/4.9.1/meme_4.9.1_2.tar.gz
RUN tar zxf meme_4.9.1_2.tar.gz
RUN cd meme_4.9.1 && ./configure --prefix=/meme --with-url=http://meme-suite.org --enable-build-libxml2 --enable-build-libxslt && make && make test && make install
RUN ln -s /meme/bin/* /usr/local/bin/

# get coltron (+ networkx pkg)
#RUN pip install coltron
#RUN coltron-get-data

RUN wget ftp://ftp.ccb.jhu.edu/pub/data/bowtie2_indexes/hg19.zip

RUN mkdir -p genome/index

RUN unzip hg19.zip -d /genome/index

RUN mkdir /home/work
RUN mkdir /home/template

WORKDIR /home/work/


ADD datatable.txt /home/template/

ADD pipeline_template.py /home/template/