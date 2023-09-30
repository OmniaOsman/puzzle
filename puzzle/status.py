from celery.result import AsyncResult
from celery import Celery

app = Celery('tasks', backend='redis://', broker='amqp://guest@localhost//')


res = AsyncResult("bcdd9344-c5eb-446e-b0ae-c8e36fecc2f9")
print(res.state)
