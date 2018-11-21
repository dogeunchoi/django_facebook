from django.contrib import admin
from django.urls import path
from facebook.views import play
from facebook.views import play2
from facebook.views import profile
from facebook.views import event
from facebook.views import newsfeed
from facebook.views import detail_feed
from facebook.views import new_feed, edit_feed, remove_feed

urlpatterns = [
    path('admin/', admin.site.urls),

    path('play/', play),
    path('play2/', play2),

    path('dogeunchoi/profile/', profile),

    path('event/', event),

    path('', newsfeed),
    path('feed/<pk>/', detail_feed),
    path('new/', new_feed),
    path('feed/<pk>/edit/', edit_feed),
    path('feed/<pk>/remove/', remove_feed),
]
