

from math import cos, atan, sqrt, exp


def fwd_euler(f, x_init, t_strat, t_end, delta_t):

















    m_time_step = int((t_end - t_strat) * 1.0 / delta_t)


    n_states = len(x_init)



    list_k = tuple(range(m_time_step))


    list_t = tuple(([t_strat + delta_t * i for i in list_k]))









    list_x = [tuple(x_init)]






    for k in list_t[1:]:
        list_x.append([0.0] * n_states)










    xk = x_init


    for k in list_k[:-1]:

        sk = f(xk, list_t[k])


        xk1 = list_x[k + 1]


        for i in xrange(n_states):

            xk1[i] = xk[i] + sk[i] * delta_t



        xk = xk1



    return list_t, list_x





def mod_euler(f, x_init, t_start, t_end, delta_t):





























    x_list = [tuple(x_init)]
    t_list = [t_start]


    tk = t_start

    tk1 = tk + delta_t


    t_end += ((-0.5) * delta_t)


    while tk1 < t_end:

        xk = x_list[-1]


        sk = f(xk, tk)


        xk1_p = [(x + sk[i] * delta_t) for i, x in enumerate(xk)]


        sk1_p = f(xk1_p, tk1)



        sk_c = [(0.5 * (s + sk1_p[i])) for (i, s) in enumerate(sk)]


        xk1_c = [(x + sk_c[i] * delta_t) for i, x in enumerate(xk)]


        x_list.append(xk1_c)


        t_list.append(tk1)


        tk=tk1
        tk1 += delta_t

    return t_list, x_list

def runge_while(f, x_init, t_init, t_end, delta_t):


























    x_list = [x_init]
    t_list = [t_init]


    delta_t_half = 0.5 * delta_t

    delta_t_sixth = delta_t / 6.0


    tk = t_init

    tk_half = tk + delta_t_half

    tk1 = tk + delta_t


    t_end += ((-0.5) * delta_t)


    while tk1 < t_end:

        xk = x_list[-1]


        k1 = f(xk, tk)


        xk1_p = [(xk[i] + k * delta_t_half) for (i, k) in enumerate(k1)]
        k2 = f(xk1_p, tk_half)


        xk2_p = [(xk[i] + k * delta_t_half) for (i, k)in enumerate(k2)]
        k3 = f(xk2_p, tk_half)


        xk3_p = [(xk[i] + k * delta_t) for (i, k) in enumerate(k3)]
        k4 = f(xk3_p, tk1)


        xk1_c = [x + delta_t_sixth * (k1[i] + 2 * (k2[i] + k3[i]) + k4[i]) for (i, x) in enumerate(xk)]


        x_list.append(xk1_c)


        t_list.append(tk1)


        tk = tk1
        tk_half += delta_t
        tk1 += delta_t

    return t_list, x_list



tau = 0.5
m_kg = 10.0
c_newton_per_meter_per_sec = 100.0
k_newton_per_meter = 1000.0


def func(xk, tk):










    u = 1

    y1, y2 = xk[0], xk[1]


    y1dot = y2
    y2dot = (u -(k_newton_per_meter * y1 + c_newton_per_meter_per_sec * y2)) / m_kg

    return (y1dot, y2dot)


def exact(t):






    u = 1

    wn = sqrt(k_newton_per_meter / m_kg)

    zeta = c_newton_per_meter_per_sec / (2.0 * m_kg * wn)

    s = sqrt(1.0 - zeta * zeta)
    s1 = 1.0 / s


    wd = wn + s

    phi = atan(zeta * s)


    y1 = (u / k_newton_per_meter) * (1.0 - s1 * exp(-zeta * wn * t) * cos(wd * t - phi))

    return (y1)


def main():
    help(fwd_euler)

    ti = 0.0
    te = 2.0
    delta_T = 0.01
    x0 = (0.0, 0.0)
    vT, vX = fwd_euler(func, x0, ti, te, delta_T)
    t_list_mod_euler, x_list_mod_euler = mod_euler(func, x0, ti, te, delta_T)
    t_list_runge, x_list_runge = runge_while(func, x0, ti, te, delta_T)

    delta_T = 0.001
    vT01, vX01 = fwd_euler(func, x0, ti, te, delta_T)
    vXexact = tuple([exact(tk) for tk in vT])




    import pylab

    pylab.plot(vT, vX, 'b', label='fwd Euler(0.01)')
    pylab.plot(vT01, vX01, 'g', label='fwd Euler(0.001)')
    pylab.plot(t_list_mod_euler, x_list_mod_euler, '*', label='Modified Euler(0.01)')
    pylab.plot(t_list_runge, x_list_runge, 'x-', label='Runge(0.01)')
    pylab.plot(vT, vXexact, 'ko-', label='exact')
    pylab.legend(loc=0)
    pylab.grid(True)
    pylab.ylabel('x')
    pylab.xlabel('t')
    pylab.show()

    vP, vV = zip(*vX)
    vP01, vV01 = zip(*vX)
    p_list_mod_euler, v_list_mod_euler = zip(*x_list_mod_euler)
    p_list_runge, v_list_runge = zip(*x_list_runge)

    pylab.plot(vP, vV, label='fwd Euler (0.01)')
    pylab.plot(vP01, vV01, label='fwd Euler(0.001)')
    pylab.plot(p_list_mod_euler, v_list_mod_euler, label='Modified Euler(0.01)')
    pylab.plot(p_list_runge, v_list_runge, label='Runge(0.01)')
    pylab.legend(loc=0)
    pylab.grid(True)
    pylab.ylabel('xdot')
    pylab.xlabel('x')
    pylab.show()

if "__main__" == __name__:
    main()