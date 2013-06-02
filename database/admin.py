from django.contrib import admin
from database.models import Pulsar, XrayArticle, XrayFit, XrayComponent, Additional, Geometry, Subpulse, Calculation

admin.site.register(Pulsar)
admin.site.register(XrayArticle)
admin.site.register(XrayFit)
admin.site.register(XrayComponent)
admin.site.register(Additional)
admin.site.register(Geometry)
admin.site.register(Subpulse)
admin.site.register(Calculation)
