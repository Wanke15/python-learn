from contextlib import contextmanager

@contextmanager
def open_file(name, method):
    f = open(name, method)
    yield f
    f.close()

with open('demo.txt', 'w') as f:
    f.write('Hello Context!')