FROM python:3.11-slim

WORKDIR /app

# Install debugpy + requirements
RUN pip install debugpy

# # Mode 1 — --wait-for-client
# # Development / CI debugging → ✅ Mode 1 (--wait-for-client)
# # python -m debugpy --listen 0.0.0.0:5678 --wait-for-client buggy_calculator_cmd_debug.py
# COPY buggy_calculator_cmd_debug.py .
# CMD ["python", "-m", "debugpy", "--listen", "0.0.0.0:5678", "--wait-for-client", "buggy_calculator_cmd_debug.py"]
# ## Run
# ## docker build -t buggy_calculator/docker-debugging-attach-mode:v1 .
# ## docker run --name buggy_calculator-docker-debugging-attach-mode-v1 -p 5678:5678 --rm -v .:/app buggy_calculator/docker-debugging-attach-mode:v1

#####------------------------------------------------------------------------------------------
# Mode 2 — listen only (non-blocking)
# Staging / Production hot debugging → ✅ Mode 2 (non-blocking)
# # python -m debugpy --listen 0.0.0.0:5678 buggy_calculator_cmd_debug.py
# COPY buggy_calculator_cmd_debug.py .
# CMD ["python", "-m", "debugpy", "--listen", "0.0.0.0:5678", "buggy_calculator_cmd_debug.py"]
# ## Run
# ## docker build -t buggy_calculator/docker-debugging-attach-mode:v2 .
# ## docker run --name buggy_calculator-docker-debugging-attach-mode-v2 -p 5678:5678 --rm -v .:/app buggy_calculator/docker-debugging-attach-mode:v2

####################################################################################
# Mode 3 - Pythonic
# # python buggy_calculator_pythonic_debug.py
COPY buggy_calculator_pythonic_debug.py .
CMD ["python", "buggy_calculator_pythonic_debug.py"]
## Run
## docker build -t buggy_calculator/docker-debugging-attach-mode:v3 .
## docker run --name buggy_calculator-docker-debugging-attach-mode-v3 -p 5678:5678 --rm -v .:/app buggy_calculator/docker-debugging-attach-mode:v3