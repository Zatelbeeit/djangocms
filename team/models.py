from django.db import models
from filer.fields.image import FilerImageField


# Create your models here.
class TeamMember(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    picture = FilerImageField(on_delete=models.CASCADE)
    linkin = models.URLField(max_length=250)
    twitter = models.URLField(max_length=250)
    facebook = models.URLField(max_length=250)

from cms.models.pluginmodel import CMSPlugin
class TeamPluginModel(CMSPlugin):
    text = models.CharField(max_length=100)
    members = models.ManyToManyField(TeamMember)

    def copy_relations(self, oldinstance):
        self.members.set(oldinstance.members.all()) 

# Create your models here.
