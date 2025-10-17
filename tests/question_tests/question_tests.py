from src.question_a.question_a import get_miles_per_hour
from src.question_b.question_b import get_sum_of_evens
from src.question_c.question_c import get_random_number
from src.question_d.question_d import get_fahrenheit

def test_get_miles_per_hour():
    # 32 km in 60 minutes → 19.883872 mph
    assert get_miles_per_hour(32, 60) == 19.883872
    # Negative input should return 'Invalid arguments'
    assert get_miles_per_hour(-5, 30) == 'Invalid arguments'
    assert get_miles_per_hour(10, -5) == 'Invalid arguments'
    assert get_miles_per_hour(10, 0) == 'Invalid arguments'


# ---------------------------
# Question B: Sum of Evens
# ---------------------------
def test_get_sum_of_evens():
    assert get_sum_of_evens(11) == 30
    assert get_sum_of_evens(10) == 30
    assert get_sum_of_evens(8) == 20
    # Edge cases
    assert get_sum_of_evens(1) == 0
    assert get_sum_of_evens(0) == 0

def test_get_random_number_range():
    # Run multiple times to confirm number stays in range 1–5
    for _ in range(1000):
        num = get_random_number()
        assert 1 <= num <= 5


def test_get_fahrenheit():
    assert get_fahrenheit(0) == 32
    assert get_fahrenheit(5) == 41
    assert get_fahrenheit(10) == 50
