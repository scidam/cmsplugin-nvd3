from django.conf import settings

#Value separator for x-data
DATASEP = getattr(settings, 'DATASEP', ',')

#Group separator for y-series
YDATAGROUPSEP = getattr(settings, 'YDATAGROUPSEP', ';')

#Used in piechart only
DEFAULT_PIE_COLORS = getattr(settings, 'DEFAULT_PIE_COLORS', ['red', 'green', 'orange', 'blue'])

#Length of random part of id 
ID_RANDOM_LENGTH = getattr(settings, 'ID_RANDOM_LENGTH', 7)

#Container prefix; used only if container name is not specified by user
CONTAINER_NAME_ID_PREFIX = getattr(settings, 'CONTAINER_NAME_ID_PREFIX', 'nvd3id-')

#Default container width; used if not specified
NVD3_CONTAINER_WIDTH = getattr(settings, 'NVD3_CONTAINER_WIDTH', 600)

#Default container height; used if not specified
NVD3_CONTAINER_HEIGHT = getattr(settings, 'NVD3_CONTAINER_HEIGHT', 400)

#Maximum allowed container size; all values of width or height will be reduced to defaults if them exeed this value
MAX_CONTAINER_DIM = getattr(settings, 'MAX_CONTAINER_DIM', 3000)
