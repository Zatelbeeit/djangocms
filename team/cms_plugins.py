from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from .models import TeamPluginModel

@plugin_pool.register_plugin
class TeamPlugin(CMSPluginBase):
    model = TeamPluginModel
    name = "ze team"
    render_template = "team.html"