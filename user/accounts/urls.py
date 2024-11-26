from django.urls import path
from accounts.views import register, login_view, user_list, chat_window

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('users/', user_list, name='user_list'),
    path('chat/<int:user_id>/', chat_window, name='chat_window'),
]
