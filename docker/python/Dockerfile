# base image
FROM python:3.7-stretch

# エラーなどを標準出力ではなくバッファする
ENV PYTHONBFFERED 1
RUN mkdir /code

# ワーキングディレクトリを変更
WORKDIR /code

# pipでライブラリをインストール
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
