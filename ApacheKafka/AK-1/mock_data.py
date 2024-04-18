from faker import Faker
from cab_service import CabProvider

fake = Faker()

fake.add_provider(CabProvider)
for i in range(0, 7):
    print(fake.cab_name())