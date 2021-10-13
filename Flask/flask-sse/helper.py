import uuid
import random
from faker import Faker
fake = Faker()

def get_data():
    data = list()
    for _ in range(10):
        data.append({'userId': uuid.uuid4(), 'id': random.randrange(1, 100), 'name': fake.name(), 'address': fake.address()})
    return data


def get_schd_time():
    return random.randrange(5,20)