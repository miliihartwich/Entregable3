import unittest
from parser import parser


class TestDSL(unittest.TestCase):
    def test_select(self):
        result = parser.parse("TRAEME TODO DE LA TABLA users DONDE age EN ESTO (18)")
        self.assertEqual(result, "SELECT * FROM users WHERE age IN (18)")
    
    def test_invalid_syntax(self):
        with self.assertRaises(SyntaxError):
            parser.parse("TRAEME DE LA TABLA users")

if __name__ == '__main__':
    unittest.main()
