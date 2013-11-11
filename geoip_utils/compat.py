import django

# Django 1.4+ compatibility
if django.VERSION >= (1, 4):
    from django.contrib.gis.geoip import GeoIP
else:
    from django.contrib.gis.utils import GeoIP


__all__ = ['GeoIP']
