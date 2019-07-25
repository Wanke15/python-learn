### 1. context_prac.py
- The with statement stores the \__exit__ method of the File class.
- It calls the \__enter__ method of the File class.
- The \__enter__ method opens the file and returns it.
- The opened file handle is passed to opened_file.
- We write to the file using .write().
- The with statement calls the stored \__exit__ method.
- The \__exit__ method closes the file.

### 2. cm_as_generator.py
- Python encounters the yield keyword. Due to this it creates a generator instead of a normal function.
- Due to the decoration, contextmanager is called with the function name (open_file) as it’s argument.
- The contextmanager decorator returns the generator wrapped by the GeneratorContextManager object.
- The GeneratorContextManager is assigned to the open_file function. Therefore, when we later call the open_file function, we are actually calling the GeneratorContextManager object.
