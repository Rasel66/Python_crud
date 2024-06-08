from django.shortcuts import render, redirect, get_object_or_404
from student.models import Student

def home(request):
    std = Student.objects.all()
    return render(request, 'student/home.html',{'std':std})

def add_student(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            roll = request.POST.get('roll')
            phone = request.POST.get('phone')
            address = request.POST.get('address')

            s = Student()
            s.name = name
            s.email = email
            s.roll = roll
            s.phone = phone
            s.address = address

            s.save()

            return redirect('/student/home/')
    except:
        pass
    return render(request, 'student/add_student.html',)

def delete_student(request, roll):
    s = Student.objects.get(pk=roll)
    s.delete()

    return redirect('/student/home/')

def update_student(request, roll):
    std = Student.objects.get(pk=roll)
    return render(request, 'student/update_student.html',{'std':std})

def do_update_student(request, roll):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        # Use get_object_or_404 for better error handling
        std = get_object_or_404(Student, pk=roll)
        std.name = name
        std.email = email
        std.phone = phone
        std.address = address
        std.save()

        return redirect('/student/home/')
    else:
        return redirect('/student/home/')

#Create your views here.
