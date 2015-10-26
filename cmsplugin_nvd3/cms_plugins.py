import ast
import re
import uuid

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from nvd3 import lineWithFocusChart, lineChart, \
    multiBarChart, pieChart, stackedAreaChart, \
    multiBarHorizontalChart, linePlusBarChart, \
    cumulativeLineChart, discreteBarChart, scatterChart
from nvd3.NVD3Chart import NVD3Chart

from cmsplugin_nvd3.models import NVD3model
from cmsplugin_nvd3.settings import *


NVD3_STATIC = getattr(settings, 'STATIC_URL', '') + '/nvd3plugin/'


def _xdataloader(xdata):
    data = None
    try:
        data = xdata.split(DATASEP)
    except AttributeError:
        pass
    return [x.strip() for x in data]


def _ydataloader(ydata):
    data = []
    try:
        for item in ydata.split(YDATAGROUPSEP):
            try:
                data.append([x.strip() for x in item.split(DATASEP)])
            except:
                pass
    except AttributeError:
        pass
    return data


def _safe_int(x):
    try:
        res = int(x)
    except:
        return None
    if res < 0.0 or res > MAX_CONTAINER_DIM:
        return None
    return res


class NVD3CMSPlugin(CMSPluginBase):
    model = NVD3model  # model where plugin data are saved
    name = _("NVD3 Plugin")
    render_template = "cmsplugin_nvd3/nvd3plugin.html"
    text_enabled = True

    def render(self, context, instance, placeholder):
        error, html_container = None, None
        if instance.chart_type not in NVD3model.CHART_TYPES:
            error = _('Chart type not specified.')

        # TODO: Change default behaviour of unique id field
        if instance.container_name == 'unique':
            container_name = uuid.uuid4().hex[:ID_RANDOM_LENGTH]
        elif not instance.container_name:
            container_name = uuid.uuid4().hex[:ID_RANDOM_LENGTH]
        else:
            container_name = instance.container_name

        container_name = CONTAINER_NAME_ID_PREFIX + container_name

        if re.match(r'[a-zA-Z0-9\-]+',  instance.container_name)\
           and instance.container_name != 'unique':
            container_name = instance.container_name

        # xdata len == ydata len
        xdata = _xdataloader(instance.xdata)
        ydata = _ydataloader(instance.ydata)
        series_attrs = _ydataloader(instance.sattrs)
        ynames = instance.ynames.split(',')
        if not all(map(lambda x: len(x) == len(xdata), ydata)):
            error = _("""Length of some of ydata arrays not equal\
            to the xdata one. Check inputs.""")

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
            ind = 0
            for yitem, yname in zip(ydata, ynames):
                try:
                    sextra = ast.literal_eval(series_attrs[ind])
                    chart.add_serie(name=yname, y=yitem, x=xdata, extra=sextra)
                except:
                    chart.add_serie(name=yname, y=yitem, x=xdata)
                ind += 1

            chart.display_container = False
            chart.buildcontent()
            outputhtml = chart.htmlcontent + '\n'

            chart_container = NVD3Chart()
            chart_container.name = str(container_name)
            chart_container.set_graph_height(
                _safe_int(instance.height) or NVD3_CONTAINER_HEIGHT
                                             )
            chart_container.set_graph_width(
                _safe_int(instance.width) or NVD3_CONTAINER_WIDTH
                                            )
            chart_container.buildcontainer()
            html_container = chart_container.container + '\n'

            if D3JS_SOURCE.lower() == 'local':
                d3js_src = NVD3_STATIC + 'd3.min.js'
            else:
                d3js_src = D3JS_SOURCE

            if NVD3JS_SOURCE.lower() == 'local':
                nvd3js_src = NVD3_STATIC + 'nv.d3.min.js'
            else:
                nvd3js_src = NVD3JS_SOURCE

            if NVD3_CSS.lower() == 'local':
                nvd3css_src = NVD3_STATIC + 'nv.d3.css'
            else:
                nvd3css_src = NVD3_CSS
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
        return NVD3_STATIC + u"icon.png"

plugin_pool.register_plugin(NVD3CMSPlugin)
