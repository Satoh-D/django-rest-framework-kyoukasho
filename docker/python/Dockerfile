# base image
FROM python:3.7-stretch

# エラーなどを標準出力ではなくバッファする
ENV PYTHONBFFERED 1
RUN mkdir /code

# nodejsのインストール
RUN apt-get update
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install -y nodejs

RUN npm install -g @vue/cli

# ワーキングディレクトリを変更
WORKDIR /code

# pipでライブラリをインストール
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
