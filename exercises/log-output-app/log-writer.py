import time
import uuid
from datetime import datetime


file_path = "/usr/src/app/files/timestamp.txt"

while True:
    current_time = datetime.now().isoformat()
    with open(file_path, "w") as file:
        file.write(f"{current_time}")
    print(f"Written timestamp: {current_time}", flush=True)
    time.sleep(5)
