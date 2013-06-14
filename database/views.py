# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.core.exceptions import ObjectDoesNotExist

from models import Pulsar, XrayArticle, XrayFit, XrayComponent, Geometry, \
    Subpulse, Additional, Calculation, GammaRayFermi
from atnf import get_page, parse_page, parse_malov
import latex
import plot


def index(request):
    """ show x-ray pulsars by default
    """
    return x_ray(request)


def pulsars(request, id=None):
    """ show all pulsars
    """
    if id != None:
        psr = Pulsar.objects.get(id=id)
        ads = psr.additionals.all()
        cas = psr.calculations.all()
        sus = psr.subpulses.all()
        ges = psr.geometries.all()
        template = loader.get_template('database/component.xhtml')
        c = Context({'psr':psr, 'cas':cas, 'ads':ads, 'sus':sus, 'ges':ges}, )
        return HttpResponse(template.render(c))
    else:
        psrs = Pulsar.objects.all().order_by('name')
        template = loader.get_template('database/all.xhtml')
        c = Context({'psrs':psrs,})
        return HttpResponse(template.render(c))


def x_ray(request):
    """ show pulsars with X-ray data
    """
    psrs = Pulsar.objects.filter(xray_articles__num__gte=0).distinct()
    template = loader.get_template('database/x-rays.xhtml')
    c = Context({'psrs':psrs})
    return HttpResponse(template.render(c))


def gamma_ray(request):
    """ show pulsars with X-ray data
    """
    psrs = Pulsar.objects.filter(gammarays__num__gte=0).distinct().order_by('name')
    template = loader.get_template('database/all.xhtml')
    c = Context({'psrs':psrs})
    return HttpResponse(template.render(c))



def get_atnf(request):
    if False:
        get_page()
        return HttpResponse('ATNF data downloaded successfully..')
    else:
        return HttpResponse('ATNF download disabled! (check views.py)')


def sync_atnf(request):
    if False:
        parse_page()
        return HttpResponse('ATNF data sync successfully..')
    else:
        return HttpResponse('ATNF sync disabled (check sync_atnf in database/views.py)..')

def sync_malov(request):
    if False:
        parse_malov()
        return HttpResponse('Malov 2007 data sync successfully..')
    else:
        return HttpResponse('Malov 2007 data sync disabled (check sync_malov in database/views.py)..')


def table_bb(request):
    # for citealiases
    #all_psrs = Pulsar.objects.all()
    #print_latex.citealiases(all_psrs)
    # data for table
    psrs = Pulsar.objects.exclude(calculations__b__isnull=True).exclude(p0__lt=0.01).order_by('-calculations__b').distinct()
    res = latex.table_bb(psrs)
    return HttpResponse(res, mimetype="text/plain")


def table_psrs(request):
    psrs = Pulsar.objects.filter(xray_articles__fits__ordinal__gt=0).filter(p0__gt=0.01).order_by('rajd').distinct()
    res = latex.table_psrs(psrs)
    return HttpResponse(res, mimetype="text/plain")


def table_pl(request):
    # sort does not work (multiple lum values for different components)
    #psrs = Pulsar.objects.filter(xray_articles__fits__ordinal__gt=0).filter(xray_articles__fits__components__spec_type='PL').distinct().order_by('xray_articles__fits__components__lum')
    comps = XrayComponent.objects.filter(spec_type='PL').filter(xrayfit__ordinal__gt=0).filter(psr_id__p0__gt=0.01).distinct().order_by('-lum')
    # data for table
    psrs = []
    for co in comps:
        print co, co.psr_id
        psrs.append(co.psr_id)
    res = latex.table_pl(psrs)
    return HttpResponse(res, mimetype="text/plain")


def bb_pl(request):
    fits = XrayFit.objects.filter(ordinal__gt=0).filter(components__spec_type='PL').filter(components__spec_type='BB').filter(psr_id__p0__gt=0.01).distinct()
    list_ = plot.bb_pl(fits)
    template = loader.get_template('database/plots/image.xhtml')
    c = Context({'list_':list_, })
    return HttpResponse(template.render(c))

def xi_age(request):
    fits = XrayFit.objects.filter(ordinal__gt=0).filter(psr_id__p0__gt=0.01).distinct()
    list_ = plot.xi_age(fits)
    template = loader.get_template('database/plots/image.xhtml')
    c = Context({'list_':list_, })
    return HttpResponse(template.render(c))

