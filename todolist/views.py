from django.shortcuts import render, redirect

from .models import Todolist

from .forms import TodoListForm

from django.views.decorators.http import require_POST

# Create your views here.

def index(request):
    return render(request,'todolist/index.html')
