from django.urls import URLPattern, path
from .views import CompanyView, ProfileView

urlpatterns = [
    path('companies/',CompanyView.as_view(),name='companies_list'),
    path('companies/<int:id>',CompanyView.as_view(),name='companies_process'),
    path('profile/',ProfileView.as_view(),name='profile_list'),
    path('profile/<int:id>',ProfileView.as_view(),name='profile_process'),
]