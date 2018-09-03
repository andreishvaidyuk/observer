from django.shortcuts import render, get_object_or_404, redirect
from observer.models import Student
from .forms import StudentForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(
        request,
        'observer/index.html',
    )


@login_required()
def student_list(request):
    # выбираются студенты, принадлежащие текущему пользователю
    students = Student.objects.filter(owner=request.user)
    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits + 1
    return render(
        request,
        'observer/student_list.html',
        {'students': students, 'num_visits': num_visits}
    )


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(
        request,
        'observer/student_detail.html',
        {'student':student}
    )


def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            # полю Owner присваивается текущий пользователь
            student.owner = request.user
            student = form.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm()
    return render(
        request,
        'observer/add_student.html',
        {'form': form}
    )


def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)
    return render(
        request,
        'observer/add_student.html',
        {'form': form}
    )


def delete_student(request, pk):
    student = get_object_or_404(Student,pk=pk)
    student.delete()
    return redirect('student_list')