def import_simplejson():
    try:
        import simplejson as json
    except ImportError:
        import json

    return json
