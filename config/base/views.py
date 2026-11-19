

from django.shortcuts import get_object_or_404, render, redirect
from .models import Employee, Trash


# Display employees and add a new employee
def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        designation = request.POST.get('designation')
        department = request.POST.get('department')

        Employee.objects.create(
            name=name,
            email=email,
            mobile_number=mobile_number,
            designation=designation,
            department=department
        )

        return redirect('home')

    employees = Employee.objects.all()

    return render(
        request,
        'home.html',
        {'employees': employees}
    )


# Update an employee
def update_employee(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == 'POST':
        employee.name = request.POST.get('name')
        employee.email = request.POST.get('email')
        employee.mobile_number = request.POST.get('mobile_number')
        employee.designation = request.POST.get('designation')
        employee.department = request.POST.get('department')

        employee.save()

        return redirect('home')

    return render(
        request,
        'update.html',
        {'employee': employee}
    )


# Move an employee to Trash
def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)

    Trash.objects.create(
        name=employee.name,
        email=employee.email,
        mobile_number=employee.mobile_number,
        designation=employee.designation,
        department=employee.department
    )

    employee.delete()

    return redirect('home')


# Display deleted employees
def trash_list(request):
    trash_employees = Trash.objects.all()

    return render(
        request,
        'trash.html',
        {'trash_employees': trash_employees}
    )


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')

