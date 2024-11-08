import time
import uuid
from datetime import datetime


random_string = str(uuid.uuid4())

while True:
    current_time = datetime.now().isoformat()
    print(f"{current_time}: {random_string}")
    time.sleep(5)
