import  unittest

from my_sum import sum

# self — это ссылка на текущий экземпляр класса.
# Это способ обращения к атрибутам и методам класса изнутри самого класса.

# Суть каждого теста - вызов assertEqual() для проверки ожидаемого результата;
# assertTrue() или assertFalse() для проверки условия;
# assertRaises() для проверки, что метод порождает исключение. Э
# ти методы используются вместо обычного assert для того,
# чтобы исполнитель тестов смог взять все результаты и оформить отчёт.
class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Проверка, может ли функция суммировать список целых чисел.
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()