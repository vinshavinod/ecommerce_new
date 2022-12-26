from django.shortcuts import render,redirect

from customer.models import Customer
from reseller.models import Reseller

# Create your views here.
def customer_home(request):

    if request.method == 'POST':  # when user clicks submit button
        if 'c_signup' in request.POST:  # when customer signup is clicked 
            c_first_name = request.POST['c_fname'] # getting data from firstname textbox, here c_fname is the name attribute of firstname textbox
            c_last_name = request.POST['c_lname']
            c_address = request.POST['c_addrs']
            c_email = request.POST['c_email']
            c_mobile = request.POST['c_phno']
            c_password = request.POST['c_passwd']

            # in ORM, if we want to insert data into a table, 

            # 1. create an object of model class by passing values

            customer = Customer(
                first_name = c_first_name, 
                last_name = c_last_name,
                address = c_address,
                email = c_email,
                mobile = c_mobile,
                password = c_password)

                # 2. call save method 
            customer.save() # save() is equivalent to insert into tablename sql query

        if 'c_login' in request.POST:
            email = request.POST['c_user_id']
            password = request.POST['c_user_passwd']

            try:
                customer = Customer.objects.get(email = email, password = password)  # select * from tablename wher email = email and password = password
                request.session['c_id'] = customer.id

            except:
                error_msg = 'Invalid username or password'
                return render(request, 'customer/customer_home.html',{'error_msg':error_msg})


        if 's_signup' in request.POST:
            name = request.POST['s_name']
            address = request.POST['s_address']
            email = request.POST['s_email']
            mobile = request.POST['s_mobile']
            ac_holdername =  request.POST['s_acholder']
            ac_number = request.POST['s_account']
            ifsc = request.POST['s_ifsc']
            photo = request.FILES['s_pic']
            password = request.POST['s_password']

            reseller = Reseller(
                s_name = name, 
                address = address, 
                email = email, 
                mobile = mobile, 
                account_holder_name = ac_holdername, 
                account_number = ac_number,
                ifsc = ifsc, 
                upload_image = photo,
                password = password )

            reseller.save()

        if 'signin' in request.POST:
            s_email = request.POST['s_mail']
            s_password = request.POST['s_pass']
            print('data')

            try:

                print('test')
                reseller = Reseller.objects.get(email = s_email,password = s_password)#approve
                request.session['s_id'] = reseller.id
                return redirect("reseller:reseller_home")# redirect is used to redirect to html page in another module "here reseller module"
            except:
                error_msg = 'invalid username or password'
                return render(request,'customer/customer_home.html',{'error_msg':error_msg})


            

    return render(request,'customer/customer_home.html')

def customer_login(request):
    return render(request,'customer/login.html')

def customer_myorder(request):
    return render(request,'customer/myorder.html')

def customer_mywishlist(request):
    return render(request,'customer/my_wishlist.html')

def customer_category(request):
    return render(request,'customer/category.html')

def modal(request):
    return render(request,'customer/login_modal.html')

def login1(request):
    return render(request,'customer/login1.html')

def signup(request):
    return render(request,'customer/signup.html')

def product_details(request):
    return render(request,'customer/product_details.html')

def customer_my_account(request):
    return render(request,'customer/my_account.html')
