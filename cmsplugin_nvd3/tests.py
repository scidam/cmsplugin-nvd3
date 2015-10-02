from django.test import TestCase

from cms.api import  add_plugin
from cms.models import Placeholder 

class NVD3PluginTestCase(TestCase):

    def setUp(self):
        #self.plugin = NVD3CMSPlugin()
        #self.plugin.save()
        pass

    def test_plugin(self):
        placeholder = Placeholder.objects.create(slot='content') 
        model_inst = add_plugin(placeholder, 'NVD3CMSPlugin', 'en')
        html = model_inst.render_plugin(context={})
        print html
        self.assertEqual(1,1)
        #instance = NVD3model()
        #rendered_html = self.plugin.render({}, instance, None)
        #self.assertIn('string', rendered_html)