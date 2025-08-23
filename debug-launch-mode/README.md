# Launch Mode - VS Code

## Local

1. Install the `debugpy` package:

   ```bash
   pip install debugpy
   ```

2. Start your script with the `debugpy` module:

```bash
   python -m debugpy --listen 5678 --wait-for-client my_script.py
   ```
