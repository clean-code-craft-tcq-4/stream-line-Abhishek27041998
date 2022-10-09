import random

MIN_LIMIT = 0
MAX_LIMIT = 100


def generate_temperature_samples(num: int):
    temperatures = []

    for _ in range(num):
        val = random.randint(MIN_LIMIT, MAX_LIMIT)

        temperatures.append(val)

    return temperatures


