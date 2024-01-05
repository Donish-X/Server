"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from server_app.views import SportsmensList, GroupList, SportsmensByGroupAPIView,  SportsmenDetailsAPIView, AuthView, register_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sportsmens/', SportsmensList.as_view(), name='sportsmens-list'),
    path('groups/', GroupList.as_view(), name='group-list'),
    path('api/sportsmens_by_group/', SportsmensByGroupAPIView.as_view(), name='sportsmens-by-group-api'),
    path('api/sportsmen_details/', SportsmenDetailsAPIView.as_view(), name='sportsmen-details-api'),
    path('api/token/', AuthView.as_view(), name='auth-token'),
    path('api/register_user/', register_user, name='register-user'),
    

]
