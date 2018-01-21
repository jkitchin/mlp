import unittest
import ase

class TestSanity(unittest.TestCase):
    def test0(self):
        self.assertTrue(True)
        self.assertFalse(False)
        self.assertEquals(1, 1)
        self.assertGreater(1, 0)
        self.assertLess(0, 1)
        self.assertLessEqual(0, 0)
        self.assertLessEqual(0, 1)
        
    def test1(self):
        from mlp.sanity import sanity0
        self.assertTrue(sanity0() == 2)


if __name__ == '__main__':
    unittest.main()
    
