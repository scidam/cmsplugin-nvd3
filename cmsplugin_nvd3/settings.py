# ------------------ Cmsplugin-nvd3 setting defaults --------------------

# Value separator for x-data
CMSNVD3_DATASEP = ','

# Group separator for y-series
CMSNVD3_YDATAGROUPSEP = ';'

# Length of random part of id
CMSNVD3_ID_RANDOM_LENGTH = 7

# Container prefix; used only if container name is not specified by user
CMSNVD3_CONT_ID_PREFIX = 'nvd3id_'

# Default container width; used if not specified
CMSNVD3_CONT_WIDTH = 600

# Default container height; used if not specified
CMSNVD3_CONT_HEIGHT = 400

# Maximum allowed container size; all values of width or height will be
# reduced to defaults if them exeed this value
CMSNVD3_MAX_CONT_DIM = 3000

# D3, NVD3 sources. You can define it as 'local' to use local copy from static dir
CMSNVD3_D3JS_SOURCE = '//cdnjs.cloudflare.com/ajax/libs/d3/3.5.6/d3.min.js'
CMSNVD3_JS_SOURCE = '//cdn.rawgit.com/novus/nvd3/v1.8.1/build/nv.d3.min.js'
CMSNVD3_CSS = '//cdn.rawgit.com/novus/nvd3/v1.8.1/build/nv.d3.css'

#
CMSNVD3_URL = 'nvd3plugin/'
