import unittest
from utils import *

class TestErrorMetrics(unittest.TestCase) :

  def setUp(self) :
      pass

  def test_F2C(self) :
      F = 212.0
      C = F2C(F)
      self.assertEqual(C, 100.)

if __name__ == '__main__' :
    unittest.main()
