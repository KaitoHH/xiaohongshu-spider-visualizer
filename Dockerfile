# Use an official Python runtime as a parent image
FROM python:3.6-slim

# update mirror
RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
RUN sed -i 's|security.debian.org/debian-security|mirrors.ustc.edu.cn/debian-security|g' /etc/apt/sources.list

# install chromedriver
RUN apt-get update -y && apt-get install -y chromedriver unzip wget curl
RUN wget -O /tmp/chromedriver.zip http://npm.taobao.org/mirrors/chromedriver/`curl -L http://npm.taobao.org/mirrors/chromedriver/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d -o /usr/bin/

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# Make port 80 available to the world outside this container
EXPOSE 5555

ENV REDIS_URL redis://redis:6379/0
# Run app.py when the container launches
#CMD ["celery", "-A", "tasks", "worker", "--loglevel=error"]
