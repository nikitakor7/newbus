# encoding: utf-8
from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now


@python_2_unicode_compatible
class BusNo(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'BusNo'
        verbose_name_plural = 'BusNos'
        ordering = ['name']

    def __str__(self):
        return self.name


class PublicBusInfoManager(models.Manager):
    def get_queryset(self):
        qs = super(PublicBusInfoManager, self).get_queryset()
        return qs.filter(is_public=True)


@python_2_unicode_compatible
class BusInfo(models.Model):
    url = models.CharField('Bus No', max_length=255)
    title = models.CharField('Bus Info', max_length=255)
    latitude = models.CharField('Latitude', max_length=255)
    longitude = models.CharField('Longitude', max_length=255)
    #description = models.TextField('description', blank=True)
    is_public = models.BooleanField('Like My Service?', default=True)
    date_created = models.DateTimeField('date created')
    date_updated = models.DateTimeField('date updated')
    owner = models.ForeignKey(User, verbose_name='owner',
        related_name='BusInfo')
    #BusNos = models.ManyToManyField(Tag, blank=True)

    objects = models.Manager()
    public = PublicBusInfoManager()

    class Meta:
        verbose_name = 'BusInfo'
        verbose_name_plural = 'BusInfo'
        ordering = ['-date_created']

    def __str__(self):
        return '%s (%s)' % (self.title, self.url)

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = now()
        self.date_updated = now()
        super(BusInfo, self).save(*args, **kwargs)
