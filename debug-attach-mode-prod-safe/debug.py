import os
import dotenv

dotenv.load_dotenv()

# Debug mode (attach later, non-blocking, listen-only):
if os.getenv("DEBUGPY_ENABLED", "false").lower() == "true":
    import debugpy

    debugpy.log_to("debugpy.log")
    host = os.getenv("DEBUGPY_HOST", "0.0.0.0")
    port = int(os.getenv("DEBUGPY_PORT", "5678"))

    print(f"🚀 Debugpy enabled, listening on {host}:{port}")
    debugpy.listen((host, port))

    # Debug mode (wait until debugger attaches)
    if os.getenv("DEBUGPY_WAIT", "false").lower() == "true":
        print("⏳ Waiting for debugger to attach...")
        debugpy.wait_for_client()
        print("Debugger is attached! 🚀")