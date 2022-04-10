import complex_Numbers as cmplx
import unittest
#Generate First Complex number in rectengular form
a1 = cmplx.cmplxNumber(1,2)
#Generate Second Complex number in rectengular form
a2 = cmplx.cmplxNumber(3,6)
#Add Two Complex number in rectengular form
""" c = cmplx.add(a1,a2)
d = cmplx.divide(a1,a2)
e = cmplx.multiply(a1,a2)
f = cmplx.substract(a1,a2) """
class testCmplx(unittest.TestCase):
    def test_Add(self):
        self.assertEqual(cmplx.add(a1,a2).real,4)
        self.assertEqual(cmplx.add(a1,a2).imag,8)
    def test_Substract(self):
        self.assertEqual(cmplx.substract(a1,a2).real,-2)
        self.assertEqual(cmplx.substract(a1,a2).imag,-4)
    def test_Multiply(self):
        self.assertEqual(cmplx.multiply(a1,a2).real,-9)
        self.assertEqual(cmplx.multiply(a1,a2).imag,12)
    def test_Divide(self):
        self.assertEqual(cmplx.divide(a1,a2).real,0.3333)
        self.assertEqual(cmplx.divide(a1,a2).imag,0)
        self.assertRaises(ValueError,cmplx.divide,cmplx.cmplxNumber(1,2),cmplx.cmplxNumber(0,0))

if __name__ == '__main__':
    unittest.main()