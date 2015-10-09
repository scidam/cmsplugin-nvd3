from django.test import TestCase

from cms.api import  add_plugin
from cms.models import Placeholder 
import pdb

class NVD3PluginTestCase(TestCase):

    def setUp(self):
        placeholder = Placeholder.objects.create(slot='content')
        #valid curve names
        self.plugin1 = add_plugin(placeholder, 'NVD3CMSPlugin', 'en')
        self.plugin1.xdata = '1, 2, 3'
        self.plugin1.ydata = '4,5,6; 7,8,9'
        self.plugin1.ynames = 'river, bank'
        self.plugin1.container_name = 'unique'

        #invalid curve names should be defined as default serie+No
        self.plugin2 = add_plugin(placeholder, 'NVD3CMSPlugin', 'en')
        self.plugin2.xdata = '1, 2, 3'
        self.plugin2.ydata = '4,5,6; 7,8,9'
        self.plugin2.ynames = 'river, bank, block'
        self.plugin2.container_name = 'my-unique-container'
        
        #simple pieChart testing
        self.plugin3 = add_plugin(placeholder, 'NVD3CMSPlugin', 'en')
        self.plugin3.pie_colors = 'red, cyan, blue, green'
        self.plugin3.chart_type = 'pieChart'
        self.plugin3.xdata = 'Banana, Strawberry, Orange, Apple'
        self.plugin3.ydata = '10, 40, 60, 70'
        
        #extra arguments
        self.plugin4 = add_plugin(placeholder, 'NVD3CMSPlugin', 'en')
        self.plugin4.attrs = "{'color_list':  ['magenta', 'green', 'orange', 'blue']}"
        self.plugin4.xdata = 'Banana, Strawberry, Orange, Apple'
        self.plugin4.ydata = '10, 40, 60, 70'
        

    def test_simple_plugin1(self):
        html1 = self.plugin1.render_plugin(context={})
        self.assertIn('river', html1)
        self.assertIn('bank', html1)
        self.assertIn('id="nvd3id-', html1)
        
    def test_simple_plugin2(self):
        html2 = self.plugin2.render_plugin(context={})
        self.assertIn('serie 1', html2)
        self.assertIn('serie 2', html2)
        self.assertIn('id="my-unique-container"', html2)
        
    def test_simple_pieChart(self):
        html3 = self.plugin3.render_plugin(context={})
        html4 = self.plugin4.render_plugin(context={})
        print html3
        self.assertIn('Banana', html3)
        self.assertIn('Strawberry', html3)
        self.assertIn('Orange', html3)
        self.assertIn('Apple', html3)
        self.assertIn('magenta', html4)

        
    
    
    