def xi_field(request):
    fits = XrayFit.objects.filter(ordinal__gt=0).filter(psr_id__p0__gt=0.01).distinct()
    list_ = plot.xi_field(fits)
    template = loader.get_template('database/plots/image.xhtml')
    c = Context({'list_':list_, })
    return HttpResponse(template.render(c))


def xi_sd(request):
    fits = XrayFit.objects.filter(ordinal__gt=0).filter(psr_id__p0__gt=0.01).distinct()
    list_ = plot.xi_sd(fits)
    template = loader.get_template('database/plots/image.xhtml')
    c = Context({'list_':list_, })
    return HttpResponse(template.render(c))


def pl_sd(request):
    fits = XrayFit.objects.filter(ordinal__gt=0).filter(components__spec_type='PL').filter(psr_id__p0__gt=0.01).distinct()
    list_ = plot.pl_sd(fits)
    template = loader.get_template('database/plots/image.xhtml')
    c = Context({'list_':list_, })
    return HttpResponse(template.render(c))

def radio(request):
    psrs = Pulsar.objects.all()
    list_ = plot.radio_plots(psrs)
    template = loader.get_template('database/plots/image.xhtml')
    c = Context({'list_':list_, })
    return HttpResponse(template.render(c))

def b_parameter(request):
    comps = XrayComponent.objects.filter(spec_type='BB').filter(xrayfit__ordinal__gt=0).filter(psr_id__calculations__b__gt=1).filter(psr_id__p0__gt=0.01).distinct()
    list_ = plot.b_parameter(comps)
    template = loader.get_template('database/plots/image.xhtml')
    c = Context({'list_':list_, })
    return HttpResponse(template.render(c))

def b_age(request):
    comps = XrayComponent.objects.filter(spec_type='BB').filter(xrayfit__ordinal__gt=0).filter(psr_id__calculations__b__gt=1).filter(psr_id__p0__gt=0.01).distinct()
    list_ = plot.b_age(comps)
    template = loader.get_template('database/plots/image.xhtml')
    c = Context({'list_':list_, })
    return HttpResponse(template.render(c))


def t6_b14(request):
    comps = XrayComponent.objects.filter(spec_type='BB').filter(xrayfit__ordinal__gt=0).filter(psr_id__calculations__b__gt=1).filter(psr_id__p0__gt=0.01).distinct()
    list_ = plot.t6_b14(comps)
    template = loader.get_template('database/plots/image.xhtml')
    c = Context({'list_':list_, })
    return HttpResponse(template.render(c))


def custom(request):
    psrs = Pulsar.objects.all()
    list_ = plot.custom(psrs)
    template = loader.get_template('database/plots/image2.xhtml')
    c = Context({'list_':list_, })
    return HttpResponse(template.render(c))


def custom_data(request):
    psrs = Pulsar.objects.all()
    res = latex.custom(psrs)
    return HttpResponse(res)


def checks_radio(request):
    list_ = []
    list_.append([r'database/plots/custom/2013-5-27T5:29.svg', 'http://www.atnf.csiro.au/people/pulsar/psrcat/proc_form.php?Name=Name&Type=Type&startUserDefined=true&c1=c1&c1_val=S400+%2F+1e3++*+%28Dist+*+3.08567758e21%29+**+2.+*+1e-23+%2F+Edot&c2_val=&c3_val=&c4_val=&sort_attr=jname&sort_order=asc&condition=&pulsar_names=&ephemeris=short&coords_unit=raj%2Fdecj&radius=&coords_1=&coords_2=&style=Long+with+last+digit+error&no_value=*&fsize=3&x_axis=Edot&x_scale=log&y_axis=C1&y_scale=log&state=query&plot_bottom.x=57&plot_bottom.y=16'])
    list_.append([r'database/plots/custom/2013-5-27T5:30.svg', 'http://www.atnf.csiro.au/people/pulsar/psrcat/proc_form.php?Name=Name&Type=Type&startUserDefined=true&c1=c1&c1_val=S1400+%2F+1e3++*+%28Dist+*+3.08567758e21%29+**+2.+*+1e-23+%2F+Edot&c2_val=&c3_val=&c4_val=&sort_attr=jname&sort_order=asc&condition=&pulsar_names=&ephemeris=short&coords_unit=raj%2Fdecj&radius=&coords_1=&coords_2=&style=Long+with+last+digit+error&no_value=*&fsize=3&x_axis=Edot&x_scale=log&y_axis=C1&y_scale=log&state=query&plot_bottom.x=46&plot_bottom.y=21'])
    list_.append([r'database/plots/custom/2013-5-27T5:31.svg', 'http://www.atnf.csiro.au/people/pulsar/psrcat/proc_form.php?Name=Name&Type=Type&startUserDefined=true&c1=c1&c1_val=S2000+%2F+1e3++*+%28Dist+*+3.08567758e21%29+**+2.+*+1e-23+%2F+Edot&c2_val=&c3_val=&c4_val=&sort_attr=jname&sort_order=asc&condition=&pulsar_names=&ephemeris=short&coords_unit=raj%2Fdecj&radius=&coords_1=&coords_2=&style=Long+with+last+digit+error&no_value=*&fsize=3&x_axis=Edot&x_scale=log&y_axis=C1&y_scale=log&state=query&plot_bottom.x=72&plot_bottom.y=32'])
    list_.append([r'database/plots/custom/2013-5-27T5:26.svg', 'http://www.atnf.csiro.au/people/pulsar/psrcat/proc_form.php?Name=Name&Type=Type&startUserDefined=true&c1=c1&c1_val=7.4e27+*+Dist+**+2.+*+S1400+%2F+Edot&c2_val=&c3_val=&c4_val=&sort_attr=jname&sort_order=asc&condition=&pulsar_names=&ephemeris=short&coords_unit=raj%2Fdecj&radius=&coords_1=&coords_2=&style=Long+with+last+digit+error&no_value=*&fsize=3&x_axis=Edot&x_scale=log&y_axis=C1&y_scale=log&state=query&plot_bottom.x=40&plot_bottom.y=35'])
    template = loader.get_template('database/plots/checks.xhtml')
    c = Context({'list_':list_, })
    return HttpResponse(template.render(c))

