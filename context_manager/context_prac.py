class File(object):
    """At the very least a context manager has an __enter__ and __exit__ method defined."""
    def __init__(self, file_name, method):
        self.file_name = file_name
        self.method = method

    def __enter__(self):
        self.file_obj = open(self.file_name, self.method)
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()


"""
Just by defining __enter__ and __exit__ methods we can use our new class in a with statement. 
"""

with File('./demo.txt', 'w') as f:
    f.write('Hello Context!')