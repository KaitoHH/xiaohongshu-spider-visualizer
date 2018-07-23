import os

from celery import Celery

# app = Celery('tasks', broker='redis://', backend='redis://')
redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
app = Celery('tasks', broker=redis_url, backend=redis_url)

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
