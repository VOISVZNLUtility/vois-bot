import json
import os
from datetime import datetime, timedelta

RESERVATION_FILE = "data/reservations.json"

def load_reservations():
    if not os.path.exists(RESERVATION_FILE):
        return []
    with open(RESERVATION_FILE, "r") as f:
        return json.load(f)

def save_reservations(data):
    os.makedirs("data", exist_ok=True)
    with open(RESERVATION_FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_reservation(user, test_name, duration_days=3):
    reservations = load_reservations()
    expiry = (datetime.now() + timedelta(days=duration_days)).strftime("%Y-%m-%d")
    reservations.append({
        "user": user,
        "test_name": test_name,
        "reserved_on": datetime.now().strftime("%Y-%m-%d"),
        "expires_on": expiry
    })
    save_reservations(reservations)

def get_active_reservations():
    today = datetime.now().date()
    return [r for r in load_reservations() if datetime.strptime(r["expires_on"], "%Y-%m-%d").date() >= today]