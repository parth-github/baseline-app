# Python App in Docker with Logging

### Run Commands

```bash
docker build -t baseline-pyapp/docker-remote-debugging:v2 .
```

## Run with Volume mounting for live edits

```bash
docker run --name baseline-pyapp-docker-remote-debugging-v2 -v .:/app -p 5678:5678 baseline-pyapp/docker-remote-debugging:v2


## Run Interactively

```bash
docker exec -it baseline-pyapp-docker-remote-debugging-v2 /bin/bash
```

## OR

```bash

docker run --name baseline-pyapp-docker-remote-debugging-v2 -it --rm -v .:/app -p 5678:5678 baseline-pyapp/docker-remote-debugging:v2 /bin/bash

# Without mounting persistent local drive
docker run --name baseline-pyapp-docker-remote-debugging-v2 -it --rm -p 5678:5678 baseline-pyapp/docker-remote-debugging:v2 /bin/bash

pwd
ls -la
cat app.py
python app.py
 
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



```bash
docker run -it -v $(pwd):/app my-python-app /bin/bash
```
