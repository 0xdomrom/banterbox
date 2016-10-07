from rest_framework.authtoken import views as auth_views
from django.conf.urls import url, include
from rest_framework import routers
from . import views

roomPattern = "(?P<room_id>[0-9a-f]{32})"
router = routers.DefaultRouter()

urlpatterns = [

    
    url(r'^api/room/'+roomPattern+r'/pause/?$',        views.pause_room), #pauses the room for 5 minutes
    url(r'^api/room/'+roomPattern+r'/comment/?$',      views.comment),
    url(r'^api/room/'+roomPattern+r'/update/?$',       views.get_update),
    url(r'^api/room/'+roomPattern+r'/blacklist/?$',    views.blacklist),
    url(r'^api/room/'+roomPattern+r'/settings/?$',     views.room_settings),
    url(r'^api/room/'+roomPattern+r'/run/?$',          views.run),

    url(r'^api/user/?$', views.current_user),
    url(r'^api/rooms/?$', views.get_rooms),

    url(r'^api/room/' + roomPattern + r'/pause/?$', views.pause_room),  # pauses the room for 5 minutes
    url(r'^api/room/' + roomPattern + r'/comment/?$', views.comment),
    url(r'^api/room/' + roomPattern + r'/update/?$', views.get_update),
    url(r'^api/room/' + roomPattern + r'/blacklist/?$', views.blacklist_users),
    url(r'^api/room/' + roomPattern + r'/settings/?$', views.room_settings),

    url(r'^$', views.index, name='index'),
    url(r'^api/', include(router.urls)),
    url(r'^docs/', include('rest_framework_docs.urls')),
]
