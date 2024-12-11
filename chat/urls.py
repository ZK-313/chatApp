# from django.urls import path

# from . import views

# urlpatterns = [
#     path("", views.index, name="index"),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat, name = 'chat'),
    path('<str:room_name>/', views.chat_room, name='chat_room'),
    # path('', views.chat, name='chat'),
]