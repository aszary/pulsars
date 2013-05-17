
        p15 = Pulsar.objects.get(name='B1055-52')
        p15.t = 1.79e6
        p15.t_plus = 0.06e6
        p15.t_minus = 0.06e6
        p15.r = 46000
        p15.r_plus = 6000
        p15.r_minus = 6000
        p15.t2 = 7.9e5
        p15.t2_plus = 0.3e5
        p15.t2_minus = 0.3e5
        p15.r2 = 12.3e5
        p15.r2_plus = 1.5e5
        p15.r2_minus = 0.7e5
        p15.l_bol = self.lbol_radius(p15.t, p15.r)
        p15.l_bol_sphere = 4. * self.lbol_radius(p15.t, p15.r)
        p15.l_bol2 = 4. * self.lbol_radius(p15.t2, p15.r2)
        p15.l_bol_sphere2 = 4. * self.lbol_radius(p15.t2, p15.r2)
        p15.dist_bb = 0.75
        p15.dist_dm_cl = 0.726
        p15.l_nonth = 8.1e30
        p15.pl = 1.7
        p15.pl_plus = 0.1
        p15.pl_minus = 0.1
        p15.articles = 'http://adsabs.harvard.edu/abs/2005ApJ...623.1051D;http://adsabs.harvard.edu/abs/2002nsps.conf..273P;http://adsabs.harvard.edu/abs/2007astro.ph..2426Z'
        p15.x_ray_info = 'page 25, no inf -> surface conversion, two component bb fit, no L_bol, diffrent values in second paper?! ... A_{\perp} [last update: 2012-03-30]'
        p15.cite = '\citet{2005_Deluca}'
        p15.spectrum = 'BB+BB+PL'
        p15.x_ray = True
        p15.comment = ''
        self.calculations(p15)
        p15.save()
        self.psrs.append(p15)

        p16 = Pulsar.objects.get(name='J1119-6127')
        #print self.ev_to_k(0.21e3) # from second paper
        p16.t_inf = 2.4e6
        p16.t_inf_plus = 0.3e6
        p16.t_inf_minus = 0.2e6
        p16.r_inf = 3.4e5
        p16.r_inf_plus = 1.8e5
        p16.r_inf_minus = 0.3e5
        p16.t = p16.t_inf / self.gr
        p16.t_plus = p16.t_inf_plus / self.gr
        p16.t_minus = p16.t_inf_minus / self.gr
        p16.r = p16.r_inf * self.gr
        p16.r_plus = p16.r_inf_plus * self.gr
        p16.r_minus = p16.r_inf_minus * self.gr
        p16.dist_bb = 8.4
        p16.l_bol = self.lbol_radius(p16.t, p16.r)
        p16.l_bol_sphere = 4. * self.lbol_radius(p16.t, p16.r)
        p16.l_nonth = 0.9e33
        p16.l_nonth_plus = 0.5e33
        p16.l_nonth_minus = 0.1e33
        p16.pl = 1.5
        p16.pl_plus = 0.3
        p16.pl_minus = 0.2
        p16.articles = 'http://adsabs.harvard.edu/abs/2007Ap%26SS.308...89G;http://adsabs.harvard.edu/abs/2008ApJ...684..532S;http://adsabs.harvard.edu/abs/2007astro.ph..2426Z;http://adsabs.harvard.edu/abs/2005ApJ...630..489G'
        p16.x_ray_info = 'page 3, no inf -> surface conversion, component is pulsing; fixed size in atmospheric fit (1.6kpc distance) [last update: 2012-03-30]'
        p16.cite = '\citet{2007_Gonzalez}, \citet{2012_Ng}'
        p16.spectrum = 'BB + PL'
        p16.x_ray = True
        p16.comment = 'G292.2-0.5'
        self.calculations(p16)
        p16.save()
        self.psrs.append(p16)

        p17 = Pulsar.objects.get(name='J1210-5226')
        p17.t_inf = 2.9e6
        p17.r_inf = 1.6e5
        p17.t = p17.t_inf / self.gr
        p17.r = p17.r_inf * self.gr
        p17.dist_bb = 2.45
        p17.t_atm = 1.6e6 / self.gr
        p17.r_atm = 11e5
        p17.l_bol = self.lbol_radius(p17.t, p17.r)
        p17.l_bol_sphere = 4. * self.lbol_radius(p17.t, p17.r)
        p17.articles = 'http://adsabs.harvard.edu/abs/2002nsps.conf..273P'
        p17.x_ray_info = 'page 10, radio quiet, no inf -> surface conversion, uncertainness in distance evaluation, no radio signal \dot{P} 1e-14 1e-17  A_{\perp} [last update: 2012-03-30]'
        p17.cite = '\citet{2002_Pavlov}'
        p17.spectrum = 'BB'
        p17.x_ray = True
        p17.comment = 'G296.5+10.0'
        self.calculations(p17)
        p17.save()
        self.psrs.append(p17)

        p18 = Pulsar.objects.get(name='J1357-6429')
        p18.t_inf = 1.7e6
        p18.t_inf_plus = 0.2e6
        p18.t_inf_minus = 0.2e6
        p18.r_inf = 2.5e5
        p18.r_inf_plus = 0.5e5
        p18.r_inf_minus = 0.5e5
        p18.t = p18.t_inf / self.gr
        p18.t_plus = p18.t_inf_plus / self.gr
        p18.t_minus = p18.t_inf_minus / self.gr
        p18.r = p18.r_inf * self.gr
        p18.r_plus = p18.r_inf_plus * self.gr
        p18.r_minus = p18.r_inf_minus * self.gr
        p18.dist_bb = 2.5
        p18.l_bol = self.lbol_radius(p18.t, p18.r)
        p18.l_bol_sphere = 4. * self.lbol_radius(p18.t, p18.r)
        p18.t_atm = 1e6
        p18.r_atm = 10e5
        p18.dist_dm_cl = 2.5
        p18.l_nonth = 1.4e32
        p18.pl = 1.3
        p18.pl_plus = 0.2
        p18.pl_minus = 0.2
        p18.articles = 'http://adsabs.harvard.edu/abs/2007ApJ...665L.143Z;http://adsabs.harvard.edu/abs/2012ApJ...744...81C'
        p18.x_ray_info = 'page 3, no inf -> surface conversion, A_{\perp} [last update: 2012-03-30]'
        p18.cite = '\citet{2007_Zavlin}'
        p18.spectrum = 'BB + PL'
        p18.x_ray = True
        p18.comment = ''
        self.calculations(p18)
        p18.save()
        self.psrs.append(p18)

        p19 = Pulsar.objects.get(name='B1706-44')
        p19.t_inf = 1.66e6
        p19.t_inf_plus = 0.17e6
        p19.t_inf_minus = 0.15e6
        p19.r_inf = 3.6e5
        p19.r_inf_plus = 0.9e5
        p19.r_inf_minus = 0.9e5
        p19.t = p19.t_inf / self.gr
        p19.t_plus = p19.t_inf_plus / self.gr
        p19.t_minus = p19.t_inf_minus / self.gr
        p19.r = p19.r_inf * self.gr
        p19.r_plus = p19.r_inf_plus * self.gr
        p19.r_minus = p19.r_inf_minus * self.gr
        p19.dist_bb = 2.5
        p19.t_atm = 1e6
        p19.r_atm = 12e5
        p19.dist_dm_cl = 2.311
        p19.l_bol = self.lbol_radius(p19.t, p19.r)
        p19.l_bol_sphere = 4. * self.lbol_radius(p19.t, p19.r)
        p19.l_nonth = 1.45e32
        p19.l_nonth_plus = 0.46e32
        p19.l_nonth_minus = 0.08e32
        p19.pl = 2.0
        p19.pl_plus = 0.5
        p19.pl_minus = 0.5
        p19.articles = 'http://adsabs.harvard.edu/abs/2002ApJ...567L.125G;http://adsabs.harvard.edu/abs/2007astro.ph..2426Z;http://adsabs.harvard.edu/abs/2006ApJ...639..377M'
        p19.x_ray_info = 'page 5, no inf -> surface conversion, thermal + non-thermal components A_{\perp} [last update: 2012-03-30]'
        p19.cite = '\citet{2002_Gotthelf}'
        p19.spectrum = 'BB + PL'
        p19.x_ray = True
        p19.comment = 'G343.1-02.3'
        self.calculations(p19)
        p19.save()
        self.psrs.append(p19)

        p20 = Pulsar.objects.get(name='J1809-1917')
        p20.t = self.ev_to_k(0.17e3)
        p20.t_plus = self.ev_to_k(0.03e3)
        p20.t_minus = self.ev_to_k(0.03e3)
        p20.r = self.radius_from_area(2.84e6*1e4)
        p20.r_plus = self.radius_from_area(2.66e6*1e4)
        p20.r_minus = self.radius_from_area(1.51e6*1e4)
        p20.dist_bb = 3.5
        p20.dist_dm_cl = 3.5
        p20.l_bol = self.lbol_radius(p20.t, p20.r)
        p20.l_bol_sphere = 4. * self.lbol_radius(p20.t, p20.r)
        p20.l_nonth = 0.37e32
        p20.l_nonth_plus = 0.12e32
        p20.l_nonth_minus = 0.1e32
        p20.pl = 1.23
        p20.pl_plus = 0.62
        p20.pl_minus = 0.62
        p20.articles = 'http://adsabs.harvard.edu/abs/2007ApJ...670..655K'
        p20.x_ray_info = 'page 5, 7(graph), no inf -> surface conversion, dist_dm_cl from paper A_{\perp} [last update: 2012-03-30]'
        p20.cite = '\citet{2007_Kargaltsev}'
        p20.spectrum = 'BB + PL'
        p20.x_ray = True
        p20.comment = ''
        self.calculations(p20)
        p20.save()
        self.psrs.append(p20)

        p21 = Pulsar.objects.get(name='B1823-13')
        p21.r = self.radius_from_area(20e10)
        p21.t = self.ev_to_k(139.)
        p21.t_plus = self.ev_to_k(9.)
        p21.t_minus = self.ev_to_k(6.)
        p21.dist_dm_cl = 3.9
        p21.dist_bb = 4
        p21.l_nonth = 0.6e32
        p21.l_bol = self.lbol_radius(p21.t, p21.r)
        p21.l_bol_sphere = 4. * self.lbol_radius(p21.t, p21.r)
        p21.pl = 1.7
        p21.pl_plus = 0.7
        p21.pl_minus = 0.7
        p21.articles = 'http://adsabs.harvard.edu/abs/2008ApJ...675..683P'
        p21.x_ray_info =  'page 13, no inf -> surface conversion, very bad photon statistics, R_BB fixed in fits - larger R_BB fit in paper, A_{\perp} [last update: 2012-03-30]'
        p21.cite = '\citet{2008_Pavlov}'
        p21.spectrum = 'BB + PL'
        p21.x_ray = True
        p21.comment = 'Vela-like'
        self.calculations(p21)
        p21.save()
        self.psrs.append(p21)

        p22 = Pulsar.objects.get(name='B1916+14')
        p22.t = self.ev_to_k(0.13e3)
        p22.t_plus = self.ev_to_k(0.01e3)
        p22.t_minus = self.ev_to_k(0.01e3)
        p22.r = 0.8e5
        p22.r_plus = 0.1e5
        p22.r_minus = 0.1e5
        p22.dist_bb = 2.1
        p22.dist_dm_cl = 2.059
        p22.l_bol = self.lbol_radius(p22.t, p22.r)
        p22.l_bol_sphere = 4. * self.lbol_radius(p22.t, p22.r)
        p22.l_nonth = 1e32
        p22.pl = 3.5
        p22.pl_plus = 1.6
        p22.pl_minus = 0.7
        p22.articles = 'http://adsabs.harvard.edu/abs/2009ApJ...704.1321Z'
        p22.x_ray_info = 'page 12, BB, no inf -> surface conversion, check table for more pulsars, A_{\perp} [last update: 2012-03-30]'
        p22.cite = '\citet{2009_Zhu}'
        p22.spectrum = 'BB, PL'
        p22.x_ray = True
        p22.comment = ''
        self.calculations(p22)
        p22.save()
        self.psrs.append(p22)

        p23 = Pulsar.objects.get(name='J2043+2740')
        p23.t_inf = self.ev_to_k(0.125e3)
        p23.t_inf_plus = self.ev_to_k(0.03e3)
        p23.t_inf_minus = self.ev_to_k(0.03e3)
        p23.r_inf = 0.467e5
        p23.r_inf_plus = 0.2e5
        p23.r_inf_minus = 0.2e5
        p23.t = p23.t_inf / self.gr
        p23.t_plus = p23.t_inf_plus / self.gr
        p23.t_minus = p23.t_inf_minus / self.gr
        p23.r = p23.r_inf * self.gr
        p23.r_plus = p23.r_inf_plus * self.gr
        p23.r_minus = p23.r_inf_minus * self.gr
        p23.dist_bb = 1.8
        p23.l_bol = self.lbol_radius(p23.t, p23.r)
        p23.l_bol_sphere =  4. * self.lbol_radius(p23.t, p23.r)
        p23.l_nonth, p23.l_nonth_plus, p23.l_nonth_minus = \
            self.lnonth_powers([[31.40,0.22,0.45],[29.90,0.22,0.45]])
        #p23.l_nonth = 8.69e-14 * 4. * pi * (p23.dist_bb * 1e3 * 3.0857e18) ** 2.  # flux recalculation
        p23.t_atm = 0.6e6
        p23.r_atm = 9.0e5
        p23.dist_dm_cl = 1.802
        p23.pl = 2.8
        p23.pl_plus = 1
        p23.pl_minus = 0.8
        p23.articles = 'http://adsabs.harvard.edu/abs/2004ApJ...615..908B;http://adsabs.harvard.edu/abs/2007astro.ph..2426Z'
        p23.x_ray_info = 'page 27, R_BB fixed in fits - larger R_BB fit in paper, inf -> surface conversion done (see text T_inf), different values in second paper ?, errors from bb fit,  A_{\perp}? [last update: 2012-03-30]'
        p23.cite = '\citet{2004_Becker}'
        p23.spectrum = 'BB + PL'
        p23.x_ray = True
        p23.comment = ''
        self.calculations(p23)
        p23.save()
        self.psrs.append(p23)

        p24 = Pulsar.objects.get(name='B2334+61')
        p24.t_inf = 1.62e6
        p24.t_inf_plus = 0.35e6
        p24.t_inf_minus = 0.58e6
        p24.r_inf = 1.66e5
        p24.r_inf_plus = 0.59e5
        p24.r_inf_minus = 0.39e5
        p24.t = p24.t_inf / self.gr
        p24.t_plus = p24.t_inf_plus / self.gr
        p24.t_minus = p24.t_inf_minus / self.gr
        p24.r = p24.r_inf * self.gr
        p24.r_plus = p24.r_inf_plus * self.gr
        p24.r_minus = p24.r_inf_minus * self.gr
        p24.dist_bb = 3.1
        p24.l_bol = self.lbol_radius(p24.t, p24.r)
        p24.l_bol_sphere = 4. * self.lbol_radius(p24.t, p24.r)
        p24.l_nonth = 3.1e-14 * 4. * pi * (3.1e3 * 3.0857e18) ** 2.  #- p24.l_bol # flux recalculation
        p24.t_atm = 0.76e6
        p24.r_atm = 10e5
        p24.dist_dm_cl = 3.131
        p24.pl = 2.2
        p24.pl_plus = 3.0
        p24.pl_minus = 1.4
        p24.articles = 'http://adsabs.harvard.edu/abs/2006ApJ...639..377M;http://adsabs.harvard.edu/abs/2007astro.ph..2426Z'
        p24.x_ray_info = 'pag 4,14, inf -> surface conversion done, no pulsation, different values in second paper ? (, R_bb 1.66e5 from text different fit?) A_{\perp}? no data (R_bb) for BB+PL (BB params from text), spectrum dominated by BB [last update: 2011-03-30]'
        p24.cite = '\citet{2006_Mcgowan}'
        p24.spectrum = 'BB + PL'
        p24.x_ray = True
        p24.comment = ''
        self.calculations(p24)
        p24.save()
        self.psrs.append(p24)

        p26 = Pulsar.objects.get(name='J0205+6449')
        p26.t_inf = 1.3e6 #self.ev_to_k(150)
        p26.r_inf = 10.7e5 #2.6e5
        p26.t = p26.t_inf / self.gr
        p26.r = p26.r_inf * self.gr
        #p26.l_bol = self.lbol_radius(p26.t, p26.r)
        p26.l_bol = 4. * self.lbol_radius(p26.t, p26.r) # whole surface
        p26.l_bol_sphere = 4. * self.lbol_radius(p26.t, p26.r)
        p26.dist_bb = 3.2
        # PL only fit
        #p26.l_nonth, p26.l_nonth_plus, p26.l_nonth_minus = \
        #    self.lnonth_powers([[32.64,0.22,0.45],[32.68,0.22, 0.45]])
        # BB+PL
        p26.l_nonth = 1.02e-12 * 4. * pi * (p26.dist_bb * 1e3 * 3.0857e18) ** 2. # flux recalculation
        #print self.lbol_radius(1.3e6 / self.gr, 10.7e5 * self.gr)
        p26.t_atm = 1.08e6
        p26.r_atm = 10e5
        p26.pl = 1.78
        p26.pl_plus = 0.02
        p26.pl_minus = 0.04
        p26.articles = 'http://adsabs.harvard.edu/abs/2004ApJ...616..403S'
        p26.x_ray_info = 'page 8 (in text), different value in table (page 9) - R_bb set to star radius there, PL from table, redshifted or unredshifted? [last update: 2012-03-30]'
        p26.spectrum = 'BB + PL'
        p26.cite = '\citet{2004_Slane}'
        p26.x_ray = True
        p26.comment = '3C58'
        self.calculations(p26)
        p26.save()
        self.psrs.append(p26)

        p27 = Pulsar.objects.get(name='B0355+54')
        p27.r_inf = 0.12e5
        p27.r_inf_plus = 0.16e5
        p27.r_inf_minus = 0.07e5
        p27.t_inf = 2.32e6
        p27.t_inf_plus = 1.16e6
        p27.t_inf_minus = 0.81e6
        p27.r = p27.r_inf * self.gr
        p27.r_plus = p27.r_inf_plus * self.gr
        p27.r_minus = p27.r_inf_minus * self.gr
        p27.t = p27.t_inf / self.gr
        p27.t_plus = p27.t_inf_plus / self.gr
        p27.t_minus = p27.t_inf_minus / self.gr
        p27.dist_bb = 1.04
        p27.l_bol = self.lbol_radius(p27.t, p27.r)
        p27.l_bol_sphere = 4. * self.lbol_radius(p27.t, p27.r)
        p27.l_nonth, p27.l_nonth_plus, p27.l_nonth_minus = \
            self.lnonth_powers([[30.21,0.64,0.71],[30.83,0.57,0.33]])
        #p27.l_nonth = 6.4e-14 * 4. * pi * (p27.dist_bb * 1e3 * 3.0857e18) ** 2. # flux recalculation
        p27.dist_dm_cl = 1.447
        p27.dist_pi = 1.04
        p27.dist_pi_plus = 0.21
        p27.dist_pi_minus = 0.16
        p27.pl = 1.
        p27.pl_plus = 0.2
        p27.pl_minus = 0.2
        p27.articles = 'http://adsabs.harvard.edu/abs/2007Ap%26SS.308..309M;http://adsabs.harvard.edu/abs/1994ApJ...437..458S'
        p27.x_ray_info = 'page (312), inf -> surface conversion done (is it ok?) [last update: 2011-03-30]'
        p27.cite = '\citet{2007_McGowan},\citet{1994_Slane}'
        p27.spectrum = 'BB + PL'
        p27.x_ray = True
        self.calculations(p27)
        p27.save()
        self.psrs.append(p27)

        p28 = Pulsar.objects.get(name='B0531+21')
        #p28.t_inf = self.ev_to_k(0.1e3)
        #p28.t_inf_plus = self.ev_to_k(7.2e3)
        #p28.t_inf_minus = self.ev_to_k(7.2e3)
        #p28.dist_bb = 2
        #p28.r_inf = 1e5 * sqrt(44.) * p28.dist_bb / 10
        #p28.r_inf_plus = 1e5 * sqrt(31000.) * p28.dist_bb / 10.
        #p28.r_inf_minus = 1e5 * sqrt(31000.) * p28.dist_bb / 10.
        p28.dist_bb = p28.dist
        p28.l_nonth = 8.912509381337513e+35
        p28.l_nonth_plus = 4.5771194445791014e+35
        p28.l_nonth_minus = 3.0240728277815817e+35
        p28.pl = 1.63
        p28.pl_plus = 0.07
        p28.pl_minus = 0.07
        p28.articles = 'http://adsabs.harvard.edu/abs/2009ASSL..357...91B;http://adsabs.harvard.edu/abs/2011ApJ...743..139W;http://adsabs.harvard.edu/abs/2004ApJ...601.1050W;http://adsabs.harvard.edu/abs/1997A%26A...326..682B;http://adsabs.harvard.edu/abs/2001A%26A...365L.212W'
        p28.x_ray_info = 'page 41 (Becker), (no BB fit, PL dominated) [last update: 2011-03-30]'
        p28.comment = 'Crab'
        p28.spectrum = 'PL'
        p28.cite = '\citet{2009_Becker}'
        p28.x_ray = True
        self.calculations(p28)
        p28.save()
        self.psrs.append(p28)


        p29 = Pulsar.objects.get(name='B1951+32')
        p29.r = 2.2e5
        p29.r_plus = 1.4e5
        p29.r_minus = 0.8e5
        p29.t = self.ev_to_k(0.13e3)
        p29.t_plus = self.ev_to_k(0.02e3)
        p29.t_minus = self.ev_to_k(0.02e3)
        p29.dist_bb = 2.0
        p29.l_bol = self.lbol_radius(p29.t, p29.r)
        p29.l_bol_sphere = 4. * self.lbol_radius(p29.t, p29.r)
        #p29.l_nonth = 1.82451e+33
        p29.l_nonth = 3.5e-12 * 4. * pi * (p29.dist_bb * 1e3 * 3.0857e18) ** 2. # flux recalculation
        p29.l_nonth_minus = 9.30906e+32
        p29.l_nonth_plus = 1.7687e+32
        p29.dist_dm_cl = 3.137
        p29.pl = 1.63
        p29.pl_plus = 0.03
        p29.pl_minus = 0.05
        p29.articles = 'http://adsabs.harvard.edu/abs/2005ApJ...628..931L'
        p29.x_ray_info = 'page 3, no inf -> surface conversion done [last update: 2012-03-30]'
        p29.cite = '\citet{2005_Li}'
        p29.spectrum = 'BB + PL'
        p29.comment = 'CTB 80'
        p29.x_ray = True
        self.calculations(p29)
        p29.save()
        self.psrs.append(p29)

        p30 = Pulsar.objects.get(name='B1509-58')
        p30.l_nonth, p30.l_nonth_plus, p30.l_nonth_minus = \
            self.lnonth_powers([[34.64,0.19,0.35],[35.12,0.2,0.37]])
        p30.dist_dm_cl = 4.181
        p30.dist_bb = 4.181
        p30.dist_dm_cl_plus = 4.784 - p30.dist_dm_cl
        p30.dist_dm_cl_minus = p30.dist_dm_cl - 3.570
        p30.pl = 1.19
        p30.pl_plus = 0.04
        p30.pl_minus = 0.04
        p30.articles = 'http://adsabs.harvard.edu/abs/2009ASSL..357...91B;http://adsabs.harvard.edu/abs/2001A%26A...375..397C;http://adsabs.harvard.edu/abs/2006ApJ...640..929D'
        p30.x_ray_info = 'page 41 (Becker), no BB fit, PL dominated  [last update: 2012-03-30]'
        p30.cite = '\citet{2001_Cusumano}, \citet{2006_DeLaney}, \citet{2009_Becker}'
        p30.spectrum = 'PL'
        p30.x_ray = True
        p30.comment = 'Crab-like pulsar'
        self.calculations(p30)
        p30.save()
        self.psrs.append(p30)

        p31 = Pulsar.objects.get(name='J1930+1852')
        p31.dist_bb = 5.
        p31.l_nonth, p31.l_nonth_plus, p31.l_nonth_minus = \
            self.lnonth_powers([[33.42,0.22,0.45],[33.75,0.22,0.45]])
        # different band
        #p31.l_nonth = 1.7e-12 * 4. * pi * (p31.dist_bb * 1e3 * 3.0857e18) ** 2.  # flux recalculation
        p31.pl = 1.2
        p31.pl_plus = 0.2
        p31.pl_minus = 0.2
        p31.articles = 'http://adsabs.harvard.edu/abs/2007ApJ...663..315L;http://adsabs.harvard.edu/abs/2002ApJ...574L..71C'
        p31.x_ray_info = '?? [last update: 2012-03-30]'
        p31.cite = '\citet{2007_Lu}, \citet{2002_Camilo}'
        p31.spectrum = 'PL'
        p31.x_ray = True
        p31.comment = 'Crab-like pulsar'
        self.calculations(p31)
        p31.save()
        self.psrs.append(p31)

        p32 = Pulsar.objects.get(name='J1617-5055')
        p32.dist_bb = 6.5
        p32.l_nonth = 17.92e33
        p32.l_nonth_minus = 0.07e33
        p32.l_nonth_plus = 0.07e33
        p32.pl = 1.14
        p32.pl_plus = 0.06
        p32.pl_minus = 0.06
        p32.articles = 'http://adsabs.harvard.edu/abs/2009ApJ...690..891K;http://adsabs.harvard.edu/abs/2002nsps.conf...64B'
        p32.x_ray_info = 'page (889, table) [last update: 2012-03-30]'
        p32.cite = '\citet{2009_Kargaltsev}, \citet{2002_Becker}'
        p32.spectrum = 'PL'
        p32.x_ray = True
        p32.comment='Crab-like pulsar'
        self.calculations(p32)
        p32.save()
        self.psrs.append(p32)

        p33 = Pulsar.objects.get(name='J1747-2958')
        #p33.r = 200e2
        #p33.t = self.ev_to_k(1e3)
        p33.dist_bb = 5.
        #p33.l_bol = self.lbol_radius(p33.t, p33.r)
        #p33.l_bol_sphere = 4. * self.lbol_radius(p33.t, p33.r)
        p33.l_nonth, p33.l_nonth_plus, p33.l_nonth_minus = \
            self.lnonth_powers([[33.82,0.26,0.23],[33.75,0.24,0.23]])
        p33.pl = 1.8
        p33.pl_plus = 0.08
        p33.pl_minus = 0.08
        p33.articles = 'http://adsabs.harvard.edu/abs/2004ApJ...616..383G;http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        p33.x_ray_info = ' PL fit values from Becker paper, page 8 (BB) [last update: 2012-03-30]'
        p33.cite = '\citet{2004_Gaensler}'
        p33.spectrum = 'PL, BB'
        p33.x_ray = True
        p33.comment = 'Mouse'
        self.calculations(p33)
        p33.save()
        self.psrs.append(p33)

        p34 = Pulsar.objects.get(name='J1124-5916')
        p34.dist_bb = 6
        p34.l_nonth, p34.l_nonth_plus, p34.l_nonth_minus = \
            self.lnonth_powers([[32.54,0.22,0.45],[32.66,0.22,0.45]])
        p34.pl = 1.6
        p34.pl_plus = 0.1
        p34.pl_minus = 0.1
        p34.articles = 'http://adsabs.harvard.edu/abs/2003ApJ...591L.139H;http://adsabs.harvard.edu/abs/2003ApJ...583L..91G;http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        p34.x_ray_info = 'PL fit from Becker, only upper limit for BB [last update: 2012-03-30]'
        p34.cite = '\citet{2003_Hughes},\citet{2003_Gonzales}'
        p34.spectrum = 'PL'
        p34.x_ray = True
        p34.comment = 'Vela-like pulsar'#'G292.0+1.8'
        self.calculations(p34)
        p34.save()
        self.psrs.append(p34)

        p35 = Pulsar.objects.get(name='B1046-58')
        p35.dist_bb = 2.7
        p35.dist_dm_cl = 2.714
        p35.dist_dm_cl_plus = 3.060 - p35.dist_dm_cl
        p35.dist_dm_cl_plus = p35.dist_dm_cl - 2.363
        p35.l_nonth, p35.l_nonth_plus, p35.l_nonth_minus = \
            self.lnonth_powers([[31.73,0.52,0.46],[31.75,0.3,0.43]])
        p35.pl = 1.7
        p35.pl_plus = 0.4
        p35.pl_minus = 0.2
        p35.articles = 'http://adsabs.harvard.edu/abs/2006ApJ...652..569G;http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        p35.x_ray_info = 'PL fit from Becker [last update: 2012-03-30]'
        p35.cite = '\citet{2006_Gonzalez}'
        p35.spectrum = 'PL'
        p35.x_ray = True
        p35.comment = 'Vela-like pulsar'
        self.calculations(p35)
        p35.save()
        self.psrs.append(p35)

        p36 = Pulsar.objects.get(name='J1811-1925')
        p36.dist_bb = 5.
        p36.l_nonth, p36.l_nonth_plus, p36.l_nonth_minus = \
            self.lnonth_powers([[33.23,0.29,0.4],[33.88,0.18,0.31]])
        #p36.l_nonth = 4.2e-12 * 4. * pi * (p36.dist_bb * 1e3 * 3.0857e18) ** 2.  # flux recalculation
        p36.pl = 0.97 # 1.3
        p36.pl_plus = 0.39
        p36.pl_minus = 0.32
        p36.articles = 'http://adsabs.harvard.edu/abs/2003ApJ...588..992R;http://adsabs.harvard.edu/abs/2004AIPC..714..306R'
        p36.x_ray_info = 'PL fit from Becker (different Gamma and flux in paper), radio quiet [last update: 2012-03-30]'
        p36.cite = '\citet{2003_Roberts}, \citet{2004_Roberts}'
        p36.spectrum = 'PL'
        p36.x_ray = True
        p36.comment = 'G11.2-0.3'
        self.calculations(p36)
        p36.save()
        self.psrs.append(p36)

        p37 = Pulsar.objects.get(name='J0537-6910')
        p37.dist_bb = 47
        p37.l_nonth, p37.l_nonth_plus, p37.l_nonth_minus = \
            self.lnonth_powers([[35.68,0.19,0.34],[35.61,0.2,0.37]])
        p37.pl = 1.8
        p37.pl_plus = 0.1
        p37.pl_minus = 0.1
        p37.articles = 'http://adsabs.harvard.edu/abs/2005A%26A...431..659M;http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        p37.x_ray_info = 'PL fit from Becker (different Gamma and flux in paper), radio quiet [last update: 2012-03-30]'
        p37.cite = '\citet{2005_Mignani}'
        p37.spectrum = 'PL'
        p37.comment = 'N157B, LMC'
        p37.x_ray = True
        self.calculations(p37)
        p37.save()
        self.psrs.append(p37)

        p38 = Pulsar.objects.get(name='B1259-63')
        p38.dist_bb = 2
        p38.l_nonth, p38.l_nonth_plus, p38.l_nonth_minus = \
            self.lnonth_powers([[32.55,0.25,0.54],[32.58,0.39,0.51]])
        p38.pl = 1.69
        p38.pl_plus = 0.04
        p38.pl_minus = 0.04
        p38.articles = 'http://adsabs.harvard.edu/abs/2009MNRAS.397.2123C;http://adsabs.harvard.edu/abs/2006MNRAS.367.1201C'
        p38.x_ray_info = 'PL fit from Becker, binary star -> variable flux [last update: 2012-03-30]'
        p38.cite = '\citet{2009_Chernyakova}, \citet{2006_Chernyakova}'
        p38.spectrum = 'PL'
        p38.x_ray = True
        p38.comment = 'Be-star bin'
        self.calculations(p38)
        p38.save()
        self.psrs.append(p38)

        p39 = Pulsar.objects.get(name='J1420-6048')
        p39.dist_bb = 8
        p39.l_nonth, p39.l_nonth_plus, p39.l_nonth_minus = \
            self.lnonth_powers([[34.41,0.22,0.45],[34.52,0.22,0.45]])
        p39.pl = 1.6
        p39.pl_plus = 0.4
        p39.pl_minus = 0.4
        p39.articles = 'http://adsabs.harvard.edu/abs/2001ApJ...561L.187R;http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        p39.x_ray_info = 'PL fit from Becker, some evidence for thermal emission [last update: 2012-03-30]'
        p39.cite = '\citet{2001_Roberts}'
        p39.spectrum = 'PL'
        p39.x_ray = True
        self.calculations(p39)
        p39.save()
        self.psrs.append(p39)

        p40 = Pulsar.objects.get(name='B1800-21')
        #p40.r =
        #p40.r_plus =
        #p40.r_minus =
        p40.t = self.ev_to_k(0.2e3)
        p40.t_plus = self.ev_to_k(0.1e3)
        p40.t_minus = self.ev_to_k(0.1e3)
        p40.dist_bb = 4.
        #p40.l_bol = self.lbol_radius(p.t, p.r)
        #p40.l_bol_sphere = 4. * self.lbol_radius(p.t, p.r)
        # from Becker (much stronger)
        #p40.l_nonth, p40.l_nonth_plus, p40.l_nonth_minus = \
        #    self.lnonth_powers([[32.35,0.49,0.8],[32.64,0.26,0.53]])
        p40.l_nonth = 4e31 # from paper PL+BB
        p40.pl = 1.4
        p40.pl_plus = 0.6
        p40.pl_minus = 0.6
        p40.articles = 'http://adsabs.harvard.edu/abs/2007ApJ...660.1413K'
        p40.x_ray_info = 'page 1, no R_BB (strong interstellar absorption) [last update: 2012-03-30]'
        p40.cite = '\citet{2007_Kargaltsev}'
        p40.spectrum = 'PL + BB'
        p40.x_ray = True
        p40.comment = 'Vela-like pulsar'#'G8.7-0.1'
        self.calculations(p40)
        p40.save()
        self.psrs.append(p40)

        p41 = Pulsar.objects.get(name='B1757-24')
        p41.dist_bb = 5
        p41.l_nonth, p41.l_nonth_plus, p41.l_nonth_minus = \
            self.lnonth_powers([[33.1,0.54,0.53],[33.21,0.26,0.53]])
        #p41.l_nonth = 6.9e-13 * 4. * pi * (p41.dist_bb * 1e3 * 3.0857e18) ** 2.  # flux recalculation
        p41.pl = 1.6
        p41.pl_plus = 0.6
        p41.pl_minus = 0.5
        p41.articles = 'http://adsabs.harvard.edu/abs/2001ApJ...562L.163K;http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        p41.x_ray_info = 'page 9, thermal fit T=1e8 [last update: 2012-03-30]'
        p41.cite = '\citet{2001_Kaspi}'
        p41.spectrum = 'PL'
        p41.x_ray = True
        p41.comment = 'Duck'
        self.calculations(p41)
        p41.save()
        self.psrs.append(p41)

        p42 = Pulsar.objects.get(name='B0540-69')
        p42.dist_bb = 55.
        p42.l_nonth, p42.l_nonth_plus, p42.l_nonth_minus = \
            self.lnonth_powers([[36.68,0.19,0.32],[36.49,0.21,0.37]])
        #p42.l_nonth = 1.2e-11 * 4. * pi * (p42.dist_bb * 1e3 * 3.0857e18) ** 2.  # flux recalculation
        p42.pl = 1.92
        p42.pl_plus = 0.11
        p42.pl_minus = 0.11
        p42.articles = 'http://adsabs.harvard.edu/abs/2001ApJ...546.1159K;http://adsabs.harvard.edu/abs/2008MNRAS.389..691C'
        p42.x_ray_info = 'page 7, [last update: 2012-03-30]'
        p42.cite = '\citet{2001_Kaaret}, \citet{2008_Campana}'
        p42.spectrum = 'PL'
        p42.comment = 'N158A, LMC'
        p42.x_ray = True
        self.calculations(p42)
        p42.save()
        self.psrs.append(p42)

        p43 = Pulsar.objects.get(name='J1105-6107')
        p43.dist_bb = 7
        p43.l_nonth, p43.l_nonth_plus, p43.l_nonth_minus = \
            self.lnonth_powers([[33.65,0.39,0.50],[33.57,0.18,0.31]])
        #p43.l_nonth = 6.4e-13 * 4. * pi * (p43.dist_bb * 1e3 * 3.0857e18) ** 2.  # flux recalculation
        p43.pl = 1.8
        p43.pl_plus = 0.4
        p43.pl_minus = 0.4
        p43.articles = 'http://adsabs.harvard.edu/abs/1998ApJ...497L..29G;http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        p43.x_ray_info = 'page 1, L from Becker [last update: 2012-03-30]'
        p43.cite = '\citet{1998_Gotthelf}'
        p43.spectrum = 'PL'
        p43.x_ray = True
        self.calculations(p43)
        p43.save()
        self.psrs.append(p43)

        p44 = Pulsar.objects.get(name='B1853+01')
        p44.dist_bb = 2.6
        p44.l_nonth, p44.l_nonth_plus, p44.l_nonth_minus = \
            self.lnonth_powers([[31.53,0.44,0.54],[31.92,0.19,0.34]])
        #p44.l_nonth = 6e32
        p44.pl = 1.28
        p44.pl_plus = 0.48
        p44.pl_minus = 0.48
        p44.articles = 'http://adsabs.harvard.edu/abs/2002ApJ...579..404P;http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        p44.x_ray_info = 'page 6, L from Becker [last update: 2012-03-30]'
        p44.cite = '\citet{2002_Petre}'
        p44.spectrum = 'PL'
        p44.x_ray = True
        p44.comment = 'W44'
        self.calculations(p44)
        p44.save()
        self.psrs.append(p44)

        p45 = Pulsar.objects.get(name='J1509-5850')
        p45.dist_bb = 2.56
        p45.l_nonth, p45.l_nonth_plus, p45.l_nonth_minus = \
            self.lnonth_powers([[31.43,0.2,0.4],[31.55,0.35,0.54]])
        #p45.l_nonth = 5.9e-14 * 4. * pi * (p43.dist_bb * 1e3 * 3.0857e18) ** 2.  # flux recalculation
        p45.dist_dm_cl = 2.56
        p45.pl = 1
        p45.pl_plus = 0.2
        p45.pl_minus = 0.3
        p45.articles = 'http://adsabs.harvard.edu/abs/2007A%26A...470..965H;http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        p45.x_ray_info = 'page 2, L from Becker BB fit t=1e7, r=10m [last update: 2012-03-30]'
        p45.cite = '\citet{2007_Hui}'
        p45.spectrum = 'PL'
        p45.x_ray = True
        p45.comment = 'MSH 15-52'
        self.calculations(p45)
        p45.save()
        self.psrs.append(p45)

        p46 = Pulsar.objects.get(name='J2021+3651')
        p46.r = 7.0e5  # should be inf?
        p46.r_plus = 4e5
        p46.r_minus = 1.7e5
        #p46.t = self.ev_to_k(0.19e3)
        #p46.t_plus = self.ev_to_k(0.03e3)
        #p46.t_minus = self.ev_to_k(0.03e3)
        p46.t_inf = self.ev_to_k(0.16e3)
        p46.t_inf_plus = self.ev_to_k(0.02e3)
        p46.t_inf_minus = self.ev_to_k(0.02e3)
        p46.t = p46.t_inf / self.gr
        p46.t_plus = p46.t_inf_plus / self.gr
        p46.t_minus = p46.t_inf_minus / self.gr
        p46.l_bol = self.lbol_radius(p46.t, p46.r)
        p46.l_bol_sphere = 4. * self.lbol_radius(p46.t, p46.r)
        p46.dist_bb = 10.
        p46.l_nonth, p46.l_nonth_plus, p46.l_nonth_minus = \
            self.lnonth_powers([[34.13,0.23,0.56],[33.97,0.18,0.33]])
        p46.pl = 1.7
        p46.pl_plus = 0.3
        p46.pl_minus = 0.2
        p46.best_dist_plus = 10.
        p46.best_dist_minus = 8.
        p46.articles = 'http://adsabs.harvard.edu/abs/2008ApJ...680.1417V;http://adsabs.harvard.edu/abs/2004ApJ...612..389H;http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        p46.other_articles = 'http://adsabs.harvard.edu/abs/2009ApJ...700.1059A;http://adsabs.harvard.edu/abs/2008ApJ...680.1417V'
        p46.x_ray_info = 'page 10, page 9 (in second paper)  remove from B/T plot, The distance to PSR J2021+3651 is intriguing , L from Becker BB [last update: 2012-03-30]'
        p46.cite = '\citet{2008_VanEtten},\citet{2004_Hessels}'
        p46.spectrum = 'PL, BB'
        p46.x_ray = True
        self.calculations(p46)
        p46.save()
        self.psrs.append(p46)

        p47 = Pulsar.objects.get(name='B1610-50')
        p47.dist_bb = 7.3
        p47.articles = 'http://adsabs.harvard.edu/abs/2000ApJ...528..436P;http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        p47.x_ray_info = 'X-ray emission from PSR B1610−50 is not detected ?? upper limits in Becker [last update: 2012-03-30]'
        p47.cite = '\citet{}'
        p47.spectrum = 'NO'
        p47.x_ray = False
        self.calculations(p47)
        p47.save()
        self.psrs.append(p47)

        p48 = Pulsar.objects.get(name='J1846-0258')
        p48.r_inf = 0.4e5
        p48.r_inf_plus = 0.2e5
        p48.r_inf_minus = 0.2e5
        p48.t_inf = self.ev_to_k(0.9e3)
        p48.t_inf_plus = self.ev_to_k(0.2e3)
        p48.t_inf_minus = self.ev_to_k(0.2e3)
        p48.r = p48.r_inf * self.gr
        p48.r_plus = p48.r_inf_plus * self.gr
        p48.r_minus = p48.r_inf_minus * self.gr
        p48.t = p48.t_inf / self.gr
        p48.t_plus = p48.t_inf_plus / self.gr
        p48.t_minus = p48.t_inf_minus / self.gr
        p48.dist_bb = 6.
        p48.l_bol = self.lbol_radius(p48.t, p48.r)
        p48.l_bol_sphere = 4. * self.lbol_radius(p48.t, p48.r)
        p48.l_nonth = 3.1e-11 * 4. * pi * (p48.dist_bb * 1e3 * 3.0857e18) ** 2.  # flux recalculation
        p48.l_nonth_plus = 0.6e-11 * 4. * pi * (p48.dist_bb * 1e3 * 3.0857e18) ** 2.  # flux recalculation
        p48.l_nonth_minus = 0.6e-11 * 4. * pi * (p48.dist_bb * 1e3 * 3.0857e18) ** 2.  # flux recalculation
        p48.pl = 1.9
        p48.pl_plus = 0.1
        p48.pl_minus = 0.1
        p48.articles = 'http://adsabs.harvard.edu/abs/2008ApJ...686..508N;http://adsabs.harvard.edu/abs/2003ApJ...582..783H'
        p48.x_ray_info = 'page 14 [last update: 2012-03-30]'
        p48.cite = '\citet{2008_Ng}, \citet{2003_Helfand}'
        p48.spectrum = 'BB + PL'
        p48.x_ray = True
        p48.comment = 'Kes 75'
        self.calculations(p48)
        p48.save()
        self.psrs.append(p48)

        p49 = Pulsar.objects.get(name='B1719-37')
        p49.r_inf = 0.31e5
        p49.r_inf_plus = 0.51e5
        p49.r_inf_minus = 0.16e5
        p49.t_inf = 2.7e6 # self.ev_to_k(0.23e3)
        p49.t_inf_plus = 0.7e6 # self.ev_to_k(0.06e3)
        p49.t_inf_minus = 0.58e6 # self.ev_to_k(0.05e3)
        p49.r = p49.r_inf * self.gr
        p49.r_plus = p49.r_inf_plus * self.gr
        p49.r_minus = p49.r_inf_minus * self.gr
        p49.t = p49.t_inf / self.gr
        p49.t_plus = p49.t_inf_plus / self.gr
        p49.t_minus = p49.t_inf_minus / self.gr
        p49.dist_bb = 1.84
        p49.dist_dm_cl = 1.835
        p49.dist_dm_cl_plus = 1.835 - 1.564
        p49.dist_dm_cl_minus = 2.132 - 1.835
        p49.l_bol = self.lbol_radius(p49.t, p49.r)
        p49.l_bol_sphere = 4. * self.lbol_radius(p49.t, p49.r)
        p49.articles = 'http://adsabs.harvard.edu/abs/2004NuPhS.132..636O;http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        p49.x_ray_info = 'page 3 (638), same fit in Beckers paper [last update: 2012-03-30]'
        p49.cite = '\citet{2004_Oosterbroek}'
        p49.spectrum = 'BB'
        p49.x_ray = True
        self.calculations(p49)
        p49.save()
        self.psrs.append(p49)

        p50 = Pulsar.objects.get(name='J0631+1036')
        p50.dist_bb = 6.56
        p50.articles = 'http://adsabs.harvard.edu/abs/2002astro.ph..2055K;http://adsabs.harvard.edu/abs/2001ApJ...551L.151T'
        p50.x_ray_info = 'no X-ray radiation (different source in first paper) [last update: 2012-03-30]'
        p50.cite = '\citet{}'
        p50.spectrum = 'NO'
        p50.x_ray = False
        self.calculations(p50)
        p50.save()
        self.psrs.append(p50)

        p51 = Pulsar.objects.get(name='B0823+26')
        p51.dist_bb = 0.34
        p51.l_nonth, p51.l_nonth_plus, p51.l_nonth_minus = \
            self.lnonth_powers([[29.36,0.69,0.56],[28.56,0.26,0.73]])
        p51.pl = 1.58
        p51.pl_plus = 0.43
        p51.pl_minus = 0.33
        p51.articles = 'http://adsabs.harvard.edu/abs/2004ApJ...615..908B;http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        p51.x_ray_info = 'values from later paper, upper limits for BB in paper [last update: 2012-03-30]'
        p51.cite = '\citet{2004_Becker}'
        p51.spectrum = 'PL'
        p51.x_ray = True
        self.calculations(p51)
        p51.save()
        self.psrs.append(p51)

        p52 = Pulsar.objects.get(name='B2224+65')
        p52.r = 1.41e3 * 2.
        p52.r_plus = 2.8e2 * 2.#2.8e2
        p52.r_minus = 1.8e+03 #R_bb (err -) from dist err. and temp #2.3e2
        p52.t = self.ev_to_k(0.5e3)
        p52.t_plus = self.ev_to_k(0.1e3)
        p52.t_minus = self.ev_to_k(0.1e3)
        p52.dist_bb = 2.
        p52.dist_dm_cl = 2.
        p52.dist_dm_cl_plus = 1.
        p52.dist_dm_cl_minus = 1.
        p52.l_bol = self.lbol_radius(p52.t, p52.r)
        p52.l_bol_sphere = 4. * self.lbol_radius(p52.t, p52.r)
        p52.l_nonth = 3.4e-14 * 4. * pi * (p52.dist_bb * 1e3 * 3.0857e18) ** 2.  # flux recalculation
        p52.l_nonth_plus = 1.7e-14 * 4. * pi * (p52.dist_bb * 1e3 * 3.0857e18) ** 2.  # flux recalculation
        p52.l_nonth_minus = 1e-14 * 4. * pi * (p52.dist_bb * 1e3 * 3.0857e18) ** 2.  # flux recalculation
        p52.pl = 2.2
        p52.pl_plus = 0.2
        p52.pl_minus = 0.3
        p52.articles = 'http://adsabs.harvard.edu/abs/2012ApJ...747...74H;http://adsabs.harvard.edu/abs/2007A%26A...467.1209H'
        p52.x_ray_info = 'page 4 (BB), page 19 (PL) [last update: 2012-03-30]'
        p52.cite = '\citet{2012_Hui}, \citet{2007_Hui_b}'
        p52.spectrum = 'PL, BB'
        p52.x_ray = True
        p52.comment = 'Guitar'
        self.calculations(p52)
        p52.save()
        self.psrs.append(p52)

        p53 = Pulsar.objects.get(name='B1451-68')
        p53.alpha = 37
        p53.beta = -6.
        p53.rho = 10.9
        p53.r = 13.8e2
        p53.r_plus = 24.2e2
        p53.r_minus = 12.3e2
        p53.t = self.ev_to_k(0.35e3)
        p53.t_plus = self.ev_to_k(0.12e3)
        p53.t_minus = self.ev_to_k(0.07e3)
        p53.dist_bb = 0.48
        p53.dist_pi = 0.48
        p53.dist_pi_plus = 0.08
        p53.dist_pi_minus = 0.06
        p53.dist_dm_cl = 0.459
        p53.dist_dm_cl_plus = 0.403 - 0.459
        p53.dist_dm_cl_minus = 0.459 - 0.415
        p53.l_bol = self.lbol_radius(p53.t, p53.r)
        p53.l_bol_sphere = 4. * self.lbol_radius(p53.t, p53.r)
        p53.l_nonth = 5.9e29
        p53.l_nonth_plus = 4.9e29
        p53.l_nonth_minus = 5e29
        p53.pl = 1.4
        p53.pl_plus = 0.5
        p53.pl_minus = 0.5
        p53.articles = 'http://adsabs.harvard.edu/abs/2012ApJ...749..146P'
        p53.other_articles = 'http://adsabs.harvard.edu/abs/1993ApJS...85..145R'
        p53.x_ray_info = 'page 6 [last update: 2012-06-12]'
        p53.cite = '\citet{2012_Posselt}'
        p53.spectrum = 'BB + PL'
        p53.x_ray = True
        p53.comment = ''
        self.calculations(p53)
        p53.save()
        self.psrs.append(p53)

        # millisecond pulsar
        p54 = Pulsar.objects.get(name='J0437-4715')
        p54.alpha = 36.
        #p54.beta = -6.
        #p54.rho = 10.9
        p54.r = 0.07e5
        p54.r_plus = 0.02e5
        p54.r_minus = 0.02e5
        p54.t = 2.9e6
        p54.t_plus = 0.05e6
        p54.t_minus = 0.06e6
        p54.l_bol = self.lbol_radius(p54.t, p54.r)
        p54.l_bol_sphere = 4. * self.lbol_radius(p54.t, p54.r)
        p54.r2 = 0.39e5
        p54.r2_plus = 0.17e5
        p54.r2_minus = 0.14e5
        p54.t2 = 1.23e6
        p54.t2_plus = 0.05e6
        p54.t2_minus = 0.06e6
        p54.l_bol2 = 2. *  self.lbol_radius(p54.t2, p54.r2)
        p54.l_bol_sphere2 = 4. * self.lbol_radius(p54.t2, p54.r2)
        p54.dist_bb = 0.1563
        p54.dist_pi = 0.1563
        p54.dist_pi_plus = 0.0013
        p54.dist_pi_minus = 0.0013
        #p54.dist_dm_cl =
        #p54.dist_dm_cl_plus =
        #p54.dist_dm_cl_minus =
        #p54.l_nonth = 5.9e29
        #p54.l_nonth_plus = 4.9e29
        #p54.l_nonth_minus = 5e29
        p54.pl = -0.11
        p54.pl_plus = 1.67
        p54.pl_minus = 1.74
        p54.articles = 'http://adsabs.harvard.edu/abs/2013ApJ...762...96B'
        p54.other_articles = ''
        p54.x_ray_info = 'page 6 [last update: 2013-01-08]'
        p54.cite = '\citet{2013_Bogdanov}'
        p54.spectrum = 'BB + PL'
        p54.x_ray = True
        p54.comment = 'many other fits in paper'
        self.calculations(p54)
        p54.save()
        self.psrs.append(p54)

        p55 = Pulsar.objects.get(name='J2021+4026')
        p55.r = 223e2
        p55.r_plus = 320e2
        p55.r_minus = 106e2
        p55.t = self.ev_to_k(0.25e3)
        p55.t_plus = self.ev_to_k(0.05e3)
        p55.t_minus = self.ev_to_k(0.05e3)
        p55.r2 = 3.6e2
        p55.r2_plus = 6.4e2
        p55.r2_minus = 2.5e2
        p55.t2 = self.ev_to_k(1.4e3)
        p55.t2_plus = self.ev_to_k(1.8e3)
        p55.t2_minus = self.ev_to_k(0.6e3)
        p55.pl = 1.2
        p55.pl_plus = 1.7
        p55.pl_minus = 1.2
        p55.articles = 'http://arxiv.org/abs/1305.0998'
        p55.other_articles = ''
        p55.x_ray_info = 'BB+BB (sec BB is incorrect?), BB+PL [last update: 2013-06-08]'
        p55.cite = '\citet{2013_Lin}'
        p55.spectrum = 'BB + BB'
        p55.x_ray = True
        p55.comment = ''
        self.calculations(p55)
        p55.save()
        self.psrs.append(p55)

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

