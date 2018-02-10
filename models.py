from django.db import models
from sorl.thumbnail import ImageField

# Create your models here.
class Town(models.Model):
    name = models.CharField(max_length=255)
    lat = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)
    lng = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)
    
    class Meta:
        ordering = ('name',)
    
    def __unicode__(self):
        return self.name

class Achievement(models.Model):
    first_name_middle = models.CharField(max_length=200)
    last_name = models.CharField(max_length=150)
    town = models.ForeignKey(Town)
    date = models.DateField()
    short_description = models.CharField(u'Achievement', max_length=255)
    long_description = models.TextField(u'Achievement in detail',)
    created_on = models.DateTimeField(auto_now_add=True)
    
    @models.permalink
    def get_absolute_url(self):
        return ('achievement_detail', [str(self.id)])
    
    class Meta:
        ordering = ('-date',)
    
    def __unicode__(self):
        return '%s %s' % (self.first_name_middle, self.last_name)

class Image(models.Model):
    achievement = models.ForeignKey(Achievement, null=True, on_delete=models.SET_NULL)
    filename = models.CharField(max_length=135, default='')
    image = ImageField(upload_to='achievement/images', max_length=130)
    alt_text = models.CharField(max_length=205, default='alt text')
    caption = models.TextField(blank=True)
    credit = models.CharField(max_length=225, blank=True)
    photo_type = models.CharField(max_length=50, help_text=u'Horizontal or vertical', blank=True)
    
    def __unicode__(self):
        return self.filename
