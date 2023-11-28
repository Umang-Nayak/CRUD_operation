import sys

from django.shortcuts import render, redirect

from CRUD.forms import EmployeeForm
from CRUD.models import Employee


# Create your views here.


def show(request):
    e = Employee.objects.all()
    return render(request, "index.html", {'emp': e})


def insert_page(request):
    return render(request, "Insert_Data.html")


def destroy_Employee(request, eid):
    ei = Employee.objects.get(e_id=eid)
    ei.delete()
    return redirect("/main")


def update_Employee(request, ei):
    eid = Employee.objects.get(e_id=ei)
    form = EmployeeForm(request.POST, instance=eid)
    if form.is_valid():
        form.save()
        return redirect("/main")
    return render(request, 'Update_Data.html', {'eid': eid})


def insert_Employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/main')
            except:
                print('------------------------', sys.exc_info())

    else:
        form = Employee()

    return render(request, 'Insert_Data.html', {'form': form})

