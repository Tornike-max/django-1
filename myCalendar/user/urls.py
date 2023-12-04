from django.urls import path
# from  import views
from user import views

urlpatterns = [
    path('/api/user', views.user_view),
]