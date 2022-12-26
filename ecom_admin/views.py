from django.shortcuts import render

# Create your views here.

def admin_home(request):
    return render(request,'ecom_admin/admin_home.html')

def approve_reseller(request):
    return render(request,'ecom_admin/approve_resellers.html')

def change_password(request):
    return render(request,'ecom_admin/change_password.html')

def register_reseller(request):
    return render(request,'ecom_admin/register_reseller.html')

def admin_login(request):
    
    return render(request,'ecom_admin/admin_login.html')