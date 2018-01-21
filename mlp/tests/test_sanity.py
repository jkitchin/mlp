import unittest
import ase

class TestSanity(unittest.TestCase):
    def test0(self):
        self.assertTrue(True)

    def test1(self):
        from mlp.sanity import sanity0
        self.assertTrue(sanity0() == 2)


if __name__ == '__main__':
    unittest.main()
    
