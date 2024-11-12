# Попробуем протестировать кортеж

# Тест-кейс 1,
def test_sum():
    # Утверждение
    assert sum([1, 2, 3]) == 6, "Should be 6"

# Тест-кейс 2,
def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"

# Точка входа теста.
if __name__ == "__main__":
    test_sum()
    test_sum_tuple()
    print("Everything passed")