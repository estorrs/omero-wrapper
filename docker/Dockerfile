FROM ubuntu:18.04

RUN apt-get update && apt-get install -y vim wget curl git

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py310_23.3.1-0-Linux-x86_64.sh -O ~/miniconda.sh
RUN bash ~/miniconda.sh -b -p /miniconda
ENV PATH="/miniconda/bin:$PATH"

# get env file seperately so it doesn't reinstall every time
COPY ./env.yaml /omero-wrapper/env.yaml
RUN conda env create --file /omero-wrapper/env.yaml 
RUN conda install -n omero-wrapper -c conda-forge openjdk -y

COPY . /omero-wrapper

RUN mkdir -p /omero_home
ENV PATH="/miniconda/envs/omero-wrapper/bin:$PATH"
ENV OMERO_USERDIR="/omero_home"

RUN pip install /omero-wrapper

CMD /bin/bash
