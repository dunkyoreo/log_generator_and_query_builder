from faker import Faker
import random
import json
import time

fake = Faker()

def generate_airline_log():
    log = {
        "flight_number": fake.random_int(min=100, max=9999),
        "departure": fake.city(),
        "arrival": fake.city(),
        "timestamp": fake.date_time_between(start_date="-1d", end_date="now").isoformat(),
    }
    return json.dumps(log)

# Example usage
for _ in range(10):
    print(generate_airline_log())
    time.sleep(1)
