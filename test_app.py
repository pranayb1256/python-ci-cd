from app import calculate_total

def test_calculate_total():
    price = 100
    tax_rate = 0.1
    expected_total = 110
    assert calculate_total(price, tax_rate) == expected_total