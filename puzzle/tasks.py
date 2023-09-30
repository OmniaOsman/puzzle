from __future__ import absolute_import, unicode_literals

from celery import shared_task
import hashlib
from project.celery import app
from .models import Puzzle

@shared_task
def solve_puzzle(data, level):
    # try to find a nounce value that makes the SHA-1 hash of the data and the nounce start with a certain number of zeros
    solution = ""
    nounce = 0
    while not solution.startswith("".join(["0" for _ in range(level)])):
        solution = hashlib.sha1(f"{data}{(nounce)}".encode()).hexdigest()
        nounce += 1
        
    # get or create the puzzle model instance with the task id
    # puzzle, created = Puzzle.objects.get_or_create(task_id=solve_puzzle.request.id)

    # # update the puzzle model instance with the data, level, nounce, solution, and status
    # puzzle.data = data
    # puzzle.level = level
    # puzzle.nounce = nounce
    # puzzle.solution = solution
    # puzzle.status = Puzzle.AsyncResult(solve_puzzle.request.id).state
    
    # # save the puzzle model instance to the database
    # puzzle.save()
    
    # # return the nounce and solution as a tuple
    return nounce, solution
