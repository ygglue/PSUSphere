"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from studentorg.views import (HomePageView, 
                              OrganizationList, 
                              OrganizationCreateView, 
                              OrganizationUpdateView, 
                              OrganizationDeleteView, 
                              OrgMemberList, 
                              OrgMemberCreateView, 
                              OrgMemberUpdateView,
                              OrgMemberDeleteView
)
from studentorg import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    path('organization_list', OrganizationList.as_view(), name='organization-list'), 
    path('organization_list/add', OrganizationCreateView.as_view(), name='organization-add'),
    path('organization_list/<pk>',OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization_list/<pk>/delete', OrganizationDeleteView.as_view(), name='organization-delete'),
    path('member_list', OrgMemberList.as_view(), name='member-list'), 
    path('member_list/add', OrgMemberCreateView.as_view(), name='member-add'), 
    path('member_list/<pk>', OrgMemberUpdateView.as_view(), name='member-update'), 
    path('member_list/<pk>/delete', OrgMemberDeleteView.as_view(), name='member-delete'), 
]
