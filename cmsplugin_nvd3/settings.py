from django.conf import settings

# Value separator for x-data
DATASEP = getattr(settings, 'DATASEP', ',')

# Group separator for y-series
YDATAGROUPSEP = getattr(settings, 'YDATAGROUPSEP', ';')

# Length of random part of id
ID_RANDOM_LENGTH = getattr(settings, 'ID_RANDOM_LENGTH', 7)

# Container prefix; used only if container name is not specified by user
CONTAINER_NAME_ID_PREFIX = getattr(settings, 'CONTAINER_NAME_ID_PREFIX',
                                   'nvd3id_')

# Default container width; used if not specified
NVD3_CONTAINER_WIDTH = getattr(settings, 'NVD3_CONTAINER_WIDTH', 600)

# Default container height; used if not specified
NVD3_CONTAINER_HEIGHT = getattr(settings, 'NVD3_CONTAINER_HEIGHT', 400)

# Maximum allowed container size; all values of width or height will be
# reduced to defaults if them exeed this value
MAX_CONTAINER_DIM = getattr(settings, 'MAX_CONTAINER_DIM', 3000)

# D3 sources. You can define it as 'local' to use local copy from static dir
D3JS_SOURCE = getattr(settings, 'D3JS_SOURCE',
                      '//cdnjs.cloudflare.com/ajax/libs/d3/3.5.6/d3.min.js')
NVD3JS_SOURCE = getattr(settings, 'NVD3JS_SOURCE',
                        '//cdn.rawgit.com/novus/nvd3/v1.8.1/build/nv.d3.min.js'
                        )
NVD3_CSS = getattr(settings, 'NVD3_CSS',
                   '//cdn.rawgit.com/novus/nvd3/v1.8.1/build/nv.d3.css')

