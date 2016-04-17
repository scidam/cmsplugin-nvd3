import ast
import re
import uuid

from nvd3 import lineWithFocusChart, lineChart, \
    multiBarChart, pieChart, stackedAreaChart, \
    multiBarHorizontalChart, linePlusBarChart, \
    cumulativeLineChart, discreteBarChart, scatterChart
from nvd3.NVD3Chart import NVD3Chart

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cmsplugin_nvd3.models import NVD3Model
from cmsplugin_nvd3.utils import _xdataloader, _ydataloader, _safe_int
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class NVD3CMSPlugin(CMSPluginBase):
    model = NVD3Model  # model where plugin data are saved
    name = _("NVD3 Plugin")
    render_template = "cmsplugin_nvd3/nvd3plugin.html"
    text_enabled = True
    NVD3_STATIC = getattr(settings, 'STATIC_URL', '') + settings.CMSNVD3_URL

    def render(self, context, instance, placeholder):
        error, html_container = None, None
        if instance.chart_type not in NVD3Model.CHART_TYPES:
            error = _('Chart type is not specified or of not valid type.')

        if not instance.container_name:
            container_name = uuid.uuid4().hex[:settings.CMSNVD3_ID_RANDOM_LENGTH]
            container_name = settings.CMSNVD3_CONT_ID_PREFIX + container_name
        elif re.match(r'[a-zA-Z0-9\-]+',  instance.container_name):
            container_name = instance.container_name
        else:
            container_name = uuid.uuid4().hex[:settings.CMSNVD3_ID_RANDOM_LENGTH]
            container_name = settings.CMSNVD3_CONT_ID_PREFIX + container_name

        # xdata len == ydata len
        xdata = _xdataloader(instance.xdata)
        ydata = _ydataloader(instance.ydata)
        ynames = instance.ynames.split(settings.CMSNVD3_DATASEP)
        if not all(map(lambda x: len(x) == len(xdata), ydata)):
            # This is validation after data loading
            error = _("""Length of one of ydata arrays not equal\
 to length of the xdata array. Check inputs.""")

        try:
            extra_attrs = ast.literal_eval(instance.attrs)
        except:
            extra_attrs = {}

        if xdata and ydata and not error:
            pars = {'x_is_date': instance.x_is_date,
                    'color_category': instance.color_category,
                    'name': container_name,
                    }
            if instance.chart_type in ['multiBarChart']:
                pars.update({'x_axis_format': None})
            if instance.x_is_date:
                pars.update({'x_axis_format': instance.x_date_format})
            pars.update(extra_attrs)
            chart = eval(instance.chart_type)(**pars)
            if len(ynames) != len(ydata):
                ynames = map(lambda x: _('serie ') + str(x+1),
                             range(len(ydata)))
            for yitem, yname in zip(ydata, ynames):
                chart.add_serie(name=yname, y=yitem, x=xdata)

            chart.display_container = False
            chart.buildcontent()
            outputhtml = chart.htmlcontent + '\n'

            chart_container = NVD3Chart()
            chart_container.name = str(container_name)
            chart_container.set_graph_height(
                _safe_int(instance.height) or settings.CMSNVD3_CONT_HEIGHT
                                             )
            chart_container.set_graph_width(
                _safe_int(instance.width) or settings.CMSNVD3_CONT_WIDTH
                                            )
            chart_container.buildcontainer()
            html_container = chart_container.container + '\n'

            if settings.CMSNVD3_D3JS_SOURCE.lower() == 'local':
                d3js_src = NVD3CMSPlugin.NVD3_STATIC + 'd3.min.js'
            else:
                d3js_src = settings.CMSNVD3_D3JS_SOURCE

            if settings.CMSNVD3_JS_SOURCE.lower() == 'local':
                nvd3js_src = NVD3CMSPlugin.NVD3_STATIC + 'nv.d3.min.js'
            else:
                nvd3js_src = settings.CMSNVD3_JS_SOURCE

            if settings.CMSNVD3_CSS.lower() == 'local':
                nvd3css_src = NVD3CMSPlugin.NVD3_STATIC + 'nv.d3.css'
            else:
                nvd3css_src = settings.CMSNVD3_CSS
        else:
            nvd3js_src,\
                d3js_src, nvd3css_src, outputhtml = None, None, None, None
            if not error:
                error = "X-data or Y-data not defined correctly."

        context.update({'htmldata': outputhtml, 'error': error,
                        'htmlcontainer': html_container,
                        'd3js_src': d3js_src,
                        'nvd3js_src': nvd3js_src,
                        'nvd3css_src': nvd3css_src
                        })
        return context

    def icon_src(self, instance):
        return NVD3CMSPlugin.NVD3_STATIC + u"nvd3icon.png"

plugin_pool.register_plugin(NVD3CMSPlugin)
