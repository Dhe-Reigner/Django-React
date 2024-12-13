from django.urls import path
from BACKEND import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('',views.api_root,name="api-root"),
    path("rooms/",views.RoomList.as_view(),name="room-list"),
    path("rooms/<int:pk>/",views.RoomDetail.as_view(),name="room-detail"),
    path("occupied-dates/",views.OccupiedDatesList.as_view(),name="occupieddate-list"),
    path("occupied-dates/<int:pk>/",views.OccupiedDatesDetail.as_view(),name="occupieddate-detail"),
    path("users/",views.UserList.as_view(),name="users"),
    path("users/<int:pk>/",views.UserDetail.as_view(),name="user-detail"),
    path("login/",views.Login.as_view(),name="login"),
    path("register/",views.Register.as_view(),name="register"),
    
    
    path('room-images/<int:pk>/',views.RoomImageDetail.as_view(),name="roomimage-detail")
]
urlpatterns = format_suffix_patterns(urlpatterns)

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)