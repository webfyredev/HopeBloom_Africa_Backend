from django.urls import path
from .import views

urlpatterns = [
    path('volunteers/', views.volunteerView, name ='Volunteer'),
    path('volunteers-list', views.volunteerList, name='VolunteerList'),
    path('partnerships/', views.partnershipView, name='Partnerships'),
    path('partnership-list/', views.partnerships_list, name='Partnership-List'),
    path('donations/', views.donationViews, name='Donations'),
    path('donation-list/', views.donationList, name='Donation-List'),
    path('contacts/', views.contacts, name='Contacts'),
    path('contacts-list/', views.contacts_list, name='Contacts-List'),
]