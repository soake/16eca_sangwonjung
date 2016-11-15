import random
import pylab

import gauss_jordan as gj
import matrix

random.seed()


def least_square_first_order(vec_x, vec_y):
    mat_x_t = [vec_x,
               [1] * len(vec_x)]
    mat_x = matrix.transpose_mat(mat_x_t)
    mat_y_measured = matrix.transpose_mat([vec_y])
    mat_w_estimated = mul_left_inverse(mat_x, mat_y_measured)
    return mat_w_estimated

def mul_left_inverse(mat_x, mat_y):
    mat_x_left_inverse = get_left_inverse(mat_x)
    mat_w_estimated = matrix.mul_mat(mat_x_left_inverse, mat_y)

    del mat_x_left_inverse[:]
    del mat_x_left_inverse
    return mat_w_estimated

def get_left_inverse(mat_x):
    mat_x_t = matrix.transpose_mat(mat_x)
    mat_xt_x = matrix.mul_mat(mat_x_t, mat_x)
    mat_xt_x_inv = gj.gauss_jordan(mat_xt_x)
    mat_x_left_inverse = matrix.mul_mat(mat_xt_x_inv, mat_x_t)
    return mat_x_left_inverse

def contaminate(vec_y, standard_deviation = 0.5):
    vec_y_measured = [yi + random.gauss(0.0, standard_deviation) for yi in vec_y]
    return vec_y_measured

def visualize_least_square_first_order(a_hat, b_hat, vec_x, vec_y, vec_y_measured):
    pylab.plot(vec_x, [a_hat * xi + b_hat for xi in vec_x], label='estimated')
    pylab.plot(vec_x, vec_y_measured, '.', label='measured')
    pylab.plot(vec_x, vec_y, 'r', label='truth')
    pylab.grid(True)
    pylab.legend(loc=0)
    pylab.show()