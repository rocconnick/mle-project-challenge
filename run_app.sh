#! /bin/sh

docker build -t loanapp -f app/container/Dockerfile .

docker run -i -p 5000:5000 loanapp