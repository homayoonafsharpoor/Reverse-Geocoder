def classFactory(iface):
    from .reverse_geocoder import ReverseGeocoder
    return ReverseGeocoder(iface)
