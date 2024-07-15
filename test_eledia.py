import unittest
from eledia import eledia_text

class TestEledia(unittest.TestCase):
    def test_eledia_text(self):
        self.assertEqual(eledia_text(1, r'c:\Users\tadib\eledia\eledia_test'), 'Hallo! Ich bin Adib Tajouri und ich freue mich, bei eleDia als Python-Entwickler zu arbeiten.')
        self.assertEqual(eledia_text(2, r'c:\Users\tadib\eledia\eledia_test'), 'Wie geht es dir?')
        self.assertEqual(eledia_text(3, r'c:\Users\tadib\eledia\eledia_test'), 'gut gemacht!')
        self.assertEqual(eledia_text(4, r'c:\Users\tadib\eledia\eledia_test'), 'super!')

if __name__ == "__main__":
    unittest.main()
