FROM ubuntu:22.04 as base

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install \
    -y build-essential cmake git libgmp3-dev libprocps-dev libboost-all-dev libssl-dev libsodium-dev nano wget clang lld libomp-dev curl \
    bash python3-pip

RUN pip3 install crypten
RUN pip3 install onnx2torch
COPY ./ .
RUN pip3 install -r requirements.txt
RUN pip3 install -r requirements.examples.txt
RUN python3 test.py