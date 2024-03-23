"""
URL configuration for WOMENSAFTY project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import *
from app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path("registration/admin",AdminRegistrationView.as_view(),name="admin-registrations"),
    path("user/registration",UserRegistrationView.as_view(),name="user-registrations"),
    path("police/registration",PoliceRegistrationView.as_view(),name="police-registrations"),
    path("userindex",UserIndexView.as_view(),name="userindex"),
    path("policeindex",PoliceIndexView.as_view(),name="policeindex"),
    path("adminindex",AdminIndexView.as_view(),name="adminindex"),
    path("userprofile",UserprofileAddView.as_view(),name="userprofile"),
    path("userupdate/<int:pk>/change/",UpdateUserProfileView.as_view(),name="userupdate"),
    path("userlist/<int:pk>",UserListView.as_view(),name="userlist"),
    # path("policeprofile",PoliceprofileAddView.as_view(),name="policeprofile"),
    path("complaint",ComplaintView.as_view(),name="complaint"),
    path("complaintlist/<int:pk>",ComplaintListView.as_view(),name="complaintlist"),
    path("complaintlist/admin",AdminComplaintListView.as_view(),name="admin-complaintlist"),


    path("saftytips/",SaftytipsView.as_view(),name='safty_tips'),
    path("saftytipsview/",SafetyTipListView.as_view(),name="saftytipsview"),
    path("policeupdate/<int:pk>/change/",PoliceUpdateView.as_view(),name="police-update"),
    path("policedelete/<int:pk>/remove/",PoliceDeleteView.as_view(),name="police-delete"),
    path("policelist/<int:pk>",policestationListView.as_view(),name="policelist"),
    path("approve_complaint/<int:pk>",approve_complaint,name="approve_complaint"),
    path("checkcomplaints",UserComplaintListView.as_view(),name="checkcomplaint"),
    path("user/<int:pk>/",SpecifiedUser.as_view(),name="specifieduser"),
    path('sos/', sos_view, name='sos'),
    path('search/', search_view, name='search'),
    path('users/', AdminUserListView.as_view(), name='all_users'),
    path('send-alert/', views.send_alertview, name='send_alert'),
    path('alert-sent/', views.alert_sentview, name='alert_sent'),
    path('view-alerts/', views.view_alertsview, name='view_alerts'),
    path('view-alerts/', views.view_alerts, name='view_alerts'),
    



    path("login",LoginView.as_view(),name="signin"),
    path("logout",signoutView.as_view(),name="logout")

]  + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
