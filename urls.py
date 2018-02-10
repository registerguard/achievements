from django.conf.urls.defaults import *
from achievements.models import Achievement

achievements_dict = {
    'queryset': Achievement.objects.all(),
}

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.list_detail.object_list', achievements_dict),
    url(r'^(?P<object_id>\d+)$', 'django.views.generic.list_detail.object_detail', achievements_dict, name='achievement_detail'),
)
