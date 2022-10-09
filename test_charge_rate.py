from generate_charge_rate import generate_charge_rate_samples


def test_generate_charge_rate():
    charge_rates = generate_charge_rate_samples(5)

    for val in charge_rates:
        assert 0.65 <= val <= 1.00
