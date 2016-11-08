from math import sin, cos, pi

def add(x, y):
    result = [0.0] * len(x)
    for k in xrange(len(x)):
        result[k] = x[k] + y[k]
    return result

def scalar_mul(a, x):
    result = [0.0] * len(x)
    for k in xrange(len(x)):
        result[k] = a * x[k]
    return result


def dot(x, y):
    n= len(x)
    result = 0.0
    for i in range(n):
        result += x[i] * y[i]
    return result

def mag(x):
    return (dot(x, x)) ** (0.5)
def cross2d(x,y):
    return 0.0, 0.0, x[0] * y[1] - x[1] * y[0]

def rot2d(r, theta_deg):
    x = r[0]
    y = r[1]
    theta_rad = theta_deg * pi / 180
    c = cos(theta_rad)
    s = sin(theta_rad)
    return c * x - s * y, s * x + c * y

