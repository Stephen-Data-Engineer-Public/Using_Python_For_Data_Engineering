import uuid
import random

def generate_sample_data_with_uuid(num_records):
    if num_records > 1000:
        raise ValueError("Too many records")
    data = []
    for _ in range(num_records):
        record = {
            'id': str(uuid.uuid4()),
            'value': random.random() * 100
        }
        data.append(record)
    return data

def process_in_batches(data, batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]
