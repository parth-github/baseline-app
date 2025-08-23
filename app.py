import logging
import os

# Ensure 'logs' directory exists
os.makedirs("logs", exist_ok=True)
    
# logging
logging.basicConfig(
    level=logging.DEBUG,
    filename="logs/app.log",           # Log messages to 'app.log'
    filemode="a",                 # Append mode
    format="%(asctime)s %(levelname)s %(message)s"
)

logging.log(logging.INFO, "#🚀 Start Calculation! ")



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
    
    logging.log(logging.INFO, "# This line will cause our program to crash if dividing by 0!")

    # This line will cause our program to crash!
    division_result = 10 / 0
    #division_result = 10/5

if __name__ == "__main__":
    main()