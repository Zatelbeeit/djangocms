# Generated by Django 2.2.11 on 2020-03-23 11:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('linkin', models.URLField(max_length=250)),
                ('twitter', models.URLField(max_length=250)),
                ('facebook', models.URLField(max_length=250)),
                ('picture', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.CASCADE, to=settings.FILER_IMAGE_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TeamPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='team_teampluginmodel', serialize=False, to='cms.CMSPlugin')),
                ('text', models.CharField(max_length=100)),
                ('members', models.ManyToManyField(to='team.TeamMember')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]