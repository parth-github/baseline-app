# Python Debugger in Docker

Run Commands

```bash
docker build -t my-python-app .
docker run my-python-app
```

## Run Interactively

```bash
docker run -it my-python-app /bin/bash
# See what directory you're in
pwd

# List files in the current directory
ls -la

# Look at your Python file
cat app.py

# Run your Python program
python3 app.py
 
# You'll also see the error:

root@fd1d0355b9e2:/app# python3 app.py
Adding 1, total is now 1
Adding 2, total is now 3
Adding 3, total is now 6
Adding 4, total is now 10
Adding 5, total is now 15
Final result: 15
Traceback (most recent call last):
  File "/app/app.py", line 18, in 
    main()
  File "/app/app.py", line 14, in main
    division_result = 10 / 0
                      ~~~^~~
ZeroDivisionError: division by zero
```

## Volume mounting for live edits

```bash
docker run -it -v $(pwd):/app my-python-app /bin/bash
```

## Connecting a Remote Debugger from Your IDE

```python
# In your Python code, add the following lines to enable remote debugging
import debugpy
debugpy.listen(("0.0.0.0", 5678))
debugpy.wait_for_client()
```

### Run with DockerfileRemoteDebugger

```bash
docker build -t debug/python-function:v1  -f DockerfileRemoteDebugger .

docker run --name debug-python-function-v1 -it -v .:/app -p 5678:5678 debug/python-function:v1 /bin/bash
```

#### OR

```bash
docker run --name debug-python-function-v1 -v .:/app -p 5678:5678 debug/python-function:v1

docker exec -it debug-python-function-v1 /bin/bash
```

Now in VS Code, you can set up a debug configuration (in .vscode/launch.json) to connect to the container:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Attach using Debugpy",
            "type": "debugpy",
            "request": "attach",
            "connect": {
                "host": "localhost",
                "port": 5678
            }
        }
    ]
}
```

## Key Debugging Features You’ll Use

- Breakpoints → stop at a specific line.

- Step In / Step Out / Step Over → navigate code execution.

- Watch Variables → track variable changes live.

- Call Stack → see which function calls led here.

- Conditional Breakpoints → stop only if condition is true:

```python
debugpy.breakpoint()   # programmatic breakpoint
```

## Common Debugging Problems and Solutions

### ⚠️ "My program works on my computer but not in Docker"

This usually means there's a difference in the environment. Check:

Python version differences.
Missing dependencies.
Different file paths.
Environment variables.
File permissions.

### ⚠️ "I can't see my print statements"

Use python -u to avoid output buffering.
Make sure you're running with -it if you want interactive output.
Check if your program is actually running as intended (maybe it's exiting early).

### ⚠️ "My changes aren't showing up"

Make sure you're using volume mounting (-v).
Check that you're editing the right file.
Verify the file is copied into the container.

### ⚠️ "The container exits immediately"

Run with /bin/bash to inspect the container's state.
Check the error messages with docker logs container_name.
Make sure your CMD in the Dockerfile is correct.