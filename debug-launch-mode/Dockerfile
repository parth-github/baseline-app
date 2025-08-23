FROM python:3.11-slim

WORKDIR /app

# Install debugpy + requirements
RUN pip install debugpy

COPY buggy_calculator.py .

# To run without debugger, use:
# CMD ["python", "buggy_calculator.py"]

