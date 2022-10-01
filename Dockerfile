


FROM nvcr.io/nvidia/pytorch:21.08-py3

WORKDIR /root
RUN apt-get update
RUN apt-get install -y zip
RUN pip install hepai

# CMD [ "hai run-server" ]


