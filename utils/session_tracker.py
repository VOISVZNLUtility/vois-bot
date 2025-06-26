import os
import csv
from datetime import datetime

def track_session():
    os.makedirs("logs", exist_ok=True)
    log_file = "logs/session_log.csv"
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user = "anonymous"  # You can enhance this with login logic

    write_header = not os.path.exists(log_file)
    with open(log_file, "a", newline="") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(["timestamp", "user"])
        writer.writerow([now, user])