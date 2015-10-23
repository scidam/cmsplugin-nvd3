from django.db import models
from cms.models import CMSPlugin
from django.utils.translation import ugettext_lazy as _


class BaseNVD3model(CMSPlugin):
    CHART_TYPES = ['lineWithFocusChart',
                   'lineChart', 'multiBarChart', 'pieChart',
                   'stackedAreaChart', 'multiBarHorizontalChart',
                   'linePlusBarChart', 'cumulativeLineChart',
                   'discreteBarChart', 'scatterChart'
                   ]
    CHART_TYPES_CHOICES = tuple((x, x) for x in CHART_TYPES)
    COLOR_CATEGORIES = (('category10', 'category10'),
                        ('category20', 'category20'),
                        ('category20c', 'category20c')
                        )

    # Common attributes
    chart_type = models.CharField(max_length=30, verbose_name=_('Chart type'),
                                  help_text=_('Select chart type'),
                                  default=CHART_TYPES_CHOICES[1][0],
                                  choices=CHART_TYPES_CHOICES)
    width = models.IntegerField(max_length=10, default=600, blank=True)
    height = models.IntegerField(max_length=10, default=400, blank=True)
    container_name = models.CharField(max_length=30,
                                      verbose_name=_('Wrapper container id'),
                                      default='unique',
                                      help_text=_('If `unique`,\
                                       id will be set randomly each time'))
    color_category = models.CharField(max_length=15, help_text=_(''),
                                      verbose_name=_('Color category'),
                                      default=COLOR_CATEGORIES[0][0],
                                      choices=COLOR_CATEGORIES,
                                      blank=True)

    # X -axis-properties
    x_is_date = models.BooleanField(
                            default=False,
                            verbose_name=_('X-axis is of date-format?'),
                            help_text=_('If True, x-axis values will\
                                        be treated as of date-format'),
                            blank=True
                                    )
    x_date_format = models.CharField(
                            max_length=15, default='%d %b %Y',
                            help_text=_('Current x-axis date format'),
                            verbose_name=_('Date format'), blank=True
                                     )

    # data
    xdata = models.TextField(verbose_name='X-data',
                             help_text=_('Values separated by commas'))
    ydata = models.TextField(verbose_name='Y-data', blank=True,
                             help_text=_('Groups of values separated by commas;\
                             groups should be separated by semicolons'))
    ynames = models.TextField(verbose_name='Y-names',
                              help_text=_('Series names separated by commas'),
                              blank=True)
    sattrs = models.TextField(verbose_name='Series attrs',
                              help_text=_('Extra series attrs separated as y-data groups.\
                                          Also, see python-nvd3 documentation.'),
                              blank=True)
    attrs = models.TextField(blank=True,
                             help_text=_('Additional chart attributes'),
                             default='', verbose_name=_('Chart attributes')
                             )

    class Meta:
        abstract = True


class NVD3model(BaseNVD3model):
    class Meta:
        abstract = False
