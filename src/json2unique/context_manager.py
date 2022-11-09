import sys


class RecursionDepth:
    def __init__(self, limit):
        if limit < 500:
            limit = 500
        if limit > 25000:
            limit = 25000
        self.limit = limit

    def __enter__(self):
        self.previous_limit = sys.getrecursionlimit()
        sys.setrecursionlimit(self.limit)

    def __exit__(self, exc_type, exc_value, traceback):
        sys.setrecursionlimit(self.previous_limit)
