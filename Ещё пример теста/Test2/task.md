Вот короткий скрипт для тестирования трех методов строк:
~~~
import unittest

class TestStringMethods(unittest.TestCase):

  def setUp()
  
  def test_upper(self):
      self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_split(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # Проверим, что s.split не работает, если разделитель - не строка
      with self.assertRaises(TypeError):
          s.split(2)

  def tearDown()
  
if __name__ == '__main__':
    unittest.main()
~~~ 

Тестовый случай создаётся путём наследования от unittest.TestCase.  
3 отдельных теста определяются с помощью методов, имя которых начинается на test.   
Это соглашение говорит исполнителю тестов о том, какие методы являются тестами.

Методы setUp() и tearDown() (которые в данном простом случае не нужны)  
позволяют определять инструкции, выполняемые перед и после каждого теста, соответственно.

Последние 2 строки показывают простой способ запуска тестов.  
unittest.main() предоставляет интерфейс командной строки для тестирования программы.   
Будучи запущенным из командной строки, этот скрипт выводит отчёт, подобный этому:
~~~
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
~~~