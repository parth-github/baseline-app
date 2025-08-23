FROM python:3.11-slim

WORKDIR /app

COPY app.py .
COPY requirements.txt .

# Install the remote debugging library
RUN pip install -r requirements.txt

# Expose the port that the debugger will use
EXPOSE 5678

# Start the program with debugger support
CMD ["python3", "-m", "-Xfrozen_modules=off", "debugpy", "--listen", "0.0.0.0:5678", "--wait-for-client", "app.py"]