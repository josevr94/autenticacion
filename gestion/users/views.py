from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.decorators import permission_required, login_required

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.groups.add(request.POST.get('group'))
            login(request,user)
            return redirect('home')
    else:
        form = UserCreationForm()   
    return render(request,'register.html', {'form': form})     


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
    return render(request,'login.html',{'error':'Credenciales invalidas'})    


@permission_required('users.view_ventas',raise_exception=True) # esta linea es la que limita que otros usuarios tengan acceso a paginas q no tienen usuario
def ventas_view(request):
    return render(request,'ventas.html', {'title': 'Ventas'})

@permission_required('users.view_compras',raise_exception=True) # si estoy logeado en ventas, no podre ver el menu de compras, eso es gracias a estos decoradores
def compras_view(request):
    return render(request, 'compras.html',{'title':'Compras'})

@permission_required('users.view_inventarios',raise_exception=True)
def inventario_view(request):
    return render(request, 'inventario.html',{'title':'Inventario'})

@permission_required('users.view_reportes', raise_exception=True)
def reportes_view(request):
    return render(request,'reportes.html',{'title': 'Reportes'})

@permission_required('users.view_finanzas',raise_exception=True)
def finanzas_view(request):
    return render('users.view_finanzas','finanzas.html',{'title':'Finanzas'})

@login_required
def logout_view(request):
    logout(request)
    return render(request,'logout.html')

@login_required
def home(request):
    user = request.user
    context = {
        'can_view_ventas' : user.has_perm('users.view_ventas'),
        'can_view_compras' : user.has_perm('users.view_compras'),
        'can_view_inventarios' : user.has_perm('users.view_inventarios'),
        'can_view_reportes' : user.has_perm('users.view_reportes'),
        'can_view_finanzas' : user.has_perm('users.view_finanzas')
    }
    return render(request,'home.html',context)

def custom_403_view(request, exception):
    return render(request, '403.html', status=403)



# Create your views here.
