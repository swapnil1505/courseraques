import unittest
from translator import english_to_french,french_to_english

class Testlanguage(unittest.TestCase):
    def test1(self):
         self.assertNotEqual(english_to_french("how are you"),"")
         self.assertEqual(english_to_french("Hello"),"Bonjour")

class Testlanguage1(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(french_to_english("Comment vous êtes"),"")
        self.assertEqual(french_to_english("Bonjour"),"Hello")






unittest.main()
