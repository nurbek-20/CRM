from django.urls import path
from . import views

urlpatterns = [
    path('apartment_list/', views.ApartmentListView.as_view()),
    path('apartment_update/<int:pk>/', views.ApartmentUpdateView.as_view()),
    path('apartment_delete/<int:pk>/', views.ApartmentDeleteView.as_view()),

    path('manager_list/', views.ManagerListView.as_view()),
    path('manager_update/<int:pk>/', views.ManagerUpdateView.as_view()),
    path('manager_delete/<int:pk>/', views.ManagerDeleteView.as_view()),
]
