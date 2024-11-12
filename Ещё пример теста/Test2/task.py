import unittest

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        a = "string0"

    # строка 'foo', переведённая в верхний регистр будет равна 'FOO'
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    # строка 'FOO', в верхнем регистре, правда?
    # строка 'Foo', в верхнем регистре, ведь это не верно?
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        # разбитая на подстроки, строка 'hello world', равна списку ['hello', 'world']
        self.assertEqual(s.split(), ['hello', 'world'])
        # Проверим, что s.split не работает, если разделитель - не строка
        with self.assertRaises(TypeError):
            s.split(2)

    def tearDown(self):
        a = "string0"

if __name__ == '__main__':
    unittest.main()
