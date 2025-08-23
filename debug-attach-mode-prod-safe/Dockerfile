FROM python:3.12-slim

WORKDIR /app
RUN pip install debugpy dotenv

COPY . .

EXPOSE 5678

# Default: run without debug
CMD ["python", "buggy_calculator_pythonic_debug.py"]

# # Enable debug mode
# ENV DEBUGPY_ENABLED=true
# ENV DEBUGPY_HOST=0.0.0.0
# ENV DEBUGPY_PORT=5678
# ENV DEBUGPY_WAIT=true 

# Build the image
# docker build -t buggy_calculator/prod_safe_pythonic_debug:v1 .

#🔹 Run modes
# Normal mode (no debugger):
# docker run --rm --name buggy_calculator-prod_safe_pythonic_debug-v1 -v .:/app buggy_calculator/prod_safe_pythonic_debug:v1

# Debug mode (attach later, non-blocking):
# docker run --rm --name buggy_calculator-prod_safe_pythonic_debug-v1 -e DEBUGPY_ENABLED=true -v .:/app buggy_calculator/prod_safe_pythonic_debug:v1

# Debug mode (wait until debugger attaches):
# docker run --rm --name buggy_calculator-prod_safe_pythonic_debug-v1 -e DEBUGPY_ENABLED=true -e DEBUGPY_WAIT=true -v .:/app buggy_calculator/prod_safe_pythonic_debug:v1