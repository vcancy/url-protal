FROM python:3.5

COPY . /app
WORKDIR /app
EXPOSE 9999
RUN pip3 install -r requirements.txt  -i https://pypi.douban.com/simple \
    &&cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
CMD ["/usr/local/bin/python", "friendcircle.py runserver 9999"]