from cms.models import CMSPlugin
from cmsplugin_nvd3.utils import _xdataloader, _ydataloader
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
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
    width = models.IntegerField(default=600, blank=True)
    height = models.IntegerField(default=400, blank=True)

    color_category = models.CharField(max_length=15, help_text=_(''),
                                      verbose_name=_('Color category'),
                                      default=COLOR_CATEGORIES[0][0],
                                      choices=COLOR_CATEGORIES,
                                      blank=True)

    # X -axis-properties
    x_is_date = models.BooleanField(
                            default=False,
                            verbose_name=_('Is x-axis date?'),
                            help_text=_('If True, x-axis values will\
                                        be treated as dates'),
                            blank=True
                                    )
    x_date_format = models.CharField(
                            max_length=15, default='%d %b %Y',
                            help_text=_('X-axis date format string (Used if the pervious is True)'),
                            verbose_name=_('Date format string'), blank=True
                                     )

    # data
    xdata = models.TextField(verbose_name='X-data',
                             help_text=_('Values separated by commas'))
    ydata = models.TextField(verbose_name='Y-data', blank=True,
                             help_text=_('Group(s) of values separated by commas;\
 groups (to plot a few curves) are separated by semicolons'))
    ynames = models.TextField(verbose_name='Y-names',
                              help_text=_('Curve names separated by commas. Optional.'),
                              blank=True)
    container_name = models.CharField(max_length=30,
                                      verbose_name=_('Chart wrapper container id'),
                                      default='',
                                      help_text=_('Id of chart container, i.e. id of a div html tag.\
 Default: CONTAINER_ID_PREFIX+random symbols. Optional.'), blank=True)

    # Extra chart attrs
    attrs = models.TextField(blank=True,
                             help_text=_('Additional chart \
attributes given as a python dict; see python-nvd3 docs'),
                             default='', verbose_name=_('Chart attributes. Optional.')
                             )

    def __str__(self):
        return u"NVD3: " + self.chart_type

    def clean(self):

        if self.width < 0.0 or self.width > settings.CMSNVD3_MAX_CONT_DIM:
            raise ValidationError(
                _("Container width should be in interval [0, %s]."
                  % settings.CMSNVD3_MAX_CONT_DIM))

        if self.height < 0.0 or self.height > settings.CMSNVD3_MAX_CONT_DIM:
            raise ValidationError(
                _("Container height should be in interval [0, %s]."
                  % settings.CMSNVD3_MAX_CONT_DIM))

        if self.x_is_date and not self.x_date_format:
            raise ValidationError(
                _("X-axis is of date-format. \
You should provide valid format string in the <Date format string> field."))
        xdata = _xdataloader(self.xdata)
        ydata = _ydataloader(self.ydata)
        if not all(map(lambda x: len(x) == len(xdata), ydata)):
            raise ValidationError(_("Length of one of the Y-data arrays not equal\
 to length of the X-data array. Check input data."))

    class Meta:
        abstract = True


class NVD3Model(BaseNVD3model):
    class Meta:
        abstract = False
