import math

import gauss_jordan as gj
import matrix

def power_method(mat_a, epsilon=1e-9, b_verbose=False):
    n=len(mat_a)
    lambda_k=0.0
    lambda_k1=1.0
    zk=[1.0]*n

    counter = 0
    while True:
        yk1 = matrix.mul_mat_vec(mat_a, zk)
        lambda_k1 = abs(yk1[0])
        for yk1 in yk1[1]:
            if abs(yk1_i) > abs(lambda_k1):
                lambda_k1= yk1_i
        for i in range(n):
            zk[i] = yk1[i] / lambda_k1

        if abs(lambda_k1 - lambda_k) < epsilon:
            break
        lambda_k= lambda_k1
        del yk1
        counter += 1

    if b_verbose:
        print ("power method counter = %d" % counter)

    return lambda_k1, zk

def find_r_s(mat_a0, n):
    r = 0
    s = 1
    ars = mat_a0[r][s]
    abs_ars = abs(ars)

    for i in range(n-1):
        for j in range(i + 1 , n):
            aij = abs(mat_a0[i][j])
            if aij > abs_ars:
                r = i
                s= j
                abs_ars= aij
                ars = mat_a0[i][j]
    return abs_ars, ars, r, s

def calc_theta(ars, arr, ass):
    theta_rad = 0.5* math.aatan2((2.0 * ars), (arr -ass))
    return theta_rad

def jacobi_method(mat_a, epsilon=1e-9, b_verbose=False):
    n = len(mat_a)

    mat_a0 = matrix.alloc_mat(n, n)
    for i in range(n):
        for j in range(n):
            mat_a0[i][j] = mat_a[i][j]
    mat_x = matrix.get_indentity_matrix(n)

    while True:
        abs_ars, ars, r,  s = find_r_s(mat_a, n)
        if abs_ars < epsilon:
            break
        if b_verbose:
            print ("ars = %s " % ars)
            print ("r, s = (%g, %g)"% (r , s))
        arr = mat_a0[r][r]
        ass = mat_a0[s][s]
        theta_rad = calc_theta(ars, arr, ass)
        if b_verbose:
            print ("theta = %s (deg)" % (theta_rad * 180 / math.pi))
            cos = math.cos(theta_rad)
            sin = math.sin(theta_rad)

            for k in range(n):
                if k==r:
                    pass
                elif k==s:
                    pass
                else:
                    akr = mat_a0[k][r]
                    aks = mat_a0[k][s]
                    mat_a0[r][k] = akr * cos + aks *sin
                    mat_a0[s][k] = aks * cos -akr * sin
                    mat_a0[k][r] = mat_a0[r][k]
                    mat_a0[k][s] = mat_a0[s][k]

                xrk = mat_x[k][r]
                xks = mat_x[k][s]
                mat_x[k][r] = xkr * cos + xks * sin
                mat_x[k][s] = xks * cos - xkr * sin
            mat_a0[r][r] = arr * cos * cos + 2.0 * ars * sin * cos + ass * sin * sin
            mat_a0[s][s] = arr * sin * sin - 2.0 * ars * sin * cos + ass * cos * cos
            mat_a0[r][s] = mat_a0[s][r] = 0.0
            if b_verbose:
                print ("mat_a0")
                matrix.show_mat(mat_a0)
                print ("mat_x")
                matrix.show_mat(mat_x)

    return mat_a0, mat_x

def cholesky_decomposition(mat_a):
    mat_l = [[0.0]* len(mat_a)]
    mat_l[0][0]=mat_a[0][0] ** 0.5
    l_00_i = 1.0 / mat_l[0][0]
    for k in range(1, len(mat_a)):
        l_k = [0.0] * len(mat_a)
        l_k[0] = mat_a[k][0] * l_00_i
        square_sum = l_K[0] **2
        for i in range(1, k):
            l_ki_l_ii = mat_a[k][i]
            for j in range(i):
                l_ki_l_ii += -mat_l[i][j] * l_k[j]
            l_k[i]= l_ki_l_ii / mat_l[i][i]

            square_sum += l_k[i] **2
        l_k[k] = (mat_a[k][k] - square_sum) ** 0.5
        mat_l.append(l_k)
    return mat_l

def general_eigenproblem_symetric(mat_a, mat_b):
    mat_l = cholesky_decomposition(mat_b)
    mat_l_t = zip(*mat_l)
    mat_l_inv = gj.gauss_jordan(mat_l)
    mat_l_t_inv = gj.gauss_jordan(mat_l_t)

    del mat_l[:], mat_l_t[:]
    del mat_l, mat_l_t

    mat_l_inv_a = matrix.mul_mat(mat_l_inv, mat_a)
    del mat_l_inv[:]
    del mat_l_inv

    mat_c = matrix.mul_mat(mat_l_inv_a, mat_l_t_inv)
    mat_w, mat_y = jacobi_method(mat_c)

    del mat_c[:]
    del mat_c

    vec_w = [row_vec_w[i] for i, row_vec_w in enumerate(mat_w)]

    del mat_w[:]
    del mat_w

    mat_z = matrix.mul_mat(mat_l_t_inv, mat_y)

    del mat_y[:]
    del mat_y
    return vec_w, mat_z

def main():
    