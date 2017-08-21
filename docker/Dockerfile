FROM python:3.5

COPY . /app
WORKDIR /app
EXPOSE 8080
RUN pip3 install -r requirements.txt  -i https://pypi.douban.com/simple \
    &&cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
CMD ["/usr/local/bin/python", "manage.py","runserver 8080"]