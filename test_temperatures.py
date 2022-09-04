from generate_temperature import generate_temperature_samples


def test_generate_temperature():
    temperatures = generate_temperature_samples(5)

    for val in temperatures:
        assert 1 <= val <= 100
