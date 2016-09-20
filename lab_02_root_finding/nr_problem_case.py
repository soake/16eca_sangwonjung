import root_finding as rf

def g(x):
    return x ** 3 - 2 * x + 2

def dgdx(x):
    return  3.0 * x ** 2.0 -2.0

if "__main__"== __name__:
    x_nr = rf.newton(g, dgdx, 0)
    print ('x = %g, f(%g) = %g' % (x_nr, x_nr, g(x_nr)))
