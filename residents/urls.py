# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('create_district_municipality/', views.create_district_municipality, name='create_district_municipality'),
    path('districts/', views.district_municipality_list, name='district_list'),
    path('municipalities/', views.municipality_list, name='municipality_list'),
    path('villages/', views.village_list, name='village_list'),
    path('households/', views.household_list, name='household_list'),
    path('residents/', views.resident_list, name='resident_list'),
    path('details/<int:id>/', views.details, name='details'),
    path('combined/', views.combined_data_view, name='combined_data'),
    path('create_resident/', views.create_resident, name='create_resident'),
    path('create_village/', views.create_village, name='create_village'),
    path('create_municipality/', views.create_municipality, name='create_municipality'),
]
