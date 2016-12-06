import itertools
import evp
import matrix
import my_matrix_unittest

class TestEigenvalueProblem(my_matrix_unittest.MyMatrixTestCase)
    def setup(self):
        self.mat_h = [[8., 4., 2.],
                      [4., 8., 4.],
                      [2., 4., 8.]]
    def test_power_method(self):
        self.mat_a = [[-2.0, -1.0],
                          [-1.0, -3.0]]
        lambda1, x1 = evp.power_method(self.mat_a)
        vec_a_x1 = matrix.mul_mat_vec(self.mat_a, x1)
        self.assertEqual(len(vec_a_x1), len(self.mat_a))

        for x1i, a_x1i in itertools.izip(x1, vec_a_x1):
            self.assertAlmostEqual(lambda1 * x1i, a_x1i)

    def test_power_method_00(self):
        b_verbose = False
        if b_verbose:
            print ("Power method 00")
        lam, vec_x0 = evp.power_method(self.mat_h)
        if b_verbose:
            print ('%s %s' % (lam, vec_x0))

        vec_x1 = matrix.mul_mat_vec(self.mat_h, vec_x0)
        vec_x0l = [lam * x0k for x0k in vec_x0]

        self.aseertSequenceAlmostEqual(vec_x0l, vec_x1)

    def test_power_method_01(self):
        b_verbose = False
        if b_verbose:
            print ("Power method 01")
        for n in range(3, 10):
            self.mat_a_half = matrix.get_random_mat(n, n)
            self.mat_a_half_transpose = matrix.transpose_mat(self.mat_a_half)

            self.mat_a = matrix.mul_mat(self.mat_a_half_transpose, self.mat_a_half)
            lam, vec_x0 = evp.power_method(self.mat_a, espilon=1e-12)
            if b_verbose:
                print ('%s %s' % (lam, vec_x0))

            vec_x1 = matrix.mul_mat_vec(self.mat_a, vec_x0)
            vec_x0l = [lam * x0k for x0k in vec_x0]

            self.assertEqual(len(vec_x0), n)

            message = '''
x0 =
%s
mat_a x0 =
%s
''' % (vec_x0, vec_x0l)
            self.assertSequenceAlmostEqual(vec_x0l, vec_x1, msg=me)