import random

MIN_LIMIT = 0.65
MAX_LIMIT = 1.00


def generate_charge_rate_samples(num: int):
    charge_rates = []

    for _ in range(num):
        val = random.uniform(MIN_LIMIT, MAX_LIMIT)

        charge_rates.append(val)

    return charge_rates


