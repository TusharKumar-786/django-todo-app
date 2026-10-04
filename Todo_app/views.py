from django.shortcuts import render, redirect
from .models import * 
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('login_page')

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('login_page')
        else:
            login(request, user)
            return redirect('/dashboard')
        
    return render(request, 'login.html')

@login_required(login_url='/')
def update_completed(request, id):
    todo = Todo.objects.get(id=id)

    todo.completed = not todo.completed
    todo.save()

    return redirect('dashboard')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User.objects.filter(username=username)

        if user.exists():
            messages.error(request, 'Already Taken.')
            return redirect('/register/')

        user = User.objects.create(
            username=username,
            email= email,
        )

        user.set_password(password)
        user.save()

        messages.info(request,'Account Created Successfully')
        return redirect('/register/')
    return render(request, 'register.html')

@login_required(login_url='/login/')
def logout_page(request):
    logout(request)
    return redirect('login_page')

@login_required(login_url='/login/')
def dashboard(request):
    queryset = Todo.objects.filter(user = request.user)

    if request.GET.get('search'):
        queryset = queryset.filter(title__icontains = request.GET.get('search'))
        
    context = {'todo': queryset}
    return render(request,'dashboard.html', context)


@login_required(login_url='/login/')
def add_todo(request):
    
    if request.method == 'POST':
            data = request.POST
        
            title = data.get('title')
            description = data.get('description')
            due_date = data.get('due_date')
            priority = data.get('priority')

            Todo.objects.create(
                user=request.user,
                title = title,
                description = description,
                due_date = due_date,
                priority = priority,
            )
            return redirect('/dashboard/')

    return render(request,'add.html')

@login_required(login_url='/login/')
def update_todo(request,id):
    queryset = Todo.objects.get(id = id)

    if request.method == 'POST':
        data = request.POST

        title = data.get('title')
        description = data.get('description')
        due_date = data.get('due_date')
        completed = 'completed' in request.POST
        priority = data.get('priority')

        queryset.title = title
        queryset.description = description
        queryset.due_date = due_date
        queryset.completed = completed
        queryset.priority = priority

        queryset.save()
        return redirect('/dashboard')
    context = {'todo': queryset}
    return render(request,'Update.html', context)

@login_required(login_url='/login/')
def delete_todo(request, id):
    queryset = Todo.objects.get(id = id)
    queryset.delete()
    return redirect('/dashboard/')
