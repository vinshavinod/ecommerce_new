from django.urls import path
from .import views

app_name = 'customer'

urlpatterns = [
    path('',views.customer_home,name='home'),
    path('login',views.customer_login,name='login'),
    path('myorder',views.customer_myorder,name='myorder'),
    path('my_wishlist',views.customer_mywishlist,name='mywhishlist'),
    path('modal',views.modal,name='modal'),
    path('login1',views.login1,name='login1'),
    path('signup',views.signup,name='signup'),
    path('product_details',views.product_details,name='productdetails'),
    path('my_account',views.customer_my_account,name='myaccount'),
    
]