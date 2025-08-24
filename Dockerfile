FROM python:3.12-slim

COPY requirements.txt .
# Install debugpy + requirements
RUN pip install -r requirements.txt

COPY app.py .

# To run without debugger, use:
# CMD ["python", "app.py"]
ENTRYPOINT [ "python", "app.py" ]
#
# docker run -t --rm --name python-tester testingpython:v1 python app.py
# To run with sonar
# COPY sonar-project.properties .
# CMD ["sonar-scanner"]
# sonar-scanner -Dsonar.projectKey=python-debugger -Dsonar.sources=. -Dsonar.host.url=http://localhost:9000 -Dsonar.login=your_token

# docker build -t testingpython:v1 .
# docker run -it --rm --name python-tester testingpython:v1 /bin/bash