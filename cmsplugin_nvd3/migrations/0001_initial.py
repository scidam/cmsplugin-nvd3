# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    operations = [
        migrations.CreateModel(
            name='NVD3Model',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('chart_type', models.CharField(choices=[(b'lineWithFocusChart', b'lineWithFocusChart'), (b'lineChart', b'lineChart'), (b'multiBarChart', b'multiBarChart'), (b'pieChart', b'pieChart'), (b'stackedAreaChart', b'stackedAreaChart'), (b'multiBarHorizontalChart', b'multiBarHorizontalChart'), (b'linePlusBarChart', b'linePlusBarChart'), (b'cumulativeLineChart', b'cumulativeLineChart'), (b'discreteBarChart', b'discreteBarChart'), (b'scatterChart', b'scatterChart')], default=b'lineChart', help_text='Select chart type', max_length=30, verbose_name='Chart type')),
                ('width', models.IntegerField(blank=True, default=600)),
                ('height', models.IntegerField(blank=True, default=400)),
                ('color_category', models.CharField(blank=True, choices=[(b'category10', b'category10'), (b'category20', b'category20'), (b'category20c', b'category20c')], default=b'category10', help_text='', max_length=15, verbose_name='Color category')),
                ('x_is_date', models.BooleanField(default=False, help_text='If True, x-axis values will                                        be treated as dates', verbose_name='Is x-axis date?')),
                ('x_date_format', models.CharField(blank=True, default=b'%d %b %Y', help_text='Current x-axis date format string', max_length=15, verbose_name='Date format string')),
                ('xdata', models.TextField(help_text='Values separated by commas', verbose_name=b'X-data')),
                ('ydata', models.TextField(blank=True, help_text='Groups of values separated by commas; groups are separated by semicolons', verbose_name=b'Y-data')),
                ('ynames', models.TextField(blank=True, help_text='Curve names separated by commas. Optional.', verbose_name=b'Y-names')),
                ('container_name', models.CharField(blank=True, default=b'', help_text='Id of chart container, i.e. id of a div html tag. Default: CONTAINER_ID_PREFIX+random symbols. Optional.', max_length=30, verbose_name='Chart wrapper container id')),
                ('attrs', models.TextField(blank=True, default=b'', help_text='Additional chart attributes given as a python dict; see python-nvd3 docs.', verbose_name='Chart attributes. Optional.')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
