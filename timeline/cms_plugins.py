from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from .models import TimelinePluginModel

@plugin_pool.register_plugin
class HelloPlugin(CMSPluginBase):
    model = TimelinePluginModel
    name = "the super timeline foufou"
    render_template = "timeline.html"
    
