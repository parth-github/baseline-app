# Debugging Python App in Docker with Logging

## Launch Mode - VS Code

## Local

1. Install the `debugpy` package:

```bash
   pip install debugpy
   ```

2. Start your script with the `debugpy` module:

```bash
   python -m debugpy --listen 5678 --wait-for-client my_script.py
   ```



1. Basic Debugging (Launch Mode) → you run your script directly with debugging enabled.

2. Debugging Inside Your Code (Attach Mode) → you add debugpy to your Python code so the debugger can connect later (useful for containers, Airflow, Spark jobs, etc.).

```plaintext
- Mode 1 — --wait-for-client
- Development / CI debugging → ✅ Mode 1 (--wait-for-client)
- python -m debugpy --listen 0.0.0.0:5678 --wait-for-client buggy_calculator_cmd_debug.py

- Mode 2 — listen only (non-blocking)
- Staging / Production hot debugging → ✅ Mode 2 (non-blocking)
- python -m debugpy --listen 0.0.0.0:5678 buggy_calculator_cmd_debug.py

- Mode 3 - Pythonic
- python buggy_calculator_pythonic_debug.py
```
