#! /usr/bin/env python
from sys import path
import os

# pretend to run from project main dir
path[0] = "/".join(os.path.abspath(__file__).split("/")[:-2])
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pulsars.settings")
from django.core.exceptions import ObjectDoesNotExist
from database.models import Pulsar, GammaRayFermi


class GammaData:

    def __init__(self):
        pass

    def add_pulsars(self):
        self.add_record('J0007+7303', 94, 1, 1, 40, 40)
        self.add_record('J0106+4855', 21, 2, 2, 20, 8)
        self.add_record('J0205+6449', 24, 1, 1, 1, 1)
        self.add_record('J0248+6021', 25, 2, 2, 5, 5)
        #self.add_record('J0357+3205', , , , , )
        self.add_record('J0534+2200', 619, 4, 4, 300, 300)
        #self.add_record('J0622+3749', , , , ,)
        self.add_record('J0631+1036', 5.6, 0.3, 0.3, 3, 2)
        #self.add_record('J0633+0632', , , , , )
        self.add_record('J0633+1746', 31.7, 0.1, 0.1, 90, 20)
        self.add_record('J0659+1414', 0.24, 0.02, 0.02, 0.05, 0.05)
        #self.add_record('J0729-1448', , , , , )
        #self.add_record('J0734-1559', , , , , )
        self.add_record('J0742-2822', 9, 1, 1, 4, 4)
        self.add_record('J0835-4510', 89.3, 0.2, 0.2, 10, 10)
        self.add_record('J0908-4913', 35, 3, 3, 30, 20)
        #self.add_record('J0940-5428', , , , , )
        self.add_record('J1016-5857', 55, 9, 9, 30, 50)
        #self.add_record('J1019-5749', , , , , )
        #self.add_record('J1023-5746', , , , , )
        self.add_record('J1028-5819', 158, 5, 5, 40, 40)
        #self.add_record('J1044-5737', , , , , )
        self.add_record('J1048-5832', 176, 5, 5, 40, 40)
        self.add_record('J1057-5226', 4.3, 0.1, 0.1, 5, 3)
        self.add_record('J1105-6107', 150, 20, 20, 50, 50)
        self.add_record('J1112-6103', 360, 90, 90, 600, 200)
        self.add_record('J1119-6127', 600, 40, 40, 60, 60)
        self.add_record('J1124-5916', 170, 10, 10, 50, 70)
        #self.add_record('J1135-6055', , , , , )
        self.add_record('J1357-6429', 25, 2, 2, 10, 8)
        self.add_record('J1410-6132', 800, 300, 300, 900, 400)
        #self.add_record('J1413-6206', , , , , )
        self.add_record('J1418-6058', 92, 4, 4, 100, 60)

        self.add_record('J1420-6048', 640, 50, 50, 200, 200)
        #self.add_record('J1429-5911', , , , , )
        #self.add_record('J1459-6053', , , , , )
        self.add_record('J1509-5850', 105, 6, 6, 40, 40)
        self.add_record('J1513-5908', 70, 10, 10, 20, 20)
        self.add_record('J1531-5610', 1.0, 0.6, 0.6, 0.4, 0.4)
        #self.add_record('J1620-4927', , , , , )
        self.add_record('J1648-4611', 160, 20, 20, 40, 40)
        self.add_record('J1702-4128', 80, 70, 70, 20, 20)
        self.add_record('J1709-4429', 853, 6, 6, 200, 200)
        self.add_record('J1718-3825', 138, 8, 8, 30, 30)
        self.add_record('J1730-3350', 36, 6, 6, 9, 9)
        self.add_record('J1732-3131', 8.6, 0.3, 0.3, 2, 2)
        self.add_record('J1741-2054', 2.1, 0.1, 0.1, 0.2, 0.2)
        #self.add_record('J1746-3239', , , , , )
        self.add_record('J1747-2958', 570, 30, 30, 200, 200)
        self.add_record('J1801-2451', 40, 10, 10, 9, 7)
        #self.add_record('J1803-2149', , , , , )
        self.add_record('J1809-2332', 164, 3, 3, 200, 100)
        #self.add_record('J1813-1246', , , , , )
        #self.add_record('J1826-1256', , , , , )
        self.add_record('J1833-1034', 160, 10, 10, 30, 20)
        self.add_record('J1835-1106', 6, 2, 2, 2, 2)
        self.add_record('J1836+5925', 20.4, 0.1, 0.1, 30, 20)
        #self.add_record('J1838-0537', , , , , )
        #self.add_record('J1846+0919', , , , , )
        self.add_record('J1907+0602', 314, 8, 8, 60, 60)
        self.add_record('J1952+3252', 66, 2, 2, 40, 30)
        #self.add_record('J1954+2836', , , , , )
        #self.add_record('J1957+5033', , , , , )
        #self.add_record('J1958+2846', , , , , )
        self.add_record('J2021+3651', 5910, 90, 90, 3000, 4000)
        self.add_record('J2021+4026', 257, 2, 2, 200, 100)

        #self.add_record('J2028+3332', , , , , )
        self.add_record('J2030+3641', 34, 4, 4, 30, 20)
        #self.add_record('J2030+4415', , , , , )
        self.add_record('J2032+4127', 169, 10, 10, 50, 50)
        self.add_record('J2043+2740', 3.8, 0.6, 0.6, 1, 1)
        #self.add_record('J2055+2539', , , , , )
        #self.add_record('J2111+4606', , , , , )
        #self.add_record('J2139+4716', , , , , )
        self.add_record('J2229+6114', 19.4, 0.3, 0.3, 8, 8)
        #self.add_record('J2238+5903', , , , , )
        self.add_record('J2240+5832', 80, 20, 20, 10, 10)

        # millisecond pulsars
        self.add_record('J0023+0923', 4.6, 0.7, 0.7, 3, 1, mod_=1e32)
        self.add_record('J0030+0451', 5.8, 0.2, 0.2, 5, 2, mod_=1e32)
        self.add_record('J0034-0534', 5.7, 0.4, 0.4, 3, 2, mod_=1e32)
        self.add_record('J0101-6422', 3.8, 0.3, 0.3, 1, 1, mod_=1e32)
        self.add_record('J0102+4839', 90, 10, 10, 40, 30, mod_=1e32)
        self.add_record('J0218+4232', 380, 20, 20, 400, 200, mod_=1e32)
        self.add_record('J0340+4130', 73, 6, 6, 10, 10, mod_=1e32)
        self.add_record('J0437-4715', 0.49, 0.03, 0.03, 0.01, 0.01, mod_=1e32)
        self.add_record('J0610-2100', 100, 20, 20, 500, 50, mod_=1e32)
        self.add_record('J0613-0200', 29, 2, 2, 30, 10, mod_=1e32)
        self.add_record('J0614-3329', 470, 10, 10, 200, 200, mod_=1e32)
        self.add_record('J0751+1807', 2.5, 0.2, 0.2, 3, 1, mod_=1e32)
        self.add_record('J1024-0719', 0.6, 0.2, 0.2, 0.1, 0.1, mod_=1e32)
        self.add_record('J1124-3653', 43, 5, 5, 20, 20, mod_=1e32)
        self.add_record('J1125-5825', 70, 20, 20, 20, 20, mod_=1e32)
        self.add_record('J1231-1411', 24, 0.6, 0.6, 5, 5, mod_=1e32)
        self.add_record('J1446-4701', 19, 4, 4, 5, 5, mod_=1e32)
        self.add_record('J1514-4946', 48, 3, 3, 10, 10, mod_=1e32)
        self.add_record('J1600-3053', 17, 9, 9, 7, 5, mod_=1e32)
        self.add_record('J1614-2230', 12, 1, 1, 2, 2, mod_=1e32)
        self.add_record('J1658-5324', 30, 2, 2, 8, 8, mod_=1e32)
        self.add_record('J1713+0747', 13, 2, 2, 2, 1, mod_=1e32)
        self.add_record('J1741+1351', 3, 1, 1, 0.3, 0.3, mod_=1e32)
        self.add_record('J1744-1134', 6.8, 0.5, 0.5, 0.5, 0.5, mod_=1e32)
        self.add_record('J1747-4036', 140, 30, 30, 70, 50, mod_=1e32)
        self.add_record('J1810+1744', 112, 8, 8, 40, 30, mod_=1e32)
        self.add_record('J1823-3021A', 700, 100, 100, 80, 80, mod_=1e32)
        self.add_record('J1858-2216', 8, 2, 2, 4, 2, mod_=1e32)
        self.add_record('J1902-5105', 36, 2, 2, 10, 10, mod_=1e32)
        self.add_record('J1939+2134', 140, 50, 50, 30, 30, mod_=1e32)
        self.add_record('J1959+2048', 130, 10, 10, 20, 40, mod_=1e32)
        self.add_record('J2017+0603', 98, 6, 6, 20, 20, mod_=1e32)
        self.add_record('J2043+1711', 100, 6, 6, 20, 30, mod_=1e32)

        self.add_record('J2047+1053', 31, 7, 7, 10, 8, mod_=1e32)
        self.add_record('J2051-0827', 4, 1, 1, 1, 1, mod_=1e32)
        self.add_record('J2124-3358', 4, 0.2, 0.2, 2, 1, mod_=1e32)
        self.add_record('J2214+3000', 93, 4, 4, 20, 20, mod_=1e32)
        self.add_record('J2215+5135', 130, 20, 20, 30, 30, mod_=1e32)
        self.add_record('J2241-5236', 10.5, 0.5, 0.5, 3, 3, mod_=1e32)
        self.add_record('J2302+4442', 62, 3, 3, 10, 20, mod_=1e32)

        #self.add_record('', , , , , , mod_=1e32)


    def gamma_get_add(self, p,  num):
        try:
            g = p.gammarays.get(num=num)
        except ObjectDoesNotExist:
            g = GammaRayFermi(num=num)
        g.psr_id = p
        g.save()
        p.gammarays.add(g)
        return g

    def add_record(self, name, lum, lum_plus, lum_minus, lum_plus_dist, lum_minus_dist, mod_=1e33):
        """luminosities in 10^{33} erg/s
        """
        try:
            p = Pulsar.objects.get(name=name)
        except ObjectDoesNotExist:
            p = Pulsar.objects.get(jname=name)
        ga = self.gamma_get_add(p, 0)
        ga.lum = float(lum) * mod_
        ga.lum_plus = float(lum_plus) * mod_
        ga.lum_minus = float(lum_minus) * mod_
        ga.lum_plus_dist = float(lum_plus_dist) * mod_
        ga.lum_minus_dist = float(lum_minus_dist) * mod_
        ga.save()

    def remove_all(self):
        ga = GammaRayFermi.objects.all()
        for g in ga:
            g.delete()


def main():
    g = GammaData()
    #g.remove_all()
    g.add_pulsars()
    print 'Bye'


if __name__ == '__main__':
    main()
