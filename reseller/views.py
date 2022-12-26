from django.shortcuts import render

# Create your views here.

def reseller_home(request):
    return render(request,'reseller/reseller_home.html')

def reseller_add_product(request):
    return render(request,'reseller/add_product.html')

def reseller_cancelled_order(request):
    return render(request,'reseller/cancelled_order.html')

def reseller_change_password(request):
    return render(request,'reseller/change_password.html')

def reseller_order_history(request):
    return render(request,'reseller/order_history.html')

def reseller_account(request):
    return render(request,'reseller/reseller_account.html')

def reseller_update_stock(request):
    return render(request,'reseller/update_stock.html')

def reseller_recent_orders(request):
    return render(request,'reseller/recent_orders.html')

def reseller_product_catelogue(request):
    return render(request,'reseller/product_catelogue.html')





