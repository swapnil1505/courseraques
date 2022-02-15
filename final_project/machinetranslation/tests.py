import unittest
from translator import englishToFrench,frenchToEnglish

class Testlanguage(unittest.TestCase):
    def test1(self):
         self.assertEqual(englishToFrench("how are you"),"Comment vous êtes")
         self.assertEqual(englishToFrench("well i am here"),"Eh bien je suis là")

class Testlanguage1(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish("Comment vous êtes"),"How You Are")
        self.assertEqual(frenchToEnglish("Eh bien je suis là"),"Well I'm here")






unittest.main()
