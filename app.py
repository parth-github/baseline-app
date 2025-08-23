import logging
import os
import debugpy

# Ensure 'logs' directory exists
os.makedirs("logs", exist_ok=True)
    
# logging
logging.basicConfig(
    level=logging.DEBUG,
    filename="logs/app.log",           # Log messages to 'app.log'
    filemode="a",                 # Append mode
    format="%(asctime)s %(levelname)s %(message)s"
)

logging.log(logging.INFO, "# Log debug info to a file")
debugpy.log_to("logs/debugpy")
logging.log(logging.INFO, "# Allow debugger to attach")
debugpy.listen(("0.0.0.0", 5678))
print("⏳ Waiting for debugger to attach...")
logging.log(logging.INFO, "# Pause the program until a remote debugger is attached")
logging.log(logging.INFO, "# ⏳ Waiting for debugger to attach...")
debugpy.wait_for_client()
# Now you can set breakpoints in VS Code and step through
print("Debugger is attached! 🚀")
logging.log(logging.INFO, "#🚀 Debugger is attached! ")



def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
        print(f"Adding {num}, total is now {total}")
    return total

def main():
    numbers = [1, 2, 3, 4, 5]
    result = calculate_sum(numbers)
    print(f"Final result: {result}")
    
    # programmatic breakpoint
    debugpy.breakpoint()   
    logging.log(logging.INFO, "# Programmatic breakpoint hit.")
    logging.log(logging.INFO, "# Hit the breakpoint! Inspect variables in VS Code.")
    print("Hit the breakpoint! Inspect variables in VS Code.")

    # This line will cause our program to crash!
    division_result = 10 / 0
    print(f"Division result: {division_result}")

if __name__ == "__main__":
    main()