from django.shortcuts import render
from .forms import ProductModelForm
from django.contrib import messages
from .models import Product
# Create your views here.
def product(request):
    modelform=ProductModelForm
    data={'modelform':modelform}
    if request.method=='POST':
       product_form=modelform(request.POST)
       if product_form.is_valid():
           product_form.save()
           messages.success(request,('Hey! You have successfully Done'))
       else:
             messages.success(request,('Hey! Form is invalid please check')) 
    return render(request,'product\product.html',data)
def Product_Report(request):
    Form_data=Product.objects.all() #Retreiving All Data From product(Database)
    data_Form={'Form_data':Form_data}
    return render(request,'product\product_details.html',data_Form)

def Update(request,id):
    Form_data=Product.objects.get(id=id)
    update_form=ProductModelForm(instance=Form_data)
    update_data={'update_form':update_form}
    if request.method=='POST':
        update_form=ProductModelForm(request.POST,instance=Form_data)
        if update_form.is_valid: 
           update_form.save()
           messages.success(request,('Hey! You have successfully Updated'))
        else:
             messages.success(request,('Hey! Form is invalid please check number'))
    return render(request,'product\product_update.html',update_data)