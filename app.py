from celery import Celery

# app = Celery('tasks', broker='redis://', backend='redis://')
app = Celery('tasks', broker='redis://redis:6379/0', backend='redis://redis:6379/0')

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
