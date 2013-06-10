from math import sin, pi

def get_t6(b_14):
    """
    from heating condition
    """
    return 1.1 * (b_14 ** 1.1 + 0.3)

def radio_lum(p):
    p0 = float(p.p0)
    p1 = float(p.p1)
    w = p.w10
    old_frac = sin(6./180. * pi) ** 2.
    frac = sin((1.24 * (500./10.) ** 0.5 * p0 ** (-0.5))/ 180. * pi ) ** 2.
    frac = old_frac
    old_delta = 0.04
    delta = w / 1e3 / p0
    delta = old_delta
    return 7.4e27 * delta / old_delta * frac / old_frac * p.dist ** 2. * p.s1400 #/ p0**0.5 #* (p1/1e-15) ** 0.2


def pseudo_lum(s_freq, p):
    p0 = float(p.p0)
    p1 = float(p.p1)
    return s_freq / 1e3  * (p.dist * 3.08567758e21) ** 2. * 1e-23 #/ p0**0.5 #* (p1/1e-15) ** 0.2
