# -*- coding: utf8 -*-
#2015110038 정상원

from math import exp

def rect0(f, xi, xe, n=100):
    delta_x = (float(xe) - float(xi)) / n
    x = [xi + delta_x * (0.5 + k) for k in xrange(n)]
    result = 0.0
    for k in xrange(n):
        xk = x[k]
        area_k = f(xk) * delta_x
        result += area_k
    return result

def trapezoid1(f, xi, xe, n=100):
    delta_x = (float(xe) - float(xi)) / n
    xk=xi
    fxk = f(xk)
    result = 0.0
    for k in xrange(n):
        xk1 = xk + delta_x
        fxk1 = f(xk1)
        area_k = (fxk + fxk1) * delta_x * 0.5
        result += area_k
        xk = xk1
        fxk = fxk1
    return result
def simpson2(f, xi, xe, n=100, b_verbose=False):
    if b_verbose:
        print "n =", n
        print "n%2 =", n % 2
    if (n % 2):
         n +=1
    delta_x = (float(xe) - float(xi)) / n
    xk = xi
    fxk = f(xk)
    result = 0.0
    for k in xrange(0, n, 2):
        xk1 = xk + delta_x
        fxk1 = f(xk1)
        xk2= xk1 + delta_x
        fxk2 = f(xk2)
        area_k = (fxk + 4 * fxk1 + fxk2) * (delta_x / 3.0)
        result += area_k
        xk = xk2
        fxk = fxk2
    return  result
def f(x):
    return exp(x)
def g(x):
    return exp(x)

def main():
    help(rect0)
    x_begin = 0.0
    x_end = 1.0
    n_interval = 8

    exact = (g(x_end) - g(x_begin))
    print "exact soultion =", exact

    intergration_0 = rect0(f, x_begin, x_end, n_interval)
    print "intergration_0 =", intergration_0, "err =", intergration_0 - exact

    intergration_1 = trapezoid1(f, x_begin, x_end, n_interval)
    print "intergration_1 =", intergration_1, "err =", intergration_1 - exact

    intergration_2 = simpson2(f, x_begin, x_end, n_interval)
    print "intergration_2 =", intergration_2, "err =", intergration_2 - exact

    from  pylab import fill, bar, show, xlim, ylim, grid
    n_plot = 100
    delta_x_plot = (float(x_end) - x_begin) / n_plot
    x = [x_begin + k * delta_x_plot for k in xrange(n_plot)]
    y = [f(x[k]) for k in xrange(n_plot)]
    x += [x_end, x_end, x_begin]
    y += [f(x_end), 0.0, 0.0]

    fill(x, y)

    n_plot = n_interval
    delta_x_plot = (float(x_end) - x_begin) / n_plot
    x = [x_begin + k * delta_x_plot for k in xrange(n_plot)]
    y = [f(xk + 0.5 * delta_x_plot) for xk in x]
    x += [x_end]
    y += [0]

    bar(x, y, width=delta_x_plot, color='g', alpha=0.3)

    n_plot = n_interval
    delta_x_plot = (float(x_end) - float(x_begin)) / n_plot
    x = [x_begin + k * delta_x_plot for k in xrange(n_plot)]
    y = [f(xk) for xk in x]
    x += [x_end, x_end, x_begin]
    y += [f(x_end), 0.0, 0.0]

    fill(x, y, color='r', alpha=0.2)

    xlim(x_begin, x_end)
    ylim(0.0, ylim()[1])
    grid()
    show()
if "__main__" == __name__:
    main()