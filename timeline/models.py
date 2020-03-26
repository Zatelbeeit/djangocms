from django.db import models
from filer.fields.image import FilerImageField


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    picture = FilerImageField(on_delete=models.CASCADE)
    date = models.DateField()

from cms.models.pluginmodel import CMSPlugin
class TimelinePluginModel(CMSPlugin):
    text = models.CharField(max_length=100)
    events = models.ManyToManyField(Event)

    def copy_relations(self, oldinstance):
        self.events.set(oldinstance.events.all()) 
