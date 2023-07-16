from datetime import datetime, timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecord, OrderForm
from .models import Record, Order_Form

def home(request):
    records = Record.objects.all()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect("home")
        else:
            messages.success(request, "There was an Error, Please try again")
            return redirect('home')
    else:
        return render(request, 'Enquiry_Database/home.html', {'records': records})

def login_user(request):
    messages.success(request, "You have been logged out")

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'Enquiry_Database/register.html', {'form': form})

    return render(request, 'Enquiry_Database/register.html', {'form': form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'Enquiry_Database/record.html', {'customer_record': customer_record})
    else:
        messages.success(request, "You must be logged in to view that page....")
        return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Your record has been deleted")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in")
        return redirect('home')

def add_record(request):
    form = AddRecord(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                record = form.save(commit=False)
                record.step_name_one = "Is Quilified Enquiry"
                record.planned_date_one = datetime.now() + timedelta(hours=1)
                record.timedelay_one = record.planned_date_one - datetime.now()  # Calculate time_delay
                record.step_name_two = "Create Indent"  # Set stepname to "Step One"
                record.planned_date_two = datetime.now() + timedelta(hours=2)
                record.timedelay_two = record.planned_date_two - datetime.now()
                record.save()
                messages.success(request, "Added Record")
                return redirect("home")
        return render(request, 'Enquiry_Database/add_record.html', {'form': form})
    else:
        messages.success(request, "You must be logged")
        return redirect('home')

def update_actual_time(request, pk):
    if request.user.is_authenticated:
        status = Record.objects.get(id=pk)
        status.actual_date_one = datetime.now() if status.actual_date_one else datetime.now()
        status.save()
        messages.success(request, "status update")
        print("All DOne")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in")
        return redirect('home')

def update_actual_time_two(request, pk):
    if request.user.is_authenticated:
        status = Record.objects.get(id=pk)
        status.actual_date_two = datetime.now() if status.actual_date_two else datetime.now()
        status.save()
        messages.success(request, "status update")
        print("All DOne")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in")
        return redirect('home')

def update_record(request, pk):
    current_record = Record.objects.get(id=pk)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddRecord(request.POST, instance=current_record)
            if form.is_valid():
                form.save()
                messages.success(request, "Record has been updated!")
                return redirect('home')
            else:
                messages.error(request, "Form is not valid. Please check the errors.")
        else:
            form = AddRecord(instance=current_record)
        return render(request, 'Enquiry_Database/update_record.html', {'form': form})
    else:
        messages.success(request, "You must be logged in...")
        return redirect('home')


# def order_form_record(request, pk):
#     record = Record.objects.get(id=pk)
#     messages.error(request, "Record does not exist")
#     if request.user.is_authenticated:
#         if request.method == "POST":
#             form = OrderForm(request.POST, instance=record)
#             if form.is_valid():
#                 order_record = form.save(commit=False)
#                 order_record.id = record  # Assign the related Record instance
#                 order_record.step_name_one = "Is Qualified Enquiry"
#                 order_record.planned_date_one = datetime.now() + timedelta(hours=1)
#                 order_record.timedelay_one = order_record.planned_date_one - datetime.now()
#                 order_record.step_name_two = "Create Indent"
#                 order_record.planned_date_two = datetime.now() + timedelta(hours=2)
#                 order_record.timedelay_two = order_record.planned_date_two - datetime.now()
#                 order_record.save()
#                 messages.success(request, "Order Form")
#                 return redirect("home")
#             return render(request, 'order_form_record.html', {'form': form, 'record': record})
#         else:
#             messages.success(request, "You must be logged in")
#     return redirect('home')

def order_form_record(request, unique_key):
    form = OrderForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                record = form.save(commit=False)
                record.step_name_one = "Is Quilified Enquiry"
                record.planned_date_one = datetime.now() + timedelta(hours=1)
                record.timedelay_one = record.planned_date_one - datetime.now()  # Calculate time_delay
                record.step_name_two = "Create Indent"  # Set stepname to "Step One"
                record.planned_date_two = datetime.now() + timedelta(hours=2)
                record.timedelay_two = record.planned_date_two - datetime.now()
                record.unique_key = record.planned_date_two - datetime.now()
                record.unique_key = unique_key
                record.save()
                messages.success(request, "Added Record")
                return redirect("home")
            else:
                form = OrderForm(initial={'unique_key': unique_key})  # Pass the unique_key as initial data

        return render(request, 'order_form_record.html', {'form': form})
    else:
        messages.success(request, "You must be logged")
        return redirect('home')


def order(request):
    records = Order_Form.objects.all()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect("home")
        else:
            messages.success(request, "There was an Error, Please try again")
            return redirect('home')
    else:
        return render(request, 'Enquiry_Database/home.html', {'records': records})
