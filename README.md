# distributed Xiaohongshu Spider and Data Visiualization
A distributed web crawler for [xiaohongshu](https://www.xiaohongshu.com/) and visualization for the crawled content.
![word cloud](https://github.com/KaitoHH/docker-playground/blob/master/wordcloud.png)

## Crawler
As this crawler supports distribution, using a pre-build docker is the recommended and convenient way to build this project.
### Building a stand-alone crawler
1. add `chromedriver` to PATH
2. install all required python packages in `requirements.txt`
3. run `xiaohongshu_consumer.py`

### Building a distributed crawler
This project use `celery` to distribute tasks, so you have to run worker(s) first, and then execute the consumer code to create tasks.

#### Using docker to start worker
`registry.cn-hangzhou.aliyuncs.com/kaitohh/celery:5` is the pre built docker image, and you can also use`docker build -t <my_image_name> .`to build image locally.
##### Step 1 Prerequisites
1. Install [docker](https://www.docker.com/)
2. if you with to run a distributed version of crawler, make sure you have deployed a cluster using docker `swarm` or `kubernetes`.

##### Step 2a run in development environment
run following command
```
docker-compose up
```
and all services will be first built locally and then run automatically. Note that this command will only create one replica for each service.

After all services up, visit `localhost:5555` to enter the celery flower dashboard, and `localhost:8080` to enter the docker visualizer page.

##### Step 2b run in Deployment
run following command
```
docker stack deploy -c docker-compose.yml <your_stack_name>
```

##### Step 3 execute the consumer code
run following command
```shell
set USE_CELERY=1 & python xiaohongshu_consumer.py
```
now visit the celery dashboard and you will see your tasks.

#### Build manually to start worker
You have to first follow instructions for building a stand-alone crawler, then start a redis server and change the environment variable `REDIS_URL` to your redis host.　Finally, run celery worker command to start workers.

See the `Dockerfile` and `docker-compose.yml` as a reference.

## Visualization
see [xiaohongshu_wordcloud.py](https://github.com/KaitoHH/docker-playground/blob/master/xiaohongshu_wordcloud.py) for more detailed implementaion.

## Acknowledgments
- [docker](https://www.docker.com/)
- [celery](http://www.celeryproject.org/)
- [redis](https://redis.io/)
- [selenium](https://www.seleniumhq.org/)
- [jieba](https://github.com/fxsjy/jieba)
- [wordcloud](http://amueller.github.io/word_cloud/)
