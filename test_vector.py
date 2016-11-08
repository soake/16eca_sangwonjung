import unittest
import vector as v
class TestVector(unittest.TestCase):
    def setUp(self):
        self.x = [1.0, 0.0]
        self.y = [0.0, 1.0]
        self.z = [0.5 ** 0.5 , 0.5 ** 0.5]
        self.w = [0.5, 0.5 * (3 ** 0.5)]

    def tearDown(self):
        del self.x
        del self.y
        del self.z
        del self.w

    def testAdd01(self):
        z = v.add(self.x, self.y)
        expected = (self.x[0] + self.y[0], self.x[1] + self.y[1])
        for k in xrange(2):
            self.assertEqual(z[k], expected[k])
    def testAdd02(self):
        z = v.add(self.x, self.x)
        e = (self.x[0] + self.x[0], self.x[1] + self.x[1])
        for zk, ek in zip(z, e):
            self.assertEqual(zk, ek)
    def testScalaMul01(self):
        z = v.scalar_mul(1.0, self.x)
        e = (self.x[0], self.x[1])
        for zk, ek in zip(z, e):
            self.assertEqual(zk.ek)

    def testScalaMul02(self):
        z = v.scalar_mul(2.0, self.x)
        e = (self.x[0] * 2.0, self.x[1] * 2.0)
        for zk, ek in zip(z, e):
            self.assertEqual(zk.ek)

    def testScalaMul03(self):
        z = v.scalar_mul(-1.0, self.x)
        e = (-self.x[0], -self.x[1])
        for zk, ek in zip(z, e):
            self.assertEqual(zk.ek)

    def testDot01(self):
        z = v.dot(self.x, self.x)
        e = 1.0
        self.assertEqual(z, e)

    def testDot02(self):
        z = v.dot(self.x, self.y)
        e = 0.0
        self.assertEqual(z, e)
    def testDot03(self):
        z = v.dot(self.x, self.z)
        e = 0.5 ** 0.5
        self.assertEqual(z, e)

    def testMag01(self):
        z = (v.mag(self.x), v.mag(self.y), v.mag(self.z))
        e = (1.0,) * 3
        [self.assertEqual(zk, ek) for zk, ek in zip(z, e)]

    def testCross2d01(self):
        z = v.cross2d(self.x, self.y)
        e = (0.0, 0.0, 1.0)
        [self.assertEqual(zk, ek) for zk, ek in zip(z, e)]

    def testRot01(self):
        z = v.rot2d(self.x, 60)
        e = self.w
        [self.assertAlmostEqual(zk, ek) for zk, ek in zip(z, e)]

    def testRot02(self):
        z = v.rot2d(self.x, 45)
        e = self.z
        [self.assertAlmostEqual(zk, ek) for zk, ek in zip(z, e)]


if "__main__" == __name__:
    unittest.main()
