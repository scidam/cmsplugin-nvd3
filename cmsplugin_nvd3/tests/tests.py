from django.test import TestCase

from cms.api import add_plugin, create_page, publish_page

from django.test.client import Client
from django.test.utils import override_settings
from django.contrib.auth.models import User
from django.conf import settings

@override_settings(ROOT_URLCONF='tests.urls')
class RenderPluginTestCase(TestCase):

    def setUp(self):

        # create a User
        self.testuser = User.objects.create_superuser('test',
                                                      'test@example.com',
                                                      'testpass')

        # Every test needs a client.
        self.page = create_page('Test Page', 'test.html', 'en', slug='/',
                                created_by=self.testuser)
        placeholder = self.page.placeholders.get(slot='slot')

        # -------------------------Add different plugins ----------------------
        add_plugin(placeholder, 'NVD3CMSPlugin', 'en',
                   xdata=' 1, 2, 3', ydata='5,6,7; 8,9,10',
                   ynames='one curve, two curve', chart_type='lineChart')

        add_plugin(placeholder, 'NVD3CMSPlugin', 'en',
                   xdata='Banana, Strawberry, Orange, Apple',
                   ydata='10, 40, 60, 70', ynames='one curve, two curve',
                   chart_type='pieChart')

        add_plugin(placeholder, 'NVD3CMSPlugin', 'en',
                   chart_type='scatterChart', xdata='3, 4, 0, -3, 5, 7',
                   ydata='-1, 2, 3, 3, 15, 2; 1, -2, 4, 7, -5, 3',
                   ynames='chartsca1, chartsca2'
                   )

        add_plugin(placeholder, 'NVD3CMSPlugin', 'en',
                   chart_type='multiBarChart',
                   xdata='onebar1, twobar2, threebar3',
                   ydata='1,2,3; 4,5,6'
                   )

        add_plugin(placeholder, 'NVD3CMSPlugin', 'en',
                   chart_type='multiBarHorizontalChart',
                   xdata='-14, -7, 7, 14',
                   ydata='-6, 5, -1, 9;-23, -6, -32, 9',
                   ynames='multihor1, multihor2'
                   )

        add_plugin(placeholder, 'NVD3CMSPlugin', 'en',
                   chart_type='discreteBarChart',
                   xdata='Atest1, B, C, D, E, Ftest2',
                   ydata='3, 4, 0, -3, 5, 7'
                   )
        add_plugin(placeholder, 'NVD3CMSPlugin', 'en',
                   chart_type='cumulativeLineChart',
                   xdata='1365026400000000,1365026500000000,1365026600000000',
                   ydata='6, 5, 1;36, 55, 11',
                   x_is_date=True,
                   ynames='unique33,unique44')

        add_plugin(placeholder, 'NVD3CMSPlugin', 'en',
                   chart_type='stackedAreaChart',
                   xdata='100, 101, 102, 103, 104, 105, 106',
                   ydata='6, 11, 12, 7, 11, 10, 11;8, 20, 16, 12, 20, 28, 28',
                   ynames='unique1122, unique2211'
                   )

        add_plugin(placeholder, 'NVD3CMSPlugin', 'en',
                   chart_type='linePlusBarChart',
                   xdata='1338501600000, 1345501600000, 1353501600000',
                   x_is_date=True,
                   ydata='6, 5, 1;0.002, 0.003, 0.004',
                   ynames='leftaxis,rightaxis',
                   attrs='{"focus_enable":True}'
                   )

        add_plugin(placeholder, 'NVD3CMSPlugin', 'en',
                   chart_type='lineWithFocusChart',
                   xdata='1365026400000000,1365026500000000,1365026600000000',
                   x_is_date=True,
                   ydata='-6, 5, -1',
                   ynames='lwfctest'
                   )

        # -------------------------------------------------------------------

        publish_page(self.page, self.testuser, 'en')
        self.client = Client()
        self.response = self.client.get('/')
        self.content = str(self.response.content)

    def test_LineChart(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertIn('lineChart', self.content)
        self.assertIn('one curve', self.content)
        self.assertIn('two curve', self.content)

    def test_pieChart(self):
        # simple pieChart testing
        self.assertIn('Banana', self.content)
        self.assertIn('Strawberry', self.content)

    def test_scatterChart(self):
        self.assertIn('chartsca1', self.content)
        self.assertIn('chartsca2', self.content)

    def test_multiBarChart(self):
        self.assertIn('onebar1', self.content)
        self.assertIn('twobar2', self.content)
        self.assertIn('threebar3', self.content)

    def test_multiBarHorizontalChart(self):
        self.assertIn('multihor1', self.content)
        self.assertIn('multihor2', self.content)

    def test_discreteBarChart(self):
        self.assertIn('Atest1', self.content)
        self.assertIn('Ftest2', self.content)

    def test_cumulativeLineChart(self):
        self.assertIn('unique44', self.content)
        self.assertIn('unique33', self.content)

    def test_stackedAreaChart(self):
        self.assertIn('unique1122', self.content)
        self.assertIn('unique2211', self.content)

    def test_linePlusBarChart(self):
        self.assertIn('leftaxis', self.content)
        self.assertIn('rightaxis', self.content)

    def test_lineWithFocusChart(self):
        self.assertIn('lwfctest', self.content)




@override_settings(NVD3JS_SOURCE='local', D3JS_SOURCE='local',
                       NVD3_CSS='local', ROOT_URLCONF='tests.urls')
class LocalNVD3PluginTestCase(TestCase): 

    def setUp(self):

        # create a User
        self.testuser = User.objects.create_superuser('test',
                                                      'test@example.com',
                                                      'testpass')

        # Every test needs a client.
        self.page = create_page('Test Page', 'test.html', 'en', slug='/',
                                created_by=self.testuser)
        placeholder = self.page.placeholders.get(slot='slot')
        add_plugin(placeholder, 'NVD3CMSPlugin', 'en',
                   xdata=' 1, 2, 3', ydata='5,6,7; 8,9,10',
                   ynames='one curve, two curve', chart_type='lineChart')
        publish_page(self.page, self.testuser, 'en')
        self.client = Client()
        self.response = self.client.get('/')
        self.content = str(self.response.content)

    def test_localnvd3(self):
        print(settings.NVD3_CSS)
        self.assertIn('nvd3plugin', self.content)
