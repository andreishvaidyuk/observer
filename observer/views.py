from django.shortcuts import render, get_object_or_404, redirect
from observer.models import Student, Section, Group, Filial
from .forms import StudentForm, SectionForm, GroupForm, FilialForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(
        request,
        'observer/index.html',
    )


# методы обработки Филиалов
@login_required()
def filial_list(request):
    # выбираются филиалы, принадлежащие текущему пользователю
    filials = Filial.objects.filter(owner=request.user)
    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits + 1
    return render(
        request,
        'observer/filial_list.html',
        {'filials': filials, 'num_visits': num_visits}
    )


def add_filial(request):
    if request.method == "POST":
        form = FilialForm(request.POST)
        if form.is_valid():
            filial = form.save(commit=False)
            # полю Owner присваивается текущий пользователь
            filial.owner = request.user
            filial = form.save()
            return redirect('filial_detail', pk=filial.pk)
    else:
        form = FilialForm()
    return render(
        request,
        'observer/add_filial.html',
        {'form': form}
    )


def filial_detail(request, pk):
    filial = get_object_or_404(Filial, pk=pk)
    return render(
        request,
        'observer/filial_detail.html',
        {'filial':filial}
    )


def edit_filial(request, pk):
    filial = get_object_or_404(Filial, pk=pk)
    if request.method == "POST":
        form = FilialForm(request.POST, instance=filial)
        if form.is_valid():
            filial = form.save()
            return redirect('filial_detail', pk=filial.pk)
    else:
        form = FilialForm(instance=filial)
    return render(
        request,
        'observer/add_filial.html',
        {'form': form}
    )


# методы обработки Направлений учебы
@login_required()
def section_list(request):
    # выбираются секции (направления занятий), принадлежащие текущему пользователю
    sections = Section.objects.filter(owner=request.user)
    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits + 1
    return render(
        request,
        'observer/section_list.html',
        {'sections': sections, 'num_visits': num_visits}
    )


def add_section(request):
    if request.method == "POST":
        form = SectionForm(request.POST)
        if form.is_valid():
            section = form.save(commit=False)
            # полю Owner присваивается текущий пользователь
            section.owner = request.user
            section = form.save()
            return redirect('section_detail', pk=section.pk)
    else:
        form = SectionForm()
    return render(
        request,
        'observer/add_section.html',
        {'form': form}
    )


def section_detail(request, pk):
    section = get_object_or_404(Section, pk=pk)
    return render(
        request,
        'observer/section_detail.html',
        {'section':section}
    )


def edit_section(request, pk):
    section = get_object_or_404(Section, pk=pk)
    if request.method == "POST":
        form = SectionForm(request.POST, instance=section)
        if form.is_valid():
            section = form.save()
            return redirect('section_detail', pk=section.pk)
    else:
        form = SectionForm(instance=section)
    return render(
        request,
        'observer/add_section.html',
        {'form': form}
    )


# методы обработки Групп обучения
@login_required()
def group_list(request):
    # выбираются группы, принадлежащие текущему пользователю
    groups = Group.objects.filter(owner=request.user)
    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits + 1
    return render(
        request,
        'observer/group_list.html',
        {'groups': groups, 'num_visits': num_visits}
    )


def add_group(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            # полю Owner присваивается текущий пользователь
            group.owner = request.user
            group = form.save()
            return redirect('group_detail', pk=group.pk)
    else:
        form = GroupForm()
    return render(
        request,
        'observer/add_group.html',
        {'form': form}
    )


def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk)
    return render(
        request,
        'observer/group_detail.html',
        {'group':group}
    )


def edit_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == "POST":
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            group = form.save()
            return redirect('group_detail', pk=group.pk)
    else:
        form = GroupForm(instance=group)
    return render(
        request,
        'observer/add_group.html',
        {'form': form}
    )


# методы обработки студентов
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