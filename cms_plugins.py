from django.template.defaultfilters import register
from django.utils.safestring import mark_safe
from django.conf import settings


from django.utils.translation import ugettext_lazy as _

import uuid
import ast

from cms.plugin_base import CMSPluginBase
from .models import NVD3model


from nvd3.NVD3Chart import NVD3Chart
from nvd3 import lineWithFocusChart, lineChart, \
    multiBarChart, pieChart, stackedAreaChart, \
    multiBarHorizontalChart, linePlusBarChart, \
    cumulativeLineChart, discreteBarChart, scatterChart
  

DATASEP = ','
YDATAGROUPSEP = ';'
DEFAULT_PIE_COLORS = ['red', 'green', 'orange', 'blue']
ID_RANDOM_LENGTH = 7
CONTAINER_NAME_ID_PREFIX = 'nvd3id-'


def _xdataloader(xdata):
    data = None
    try:
        data = xdata.split(sep=DATASEP)
    except AttributeError:
        pass
    return data
    

def _ydataloader(ydata):
    data = []
    try:
        for item in ydata.split(sep=YDATAGROUPSEP):
            try:
                data.append(item.split(sep=DATASEP))
            except:
                pass
    except AttributeError:
        pass
    return data 


def NVD3CMSPlugin(CMSPluginBase):
    model = NVD3model  # model where plugin data are saved
    name = _("NVD3 Plugin")
    render_template = "cmsplugin_nvd3/nvd3plugin.html"
    
    def render(self, context, instance, placeholder):
        xdata, ydata, pie_colors, error = None, None, None, None
        if instance.chart_type not in NVD3model.CHART_TYPES:
            error = _('Chart type not specified.')
        
        if instance.container_name == 'unique':
            container_name = uuid.uuid4().hex[:ID_RANDOM_LENGTH]
        elif not instance.container_name:
            container_name = uuid.uuid4().hex[:ID_RANDOM_LENGTH]
        else:
            container_name = instance.container_name
        
        container_name+=CONTAINER_NAME_ID_PREFIX  
        
        #xdata len == ydata len
        xdata = _xdataloader(instance.xdata)
        ydata = _ydataloader(instance.ydata)
        
        ynames = instance.ynames.split(sep=',')
        
        if instance.chart_type == 'pieChart':
            try:
                pie_colors = instance.pie_colors.split(sep=',')
            except:
                pie_colors = DEFAULT_PIE_COLORS
        
        if not all(map(lambda x: len(x)==len(xdata), ydata)):
            error = _('Some of ydata array has different length to xdata. Check inputs.')

        try:
            extra_attrs = ast.literal_eval(instance.attrs)
        except:
            extra_attrs = {}
            
        if xdata and ydata and not error:
            pars = {'x_is_date': instance.x_is_date, 
                    'x_axis_format': instance.x_axis_format,
                    'color_category': instance.color_category,
                    'name': container_name
                   }
            pars.update(extra_attrs)
            chart = eval(instance.chart_type)(**pars)
            
            if len(ynames)!=len(ydata):
                ynames = map(lambda x: _('serie ') + str(x+1), xrange(len(ydata)))
            
            for yitem, yname in zip(ydata, ynames):
                chart.add_serie(name=yname, y=yitem, x=xdata)
            
            chart.display_container = False
            chart.buildcontent()
            outputhtml = chart.htmlcontent + '\n'
        else:
            outputhtml = None
            if not error:
                error = "X-data or Y-data not defined correctly."
                
        context.update({'html': outputhtml, 'error': error})
        return context
    
  
