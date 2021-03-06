

        # add ordinal_x
        psrs = Pulsar.objects.filter(x_ray=True, duplicate=False, p0__gt=0.01).order_by('raj')
        for i in xrange(len(psrs)):
            psrs[i].ordinal_x = i+1
            psrs[i].save()


    def calculations(self, p):
        print p.name
        try: p.dotP_15 = p.p1 / 1e-15
        except: print 'W (1)'
        try: p.t_6 = p.t / 1e6
        except: print 'W (2)'
        try: p.t_6_minus = p.t_minus / 1e6
        except: print 'W (3)'
        try: p.t_6_plus = p.t_plus / 1e6
        except:print 'W (4)'
        try: p.a = pi * p.r ** 2.
        except: print 'W (5)'
        try: p.a_dp = 6.58429132402614e8 / float(p.p0)
        except: print 'W (6)'
        try: p.r_dp = ( p.a_dp / pi )**0.5
        except: print 'W (7)'
        try: p.b = p.a_dp / p.a
        except: pass
        try: p.bsurf2 = 2.02 * 1e12 * float(p.p0) ** 0.5 * p.dotP_15 ** 0.5
        except: print 'W (9)'
        try: p.b_14dp =  p.bsurf2 / 1e14
        except: print 'W (10)'
        try: p.b_14 = p.b * p.b_14dp
        except: print 'W (11)'
        try: p.l_sd = 3.94784176043574e31 * p.dotP_15 / float(p.p0)**3.
        except: print 'W (12)'
        try: p.xray_eff = p.l_bol / p.l_sd
        except: print 'W (13)'
        try: p.xray_eff2 = p.l_bol2 / p.l_sd
        except: print 'W (14)'
        try: p.xray_nonth = p.l_nonth / p.l_sd
        except: print 'W (15)'

        if p.best_age == 0:
            p.best_age = p.age

        # distance errors
        if p.best_dist == 0:
            p.best_dist = p.dist_bb
        if p.best_dist_plus == 0:
            dists  = [p.dist_dm_cl_plus, p.dist_pi_plus]
            while True:
                try: dists.remove(0.)
                except: break
            try: p.best_dist_plus = min(dists)
            except: pass
        if p.best_dist_minus == 0:
            dists = [p.dist_dm_cl_minus, p.dist_pi_minus]
            while True:
                try: dists.remove(0.)
                except: break
            try: p.best_dist_minus = min(dists)
            except: pass

        # from distance and temperature errors
        try:
            flux = p.l_bol / (4. * pi * p.dist_bb ** 2.)
            p.l_bol_dist = 4. * pi * flux * p.best_dist ** 2.
            lbol_min = 4. * pi * flux * (p.best_dist - p.best_dist_minus) ** 2.
            lbol_max = 4. * pi * flux * (p.best_dist + p.best_dist_plus) ** 2.
            p.l_bol_dist_plus = lbol_max - p.l_bol_dist
            p.l_bol_dist_minus = p.l_bol_dist - lbol_min
            p.r_dist = (p.l_bol_dist /  (2. * pi *  c.sigma * p.t ** 4.)) ** 0.5 # two spots
            r_min = ((p.l_bol_dist - p.l_bol_dist_minus) /
                (2. * pi *  c.sigma * (p.t + p.t_plus) ** 4.)) ** 0.5
            r_max = ((p.l_bol_dist + p.l_bol_dist_minus) /
                (2. * pi * c.sigma * (p.t - p.t_minus) **4.)) ** 0.5
            p.r_dist_minus = p.r_dist - r_min
            p.r_dist_plus = r_max - p.r_dist
            a = 2. * pi * p.r_dist ** 2.
            p.b_14_dist = p.a_dp / a * p.b_14dp
            a = 2. * pi * r_min ** 2. # two spots
            p.b_14_dist_plus =  p.a_dp / a * p.b_14dp - p.b_14_dist
            a = 2. * pi * r_max ** 2. # two spots
            p.b_14_dist_minus = p.b_14_dist - p.a_dp / a * p.b_14dp
        except: pass

        # bb fit
        try:
            r_min = p.r - p.r_minus
            r_max = p.r + p.r_plus
            a_min = pi * r_min ** 2.
            a_max = pi * r_max ** 2.
            b_max = p.a_dp / a_min
            b_min = p.a_dp / a_max
            p.b_14_minus = (p.b - b_min) * p.b_14dp
            p.b_14_plus = (b_max - p.b) * p.b_14dp
        except: pass

        # dist errors when there is no r error (J2021..)
        if p.b_14_minus == 0.:
            p.b_14_minus = p.b_14_dist_minus
        if p.b_14_plus == 0.:
            p.b_14_plus = p.b_14_dist_plus

        # try to calculate p_2 and p_3 from deg values
        try:
            p.p2 = float(p.p0) * p.p2_deg / 360.
        except: pass
        try: p.p2_plus = float(p.p0) * p.p2_deg_plus / 360.
        except: pass
        try: p.p2_minus = float(p.p0) * p.p2_deg_minus / 360.
        except: pass
        try:
            if p.p3==0.:
                p.p3 = p.p3_p0 * float(p.p0)
            else:
                p.p3_p0 = p.p3 / float(p.p0)
        except: pass
        try:
            if p.p3_plus ==0.:
                p.p3_plus = p.p3_p0_plus * float(p.p0)
            else:
                p.p3_p0_plus = p.p3_plus / float(p.p0)
        except: pass
        try:
            if p.p3_minus == 0.:
                p.p3_minus = p.p3_p0_minus * float(p.p0)
            else:
                p.p3_p0_minus = p.p3_minus / float(p.p0)
        except: pass



    def ev_to_k(self, t_ev):
        return t_ev / 8.61734315e-5

    def radius_from_area(self, a):
        return (a / pi) ** 0.5

    def lbol_radius(self, t, r):
        """ Bolometric luminosity for  hot spot sigma T^4 A (radius)"""
        return c.sigma * t ** 4. * pi * r ** 2.

    def radius_from_lt_simple(self, l_bol, t):
        return (l_bol / (c.sigma * t ** 4. * pi)) ** 0.5

    def k_to_ev(self, t_k):
        return t_k * 8.61734315e-5

    def lnonth_powers(self, pow_):
        l_nth = 0.
        l_nth_plus = 0.
        l_nth_minus = 0.
        l_nth_min = 0.
        l_nth_max = 0.
        for p in pow_:
            l_nth += 10. ** p[0]
            l_nth_max += 10 ** (p[0]+p[1])
            l_nth_min += 10 ** (p[0]-p[2])
        l_nth_plus = l_nth_max - l_nth
        l_nth_minus = l_nth - l_nth_min
        return l_nth, l_nth_plus, l_nth_minus


    def flux_ep(self, eps, t_6=None):
        """ to calculate in and off window flux/luminosity
        """
        try:
            return 2 * pi / c.c ** 2. * c.h *  eps** 3. / c.h ** 3. / \
               (exp(eps/(c.k * t_6 * 1e6))-1.)
        except:
            return 0.

    def in_window(self, t_6, win_kev_min=0.5, win_kev_max=8.):

        eps_th = c.k * t_6 * 1e6

        win_min = win_kev_min * 1e3 * 1.60217646e-12
        win_max = win_kev_max * 1e3 * 1.60217646e-12

        res1 = quad(self.flux_ep, win_min, win_max, args=(t_6, ))[0]
        #print 'F_BB = %.2e (in window)'%res1
        res2 = quad(self.flux_ep, 0.01*eps_th, 100.*eps_th, args=(t_6, ))[0]
        #res2 = quad(self.flux_ep, 0.1*win_min, 10.*win_max, args=(mod_bb2, t_6, ))[0]
        #print 'F_BB_full = %.2e'%res2
        return res2/res1


    def b0943(self, p, flux, flux_plus, flux_minus, f_pl, f_pl_plus, f_pl_minus):
        x = self.in_window(3.2)
        f = 0.98
        l_pc = x * 1./f *flux* pi * ((p.dist_bb) * 1e3 * 3.0857e18) ** 2.
        l_pc_max = x * 1./f * (flux+flux_plus) * pi * ((p.dist_bb+p.dist_dm_cl_plus) * 1e3 * 3.0857e18) ** 2.
        l_pc_min = x * 1./f * (flux-flux_minus) * pi * ((p.dist_bb-p.dist_dm_cl_minus) * 1e3 * 3.0857e18) ** 2.

        l_pl = f_pl * 4. * pi * (p.dist_bb * 1e3 * 3.0857e18) ** 2. # flux recalculation, maximum value - no anisotropy
        l_pl_max = (f_pl+f_pl_plus) * 4. * pi * ((p.dist_bb+p.dist_dm_cl_plus) * 1e3 * 3.0857e18) ** 2. # flux recalculation, maximum value - no anisotropy
        l_pl_min = (f_pl-f_pl_minus) * 4. * pi * ((p.dist_bb-p.dist_dm_cl_minus) * 1e3 * 3.0857e18) ** 2. # flux recalculation, maximum value - no anisotropy

        r_bb = ( l_pc / (c.sigma * pi * p.t ** 4.)) ** 0.5
        r_bb_max = ( l_pc_max / (c.sigma * pi * (p.t-p.t_minus) ** 4.)) ** 0.5
        r_bb_min = ( l_pc_min / (c.sigma * pi * (p.t+p.t_plus) ** 4.)) ** 0.5

        b = (p.r_dp / r_bb) ** 2.
        b_min = (p.r_dp / r_bb_max) ** 2.
        b_max = (p.r_dp / r_bb_min) ** 2.

        b_14 = b * p.b_14dp
        b_14_min = b_min * p.b_14dp
        b_14_max = b_max * p.b_14dp

        #print b, b_min, b_max
        #print 'B_14 =', b_14, 'B_14_min =', b_14_min, 'B_14_max =', b_14_max

        p.l_bol = l_pc
        p.l_bol_plus = l_pc_max - l_pc
        p.l_bol_minus = l_pc - l_pc_min
        p.l_nonth = l_pl
        p.l_nonth_plus = l_pl_max - l_pl
        p.l_nonth_minus = l_pl - l_pl_min
        p.r = r_bb
        p.r_plus = r_bb_max - r_bb
        p.r_minus = r_bb - r_bb_min

        p.b_14 = b_14
        p.b_14_plus = b_14_max - b_14
        p.b_14_minus = b_14 - b_14_min

        print 'log10(l_bol) =', log10(l_pc), 'log10(l_nonth) =', log10(l_pl)
        print 'r_max = %.2f [m]'%(p.r_dp*sqrt(p.b_14dp/2.2)/1e2), 'r_min = %.2f [m]'%(p.r_dp*sqrt(p.b_14dp/2.6)/1e2)



###############################################################################
def main():
    p = Pulsars()
    #print (8.9e35 / (c.sigma * 4. * pi * 10e5**2))**(1./4.)
    #print (8.9e35/(4.*pi) / (c.sigma * 2. * pi * 7.96e+04 ** 2))**(1./4.)
    #print (0.1 * 8.9e35 / (c.sigma * 2. * pi * 7.96e+04 ** 2))**(1./4.)
    #t =  p.ev_to_k(1.4e3)
    #print '%.1e'%t
    #r = p.radius_from_lt_simple(1.1e33, t)
    #print 'R = %.1f [m]'%(r/1e2)
    #exit()
    #print p.ev_to_k(0.15e3)
    #print p.ev_to_k(0.11e3)
    #print p.ev_to_k(0.54e3)/1e6
    p.add_pulsars()
    print 'Bye'

###############################################################################
if __name__ == '__main__':
    main()

