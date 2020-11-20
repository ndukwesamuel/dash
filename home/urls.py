from django.urls import path
from . import views 


urlpatterns = [

    path('', views.home, name="home"),
    path('product/', views.product, name="product"),
    path('create_ord/', views.create_ord, name="create_ord"),
    path('update_ord/<str:id_test>/', views.update_ord, name="update_ord"),
    path('delete_form/<str:id_test>/', views.delete_form, name="delete_form"),

    path('customer/<str:id_test>', views.customer, name='customer')

]