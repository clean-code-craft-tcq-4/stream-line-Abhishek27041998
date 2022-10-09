from generate_temperature import generate_temperature_samples
from generate_charge_rate import generate_charge_rate_samples


def main():
    # Totally 10 samples, each sample consisting of 60 readings for each parameters
    NUM_OF_READINGS = 50

    # Outputting the Charge rates reading to standard output console
    charge_rates = generate_charge_rate_samples(NUM_OF_READINGS)
    print(" ".join([str(i) for i in charge_rates]))

    # Outputting the Temperature reading to standard output console
    temperatures = generate_temperature_samples(NUM_OF_READINGS)
    print(" ".join([str(i) for i in temperatures]))


if __name__ == '__main__':
    main()
