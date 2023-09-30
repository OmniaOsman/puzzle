from celery.backends.database import DatabaseBackend

class PuzzleBackend(DatabaseBackend):
    # specify your custom model class here
    model_class = Puzzle


app = Celery('tasks', 
             backend='myapp.backends.PuzzleBackend', 
             broker='amqp://guest@localhost//')
