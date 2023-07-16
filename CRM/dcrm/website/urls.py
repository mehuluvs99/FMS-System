from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('order_form_record/<str:unique_key>', views.order_form_record, name='order_form_record'),
    path('update_actual_time/<int:pk>', views.update_actual_time, name='update_actual_time'),
    path('update_actual_time_two/<int:pk>', views.update_actual_time_two, name='update_actual_time_two'),
    # path('customer/<int:pk>', views.customer_record, name='customer_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('order_form/', views.order, name='order'),

]
