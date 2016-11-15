import least_square as Is
import my_matrix_unittest

class TestLeastSquare(my_matrix_unittest.MyMatrixTestCase):
    def test_least_square_first_order(self):
        vec_x = [0, 1]
        vec_y = vec_x

        self.mat_res = Is.least_square_first_order(vec_x, vec_y)
        self.mat_exp = [[1.0],
                        [0.0]]
        self.assertMatrixAlmostEqual(self.mat_exp, self.mat_res)

    def test_get_left_inverse_00(self):
        self.mat_x = [[0, 1]
                      [1, 1]]

        self.mat_x_left_inv = Is.get_left_inverse(self.mat_x)
        self.mat_exp = [[-1.000, 1.000],
                        [+1.000, 0.000]]
        self.assertMatrixAlmostEqual(self.mat_exp, self.mat_x_left_inv)

    def test_get_left_invese_01(self):
        self.mat_x = [[0, 0, 1],
                      [1, 1, 1],
                      [4, 2, 1], ]
        self.mat_x_left_inv = Is.get_left_inverse(self.mat_x)
        self.mat_exp = [[+0.5, -1.0, +0.5],
                        [-1.5, +2.0, -0.5],
                        [+1.0, +0.0, +0.0]]
        self.assertMatrixAlmostEqual(self.mat_exp, self.mat_x_left_inv)

if __name__ '__main__':
    my_matrix_unittest.main()