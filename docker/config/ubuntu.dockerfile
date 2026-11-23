# docker build -t instinct323/jammy:empty -f ubuntu.dockerfile .

# Base image
ARG LSB_RELEASE=22.04
ARG CUDA_VERSION=12.6.3-cudnn-devel

FROM nvidia/cuda:${CUDA_VERSION}-ubuntu${LSB_RELEASE}

LABEL maintainer="tongzanjia@qq.com"

ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /home

# Initialize Ubuntu
RUN apt update && \
    apt install -y --no-install-recommends curl ca-certificates && \
    curl -fsSL https://raw.githubusercontent.com/Instinct323/EnvConfig/master/ubuntu/init-ubuntu.bash -o /tmp/init-ubuntu.bash && \
    bash -e /tmp/init-ubuntu.bash && \
    rm /tmp/init-ubuntu.bash && \
    apt clean

# Timezone
RUN echo 'Asia/Shanghai' > /etc/timezone && \
    apt install -q -y --no-install-recommends tzdata

# OpenSSH
ARG CFG=/etc/ssh/sshd_config
RUN apt update && \
    apt install -y openssh-server && apt clean && \
    mkdir /var/run/sshd && \
    echo "PermitRootLogin yes" >> $CFG

CMD /usr/sbin/sshd -D
