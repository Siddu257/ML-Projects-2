import logging
import os
from datetime import datetime

# Generate the log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  # Use single quotes here

# Define the path to the logs directory
logs_path = os.path.join(os.getcwd(), "logs")

# Create the logs directory if it doesn't exist
os.makedirs(logs_path, exist_ok=True)

# Define the full path for the log file
LOG_FILE_Path = os.path.join(logs_path, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_Path,  # Use 'filename' in lowercase
    format="[%asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Fixed format string
    level=logging.INFO
)

# Test the logging functionality
if __name__ == "__main__":
    logging.info("Logging has started")

