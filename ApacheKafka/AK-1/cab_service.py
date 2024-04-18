import random
from faker.providers import BaseProvider

class CabProvider(BaseProvider):
    def cab_name(self):
        validCabNames= ["Comfort",
                          'WAV',
                          'Black',
                          'XL',
                          'Intercity',
                          'Bikes',
                          'Upfront XL'
                        ]
        return validCabNames[random.randint(0, len(validCabNames)-1)]