from __future__ import absolute_import, unicode_literals

from celery import shared_task
import hashlib
from project.celery import app
from .models import Puzzle

@app.task(bind=True, ignore_result=False)
def solve_puzzle(data, level=4):
    solution = ""
    nounce = 0
    while not solution.startswith("".join(["0" for _ in range(level)])):
        solution = hashlib.sha1(f"{data}{(nounce)}".encode()).hexdigest()
        nounce += 1
        
    # get or create the puzzle model instance with the task id
    puzzle, created = Puzzle.objects.get_or_create(task_id=solve_puzzle.request.id)

    # update the puzzle model instance with the result and other fields
    puzzle.data = data
    puzzle.nounce = nounce
    puzzle.solution = solution
    puzzle.status = Puzzle.AsyncResult(solve_puzzle.request.id).state
    # save the puzzle model instance to the database
    puzzle.save()
    return nounce, solution