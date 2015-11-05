from django.test import TestCase

from cms.api import add_plugin
from cms.models import Placeholder

from cmsplugin_nvd3.cms_plugins import NVD3CMSPlugin
from cmsplugin_nvd3.models import NVD3model

class MypluginTests(TestCase):
    
    def test_plugin_context(self):
        placeholder = Placeholder.objects.create(slot='test')
        model_instance = add_plugin(
            placeholder,
            MyPlugin,
            'en',
        )
        plugin_instance = model_instance.get_plugin_class_instance()
        context = plugin_instance.render({}, model_instance, None)
        self.assertIn('key', context)
        self.assertEqual(context['key'], 'value')

    def test_plugin_html(self):
        placeholder = Placeholder.objects.create(slot='test')
        model_instance = add_plugin(
            placeholder,
            MyPlugin,
            'en',
        )
        html = model_instance.render_plugin({})
        self.assertEqual(html, '<strong>Test</strong>')