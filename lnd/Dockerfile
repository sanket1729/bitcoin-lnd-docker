FROM ubuntu:16.04

RUN apt-get update && apt-get install -qy git wget
RUN apt-get install -qy build-essential
RUN wget https://dl.google.com/go/go1.11.5.linux-amd64.tar.gz
RUN tar -C /usr/local -xzf go1.11.5.linux-amd64.tar.gz
ENV PATH="/usr/local/go/bin:${PATH}"
RUN go get -d github.com/lightningnetwork/lnd
WORKDIR /root/go/src/github.com/lightningnetwork/lnd
RUN git checkout abfbdf6aec3bbf63a1f13e5706ee983efbfb4674
RUN sed -i "s/.*defaultTrickleDelay.*=.*/        defaultTrickleDelay=2*1000/" config.go
RUN make && make install

EXPOSE 9735 10009
WORKDIR /root/go/bin
ADD lnd.conf /root/.lnd/lnd.conf
CMD ["./lnd" ,"--bitcoin.mainnet", "--no-macaroons" ,"--noseedbackup"]
