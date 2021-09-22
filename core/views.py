from django.contrib import messages
from django.shortcuts import redirect, render
import bcrypt
from .decorators import login_required,admin_requerido


@login_required
def index(request):

    context = {
        'saludo': 'Hola'
    }
    return render(request, 'dashboard.html', context)

@admin_requerido
def administrador(request):

    context = {
        'saludo': 'Hola!'
    }
    return render(request, 'admin.html', context)

