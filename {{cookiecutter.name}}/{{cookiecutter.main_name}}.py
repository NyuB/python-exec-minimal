#!{{ cookiecutter.python3 }}
import sys
import unittest

def message() -> str:
    return "{{ cookiecutter.name }}"

def main(args: list[str]):
    print(message(), *args)

if __name__ == '__main__':
    main(sys.argv[1:]) # First argument is the program name

class Test(unittest.TestCase):
    def test_ok(self):
        self.assertEqual(message(), "{{ cookiecutter.name }}")
