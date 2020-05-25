from django.contrib import admin
from django.urls import path, include
from app import views
# from .views import home

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('detail/<int:pk>/', views.HomeDetailView.as_view(), name='detail_page'),
    path('edit-page', views.OrganisationCreateView.as_view() , name='edit_page'),
    path('update-page/<int:pk>/', views.OrganisationUpdateView.as_view(), name='update_page'),
    path('delete-page/<int:pk>/', views.OrganisationDeleteView.as_view(), name='delete_page'),
    path('login', views.MyprojectLoginView.as_view(), name='login_page'),
    path('register', views.RegisterUserView.as_view(), name='register_page'),
    path('logout', views.MyprojectLogout.as_view(), name='logout_page'),


]
