import uuid
import random
from faker import Faker


def generate_sample_data_with_uuid(num_records):
    if num_records > 200:
        raise ValueError("Too many records")
    fake = Faker('en_GB')
    data = []
    for _ in range(num_records):
        record = {
                "id": str(uuid.uuid4()),
                "name": fake.name(),
                "email": fake.email(),
                "city": fake.city(),
                "price": round(random.uniform(10, 100), 2),
                "date": fake.date(),
                "job": fake.job(),
                "phone": fake.phone_number()
        }
        data.append(record)
    return data



def process_in_batches(data, batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]
