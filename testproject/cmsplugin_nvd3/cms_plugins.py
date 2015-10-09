import uuid
import ast
import re

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from nvd3.NVD3Chart import NVD3Chart
from nvd3 import lineWithFocusChart, lineChart, \
    multiBarChart, pieChart, stackedAreaChart, \
    multiBarHorizontalChart, linePlusBarChart, \
    cumulativeLineChart, discreteBarChart, scatterChart

from cmsplugin_nvd3.settings import *
from cmsplugin_nvd3.models import NVD3model
  
def _xdataloader(xdata):
    data = None
    try:
        data = xdata.split(DATASEP)
    except AttributeError:
        pass
    return data
    

def _ydataloader(ydata):
    data = []
    try:
        for item in ydata.split(YDATAGROUPSEP):
            try:
                data.append(item.split(DATASEP))
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


class NVD3CMSPlugin(CMSPluginBase):
    model = NVD3model  # model where plugin data are saved
    name = _("NVD3 Plugin")
    render_template = "cmsplugin_nvd3/nvd3plugin.html"
    
    def render(self, context, instance, placeholder):
        xdata, ydata, pie_colors, error, html_container = None, None, None, None, None
        if instance.chart_type not in NVD3model.CHART_TYPES:
            error = _('Chart type not specified.')
        
        if instance.container_name == 'unique':
            container_name = uuid.uuid4().hex[:ID_RANDOM_LENGTH]
        elif not instance.container_name:
            container_name = uuid.uuid4().hex[:ID_RANDOM_LENGTH]
        else:
            container_name = instance.container_name

        container_name = CONTAINER_NAME_ID_PREFIX + container_name

        if re.match(r'[a-zA-Z0-9\-]+',  instance.container_name) and instance.container_name!='unique':
            container_name = instance.container_name

        #xdata len == ydata len
        xdata = _xdataloader(instance.xdata)
        ydata = _ydataloader(instance.ydata)
        
        ynames = instance.ynames.split(',')
        
        if instance.chart_type == 'pieChart':
            try:
                pie_colors = instance.pie_colors.split(',')
            except:
                pie_colors = DEFAULT_PIE_COLORS
        
        if not all(map(lambda x: len(x)==len(xdata), ydata)):
            error = _("""Length of some of ydata arrays not equal to the xdata one. Check inputs.""")

        try:
            extra_attrs = ast.literal_eval(instance.attrs)
        except:
            extra_attrs = {}
            
        if xdata and ydata and not error:
            pars = {'x_is_date': instance.x_is_date, 
                    'x_axis_format': instance.x_date_format,
                    'color_category': instance.color_category,
                    'name': container_name,
                    'color_list': pie_colors
                   }
            pars.update(extra_attrs)
            if instance.chart_type == 'pieChart' and pie_colors!=DEFAULT_PIE_COLORS:
               pars['color_category'] = None
            
            chart = eval(instance.chart_type)(**pars)
            
            if len(ynames)!=len(ydata):
                ynames = map(lambda x: _('serie ') + str(x+1), range(len(ydata)))
            
            for yitem, yname in zip(ydata, ynames):
                chart.add_serie(name=yname, y=yitem, x=xdata)
            
            chart.display_container = False
            chart.buildcontent()
            outputhtml = chart.htmlcontent + '\n'
            
            chart_container = NVD3Chart()
            chart_container.name = str(container_name)
            chart_container.set_graph_height(_safe_int(instance.height) or NVD3_CONTAINER_HEIGHT)
            chart_container.set_graph_width(_safe_int(instance.width) or NVD3_CONTAINER_WIDTH)
            chart_container.buildcontainer()
            html_container = chart_container.container + '\n'
        else:
            outputhtml = None
            if not error:
                error = "X-data or Y-data not defined correctly."

        context.update({'htmldata': outputhtml, 'error': error, 'htmlcontainer': html_container})
        return context
    
plugin_pool.register_plugin(NVD3CMSPlugin)