#-*- coding: utf-8 -*-
import os

from django.contrib.gis.utils import LayerMapping
from ongs.models import mdgShoreline, mdgRegion, mdgDistrict, mdgCommune

# Auto-generated `LayerMapping` dictionary for mdgShoreline model
mdgshoreline_mapping = {
    'name' : 'NAME',
    'name_iso' : 'NAME_ISO',
    'geom' : 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for mdgRegion model
mdgregion_mapping = {
    'id_faritan' : 'id_faritan',
    'faritany' : 'faritany',
    'id_region' : 'id_region',
    'region' : 'region',
    'geom' : 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for mdgDistrict model
mdgdistrict_mapping = {
    'id_faritan' : 'id_faritan',
    'faritany' : 'faritany',
    'id_region' : 'id_region',
    'region' : 'region',
    'id_distric' : 'id_distric',
    'district' : 'district',
    'geom' : 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for mdgCommune model
mdgcommune_mapping = {
    'id_faritan' : 'id_faritan',
    'faritany' : 'faritany',
    'id_region' : 'id_region',
    'region' : 'region',
    'id_distric' : 'id_distric',
    'district' : 'district',
    'id_commune' : 'id_commune',
    'commune' : 'commune',
    'geom' : 'MULTIPOLYGON',
}

mdgShoreline_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'static/MG_shp/MDG_shoreline.shp'))
mdgRegion_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'static/MG_shp/MDG_region.shp'))
mdgDistrict_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'static/MG_shp/MDG_district.shp'))
mdgCommune_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'static/MG_shp/MDG_commune.shp'))

def run(verbose=True):
    lm1 = LayerMapping(mdgShoreline, mdgShoreline_shp, mdgshoreline_mapping,
                      transform=False, encoding='iso-8859-1')

    lm1.save(strict=True, verbose=verbose)

    lm2 = LayerMapping(mdgRegion, mdgRegion_shp, mdgregion_mapping,
                      transform=False, encoding='iso-8859-1')

    lm2.save(strict=True, verbose=verbose)

    lm3 = LayerMapping(mdgDistrict, mdgDistrict_shp, mdgdistrict_mapping,
                      transform=False, encoding='iso-8859-1')

    lm3.save(strict=True, verbose=verbose)

    lm4 = LayerMapping(mdgCommune, mdgCommune_shp, mdgcommune_mapping,
                      transform=False, encoding='iso-8859-1')

    lm4.save(strict=True, verbose=verbose)

# Now you may run the script from the shell, and the shapefile will be loaded in your spatial database:

"""
# A (Supprimer avant de) lancer depuis le shell
python manage.py shell

from ongs import load_shp
load_shp.run()

"""



