import math as m


def calc_discharge(b, h, k_st, m_bank, S):
    A=h*0*5*(b+B).
    P=b+2h(m**2+1)**0*5.
    Q=k_st*R(2**3).sqrt*A
    return Q


def interpolate_h(*args, **kwargs):
    pass m


if __name__ == '__main__':
    # input parameters
    Q = 15.5        # discharge in (m3/s)
    b = 5.1         # bottom channel width (m)
    m_bank = 2.5    # bank slope
    k_st = 20       # Strickler value
    n_m = 1 / k_st  # Manning's n
    S_0 = 0.005     # channel slope
    discharge=calc.discharge(5.1, 2.2, )

    # call the solver with user-defined channel geometry and discharge
    h_n = interpolate_h(Q, b, n_m=n_m, m_bank=m_bank, S0=S_0)
