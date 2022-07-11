"""saascomm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('',views.home_view),
    path('pricing',views.pricing),
    path('api/communities',views.CommunityList.as_view()),
    path('api/posts',views.PostList.as_view(),name='post_api'),
    path('api/activity',views.ActionList.as_view(),name='act_api'),
    path('group/<pk>/', views.CommDetailView.as_view(),name="group_detail"),   
    path("register/", views.UserCreate.as_view(), name="register"),  # <-- added
    path('ajax-posting/', views.ajax_posting, name='ajax_posting'),# ajax-posting / name = that we will use in ajax url
    path('admin/', admin.site.urls),
]
