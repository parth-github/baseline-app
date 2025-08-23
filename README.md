# Python App in Docker with Logging

Run Commands

```bash
docker build -t pyapp-integration/logging:v2 .
```

## Run Interactively

```bash
docker run --name pyapp-integration-logging-v2 -it -v .:/app -p 5678:5678 pyapp-integration/logging:v2 /bin/bash

pwd
ls -la
cat app.py
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
