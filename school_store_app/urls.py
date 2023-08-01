from django.urls import path
from school_store_app import views

app_name = "school_store_app"

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('form_page/', views.form_page, name='form_page'),
    path('ajax/load-courses/', views.load_courses, name='ajax_load_courses'),  # AJAX
]