def xi_sd_radio(request):
    psrs = Pulsar.objects.all()
    list_ = plot.xi_sd_radio(psrs)
    template = loader.get_template('database/plots/image2.xhtml')
    c = Context({'list_':list_, })
    return HttpResponse(template.render(c))


def xi_age_radio(request):
    psrs = Pulsar.objects.filter(binary='*')
    list_ = plot.xi_age_radio(psrs)
    template = loader.get_template('database/plots/image2.xhtml')
    c = Context({'list_':list_, })
    return HttpResponse(template.render(c))


def xi_sd_age_radio(request):
    psrs = Pulsar.objects.all()
    list_ = plot.xi_sd_age_radio(psrs)
    template = loader.get_template('database/plots/image2.xhtml')
    c = Context({'list_':list_, })
    return HttpResponse(template.render(c))


def xi_xray_gamma(request):
    fits = XrayFit.objects.filter(ordinal__gt=0).distinct()
    gamma_data = GammaRayFermi.objects.filter(num=0).order_by('psr_id__name')
    list_ = plot.xi_xray_gamma(fits, gamma_data)
    template = loader.get_template('database/plots/image2.xhtml')
    c = Context({'list_':list_, })
    return HttpResponse(template.render(c))


def l_sd_radio(request):
    psrs = Pulsar.objects.all()
    list_ = plot.l_sd_radio(psrs)
    template = loader.get_template('database/plots/image2.xhtml')
    c = Context({'list_':list_, })
    return HttpResponse(template.render(c))

def ll_sd_radio(request):
    psrs = Pulsar.objects.all()
    list_ = plot.ll_sd_radio(psrs)
    template = loader.get_template('database/plots/image2.xhtml')
    c = Context({'list_':list_, })
    return HttpResponse(template.render(c))

def l_sd_radio_three(request):
    psrs = Pulsar.objects.all()
    list_ = plot.l_sd_radio_three(psrs)
    template = loader.get_template('database/plots/image2.xhtml')
    c = Context({'list_':list_, })
    return HttpResponse(template.render(c))


def flux_sd_radio(request):
    psrs = Pulsar.objects.all()
    list_ = plot.flux_sd_radio(psrs)
    template = loader.get_template('database/plots/image2.xhtml')
    c = Context({'list_':list_, })
    return HttpResponse(template.render(c))


def malov_radio(request):
    psrs = Pulsar.objects.filter(lum_malov__isnull=False)
    list_ = plot.malov_radio(psrs)
    template = loader.get_template('database/plots/image2.xhtml')
    c = Context({'list_':list_, })
    return HttpResponse(template.render(c))

def xray_radio(request):
    psrs = Pulsar.objects.filter(s1400__gt=0)
    list_ = plot.xray_radio(psrs)
    template = loader.get_template('database/plots/image2.xhtml')
    c = Context({'list_':list_, })
    return HttpResponse(template.render(c))

