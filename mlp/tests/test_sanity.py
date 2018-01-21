"""Sanity tests.

These should just work and verify that the basic Python environment is setup.
Also, they remind me of the unittest structure.
"""
import unittest
import ase

class TestSanity(unittest.TestCase):
    def test0(self):
        self.assertTrue(True)
        self.assertFalse(False)

        self.assertEqual(1, 1)
        self.assertAlmostEqual(0, 1e-6, 5)

        self.assertNotEqual(1, 2)
        self.assertNotAlmostEqual(0, 1e-6, 6)
        
        self.assertGreater(1, 0)
        self.assertGreaterEqual(0, 0)
        self.assertGreaterEqual(1, 0)

        self.assertLess(0, 1)
        self.assertLessEqual(0, 0)
        self.assertLessEqual(0, 1)

        self.assertIn(1, [0, 1])
        self.assertNotIn(2, [0, 1])
        
        self.assertIsNone(None)
        self.assertIsNotNone(True)

        self.assertSequenceEqual([0, 1], [0, 1])
        self.assertListEqual([0, 1], [0, 1])

        self.assertDictEqual({0: 'test', 1: 'tree'},
                             {1: 'tree', 0: 'test'})

        self.assertTupleEqual((1, 2, 3), (1, 2, 3))


        self.assertSetEqual(set([0, 1]), set([1, 1, 0]))

        s = '''a long 
multiline
string'''
        self.assertMultiLineEqual(s, s)
        
        with self.assertRaises(ZeroDivisionError):
            1 / 0

        self.assertCountEqual([0, 1, 1], [1, 0, 1])

        
    def test1(self):
        from mlp.sanity import sanity0
        self.assertTrue(sanity0() == 2)


if __name__ == '__main__':
    unittest.main()
    
