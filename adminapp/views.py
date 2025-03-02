from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from . import services


def login_required_decorator(func):
    return login_required(func, login_url='login_page')


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect("login_page")


def login_page(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request, user)
            return redirect("home_page")

    return render(request, 'login.html')


@login_required_decorator
def home_page(request):
    faculties = services.get_faculties()
    kafedras = services.get_kafedra()
    ctx = {
        'counts': {
            'faculties': len(faculties),
            'kafedras': len(kafedras),
        }
    }
    return render(request, 'index.html', ctx)


@login_required_decorator
def faculty_create(request):
    model = Faculty()
    form = FacultyForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('faculty_list')
    ctx = {
        "form": form
    }
    return render(request, 'faculty/form.html', ctx)


@login_required_decorator
def faculty_edit(request, pk):
    model = Faculty.objects.get(pk=pk)
    form = FacultyForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('faculty_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'faculty/form.html', ctx)


@login_required_decorator
def faculty_delete(request, pk):
    model = Faculty.objects.get(pk=pk)
    model.delete()
    return redirect('faculty_list')


@login_required_decorator
def faculty_list(request):
    faculties = services.get_faculties()
    print(faculties)
    ctx = {
        "faculties": faculties
    }
    return render(request, 'faculty/list.html', ctx)


# KAFEDRA
@login_required_decorator
def kafedra_create(request):
    model = Kafedra()
    form = KafedraForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('kafedra_list')
    ctx = {
        "form": form
    }
    return render(request, 'kafedra/form.html', ctx)


@login_required_decorator
def kafedra_edit(request, pk):
    model = Kafedra.objects.get(pk=pk)
    form = KafedraForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('kafedra_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'kafedra/form.html', ctx)


@login_required_decorator
def kafedra_delete(request, pk):
    model = Kafedra.objects.get(pk=pk)
    model.delete()
    return redirect('kafedra_list')


@login_required_decorator
def kafedra_list(request):
    kafedras = services.get_kafedra()
    ctx = {
        "kafedras": kafedras
    }
    return render(request, 'kafedra/list.html', ctx)


@login_required_decorator
def guruh_created(request):
    model = Guruh()
    form = GuruhForm(request.POST or None,instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('guruh_list')

    stx = {
        "form":form
    }
    return render(request,'Guruh/form.html',stx)


@login_required_decorator
def guruh_edit(request,pk):
    model = Guruh.objects.get(pk=pk)
    form = GuruhForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('guruh_list')

    stx = {
        "form": form,
        "model":model
    }
    return render(request, 'guruh/form.html', stx)


@login_required_decorator
def guruh_delete(request,pk):
    model = Guruh.objects.get(pk=pk)
    model.delete()
    return redirect('guruh_list')


@login_required_decorator
def guruh_list(request):
    guruhs = services.get_guruh()

    stx = {
        "guruhs": guruhs
    }
    return render(request,'guruh/list.html',stx)


@login_required_decorator
def subject_created(request):
    model = Subject()
    form = SubjectForm(request.POST or None,instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('subject_list')

    stx = {
        "form":form
    }
    return render(request,'subject/form.html',stx)


@login_required_decorator
def subject_edit(request,pk):
    model = Subject.objects.get(pk=pk)
    form = SubjectForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('subject_list')

    stx = {
        "form": form,
        "model":model
    }
    return render(request, 'subject/form.html', stx)


@login_required_decorator
def subject_delete(request,pk):
    model = Subject.objects.get(pk=pk)
    model.delete()
    return redirect('subject_list')


@login_required_decorator
def subject_list(request):
    subjects = services.get_subject()

    stx = {
        "subjects": subjects
    }
    return render(request,'subject/list.html',stx)