@register.simple_tag
def load_chart(chart_type, series, container, kw_extra={}, *args, **kwargs):
    """Loads the Chart objects in the container.
    **usage**:
        {% load_chart "lineWithFocusChart" data_set "div_lineWithFocusChart" %}
    **Arguments**:
        * ``chart_type`` - Give chart type name eg. lineWithFocusChart/pieChart
        * ``series`` - Data set which are going to be plotted in chart.
        * ``container`` - Chart holder in html page.
    **kw_extra settings**::
        * ``x_is_date`` - if enabled the x-axis will be display as date format
        * ``x_axis_format`` - set the x-axis date format, ie. "%d %b %Y"
        * ``tag_script_js`` - if enabled it will add the javascript tag '<script>'
        * ``jquery_on_ready`` - if enabled it will load the javascript only when page is loaded
            this will use jquery library, so make sure to add jquery to the template.
        * ``color_category`` - Define color category (eg. category10, category20, category20c)
        * ``chart_attr`` - Custom chart attributes
    """
    if not chart_type:
        return False

    if 'x_is_date' not in kw_extra:
        kw_extra['x_is_date'] = False
    if 'x_axis_format' not in kw_extra:
        kw_extra['x_axis_format'] = "%d %b %Y"
    if 'color_category' not in kw_extra:
        kw_extra['color_category'] = "category20"
    if 'tag_script_js' not in kw_extra:
        kw_extra['tag_script_js'] = True
    if 'chart_attr' not in kw_extra:
        kw_extra['chart_attr'] = {}
    # set the container name
    kw_extra['name'] = str(container)

    # Build chart
    chart = eval(chart_type)(**kw_extra)

    xdata = series['x']
    y_axis_list = [k for k in series.keys() if k.startswith('y')]
    if len(y_axis_list) > 1:
        # Ensure numeric sorting
        y_axis_list = sorted(y_axis_list, key=lambda x: int(x[1:]))

    for key in y_axis_list:
        ydata = series[key]
        axis_no = key.split('y')[1]

        name = series['name' + axis_no] if series.get('name' + axis_no) else None
        extra = series['extra' + axis_no] if series.get('extra' + axis_no) else {}
        kwargs = series['kwargs' + axis_no] if series.get('kwargs' + axis_no) else {}

        chart.add_serie(name=name, y=ydata, x=xdata, extra=extra, **kwargs)

    chart.display_container = False
    chart.buildcontent()

    html_string = chart.htmlcontent + '\n'
    return mark_safe(html_string)


@register.simple_tag
def include_container(include_container, height=400, width=600):
    """
    Include the html for the chart container and css for nvd3
    This will include something similar as :
        <div id="containername"><svg style="height:400px;width:600px;"></svg></div>
    **usage**:
        {% include_container "lineWithFocusChart" 400 400 %}
    **Arguments**:
        * ``include_container`` - container_name
        * ``height`` - Chart height
        * ``width`` - Chart width
    """
    chart = NVD3Chart()
    chart.name = str(include_container)
    chart.set_graph_height(height)
    chart.set_graph_width(width)
    chart.buildcontainer()
    return mark_safe(chart.container + '\n')






@register.simple_tag
def include_chart_jscss(static_dir='', css_dir='', js_dir=''):
    """
    Include the html for the chart container and css for nvd3
    This will include something similar as :
        <link media="all" href="/static/nvd3/src/nv.d3.css" type="text/css" rel="stylesheet" />
        <script src="/static/d3/d3.min.js" type="text/javascript"></script>
        <script src="/static/nvd3/nv.d3.min.js" type="text/javascript"></script>
    **usage**:
        {% include_chart_jscss %}
    Or if you want to specify a subdirectory below STATIC_URL for all static files,
        {% include_chart_jscss 'newfies' %}
    Or if you have all your CSS and JS files in particular directories and want to specify them,
        {% include_chart_jscss css_dir='css' js_dir='js' %}
    **Arguments**:
        * ``static_dir`` -
        * ``css_dir`` -
        * ``js_dir`` -
    """
    if static_dir:
        static_dir += '/'

    css_files_dirs = {}
    js_files_dirs = {}

    css_files_dirs['nv.d3.min.css'] = '%s%snvd3/build/' % (settings.STATIC_URL, static_dir)

    js_files_dirs['d3.min.js'] = '%s%sd3/' % (settings.STATIC_URL, static_dir)
    js_files_dirs['nv.d3.min.js'] = '%s%snvd3/build/' % (settings.STATIC_URL, static_dir)

    if css_dir:
        if not css_dir.endswith('/'):
            css_dir += '/'
        for css_file in css_files_dirs:
            css_files_dirs[css_file] = '%s%s%s' % (settings.STATIC_URL, static_dir, css_dir)

    if js_dir:
        if not js_dir.endswith('/'):
            js_dir += '/'
        for js_file in js_files_dirs:
            js_files_dirs[js_file] = '%s%s%s' % (settings.STATIC_URL, static_dir, js_dir)

    chart = NVD3Chart()
    chart.header_css = [
        '<link media="all" href="%s" type="text/css" rel="stylesheet" />\n' % h for h in
        (
            '%s%s' % (path, css_file) for css_file, path in css_files_dirs.items()
        )
    ]

    chart.header_js = [
        '<script src="%s" type="text/javascript"></script>\n' % h for h in
        (
            '%s%s' % (path, js_file) for js_file, path in js_files_dirs.items()
        )
    ]
    chart.buildhtmlheader()
    return mark_safe(chart.htmlheader + '\n')
  