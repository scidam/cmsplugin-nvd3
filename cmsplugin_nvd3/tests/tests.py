from __future__ import print_function

import os

from cms.api import add_plugin
from cms.models import Page
from cms.models import Placeholder
from cms.test_utils.testcases import CMSTestCase
from django.conf import settings
from django.conf.urls import url, patterns, include
from django.contrib import admin
from django.test import TestCase
from django.test.client import Client
from django.test.utils import override_settings

# from cmsplugin_nvd3.cms_plugins import NVD3_STATIC


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('cms.urls')),
)

CMS_TEMPLATES = (('test.html', 'test'),)
TEMPLATE_DIRS = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), 'templates'
                              )



class LazyNVD3PluginTestCase(TestCase):

    def setUp(self):
        placeholder = Placeholder.objects.create(slot='content')
        # valid curve names
        self.plugin1 = add_plugin(placeholder, 'NVD3CMSPlugin', 'en')
        self.plugin1.xdata = '1, 2, 3'
        self.plugin1.ydata = '4,5,6; 7,8,9'
        self.plugin1.ynames = 'river, bank'
        self.plugin1.container_name = 'unique'

        # invalid curve names should be defined as default serie+No
        self.plugin2 = add_plugin(placeholder, 'NVD3CMSPlugin', 'en')
        self.plugin2.xdata = '1, 2, 3'
        self.plugin2.ydata = '4,5,6; 7,8,9'
        self.plugin2.ynames = 'river, bank, block'
        self.plugin2.container_name = 'my-unique-container'

        # simple pieChart testing
        self.plugin3 = add_plugin(placeholder, 'NVD3CMSPlugin', 'en')
        self.plugin3.chart_type = 'pieChart'
        self.plugin3.xdata = 'Banana, Strawberry, Orange, Apple'
        self.plugin3.ydata = '10, 40, 60, 70'

    def test_simple_plugin1(self):
        html1 = self.plugin1.render_plugin(context={})
        self.assertIn('river', html1)
        self.assertIn('bank', html1)
        self.assertIn('id="nvd3id_', html1)

    def test_simple_plugin2(self):
        html2 = self.plugin2.render_plugin(context={})
        self.assertIn('serie 1', html2)
        self.assertIn('serie 2', html2)
        self.assertIn('id="my-unique-container"', html2)

    def test_simple_pieChart(self):
        html3 = self.plugin3.render_plugin(context={})
        self.assertIn('Banana', html3)
        self.assertIn('Strawberry', html3)
        self.assertIn('Orange', html3)
        self.assertIn('Apple', html3)

#     @override_settings(NVD3JS_SOURCE='local', D3JS_SOURCE='local',
#                        NVD3_CSS='local')
#     def test_d3paths(self):
#         html3 = self.plugin3.render_plugin(context={})
#         self.assertIn('', html3)


class RenderPluginTestCase(CMSTestCase):

    def setUp(self):
        # Every test needs a client.
        self.page = Page.objects.create(site_id=settings.SITE_ID, template='test.html')
        placeholder = self.page.placeholders.get(slot='test')
        self.plugin = add_plugin(placeholder, 'NVD3CMSPlugin', 'en')
        self.client = Client()

    @override_settings(CMS_TEMPLATES=CMS_TEMPLATES,
                       TEMPLATE_DIRS=TEMPLATE_DIRS,
                       ROOT_URLCONF='cmsplugin_nvd3.tests.tests')
    def test_LineChart(self):
        self.plugin.chart_type = 'lineChart'
        self.plugin.xdata = ' 1, 2, 3'
        self.plugin.ydata = '5,6,7; 8,9,10'
        self.plugin.ynames = 'one curve, two curve'
        self.page.publish()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.asserIn('lineChart', response.content)
