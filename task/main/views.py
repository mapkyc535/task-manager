from django.shortcuts import render, redirect
from .models import Tasks
from .forms import ViewTaskForm, AddTaskForm, StatusTaskForm


def index(request):
    title = 'задачи'
    #сперва идут не сделанные задачи
    list_task1 = Tasks.objects.filter(status=False).order_by('date_of_completion')
    list_task2 = (Tasks.objects.filter(status=True).order_by('date_of_completion'))
    return render(request, 'main/index.html', {'title': title, 'list2': list_task2, 'list1': list_task1})


def add(request):
    title = 'новая задача'
    message = False
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add')
        else:
            message = 'Данные были введены некорректно'
    else:
        form = AddTaskForm()
    return render(request, 'main/add.html', {'title': title, 'form': form, 'message': message})


def search(request):
    title = 'поиск'
    #пока месседж ложный он не будет отображаться
    message = False
    if request.method == 'POST':
        formm = ViewTaskForm(request.POST)
        if formm.is_valid():
            id = formm.cleaned_data.get('number')
            if Tasks.objects.filter(pk=id).exists():
                task = Tasks.objects.get(pk=id)
            else:
                task = False
                message = 'Такой задачи не существует'
    else:
        task = False
    form = ViewTaskForm()
    return render(request, 'main/search.html', {'title': title, 'form': form, 'item': task, 'message': message})


def perform(request):
    title = 'выполнить задачу'
    message = False
    if request.method == 'POST':
        form = StatusTaskForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data.get('id')
            #проверка существует ли такая задача
            if Tasks.objects.filter(pk=id).exists():
                status = form.cleaned_data.get('status')
                Tasks.objects.filter(pk=id).update(status=status)
                return redirect('perform')
            else:
                message = 'Такой задачи не существует'
                form = StatusTaskForm()
    else:
        form = StatusTaskForm()
    return render(request, 'main/perform.html', {'title': title, 'form': form, 'message': message})


def delete(request):
    title = 'удалить задачу'
    message = False
    if request.method == 'POST':
        form = ViewTaskForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data.get('number')
            #проверка существует ли такая задача
            if Tasks.objects.filter(pk=id).exists():
                Tasks.objects.filter(pk=id).delete()
                form = ViewTaskForm()
                message = 'Задача была удалена'
            else:
                form = ViewTaskForm()
                message = 'Такой задачи не существует'
        else:
            form = ViewTaskForm()
            message = 'Данные были введены некоректно'
    else:
        #так как существующая форма подходит была использованна она
        form = ViewTaskForm()
    return render(request, 'main/delete.html', {'title': title, 'form': form, 'message': message})