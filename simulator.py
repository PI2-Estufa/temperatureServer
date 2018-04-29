import time
import random

temperature = 20

while True:
    print(temperature)
    time.sleep(2)
    temperature = random.randint(20, 30) + random.random()
