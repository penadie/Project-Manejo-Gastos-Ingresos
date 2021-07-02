
from django.db.models import fields
from django.db.models.deletion import SET
from django.forms.models import fields_for_model
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from AppFinanzas.models import *
from AppFinanzas.forms import GastosForm, IngresosForm, CrearUsuarioForm, TipoGForm, TipoIngForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.sessions.models import Session
# Create your views here.


# Cuando nada funcione date un descanso
#---------------------------------------- aPI -----------------------------

@login_required(login_url='login')
def api(request):
    return render(request, 'api.html')


#------------------------------- Index -----------------------------------


@login_required(login_url='login')
def index(request):
    uid= request.user.id
    ingreso = Ingresos.objects.filter(usuarioId=uid)
    gasto = Gastos.objects.filter(usuarioId=uid)
    return render(request,'index.html',{'ingresos':ingreso, 'gastos':gasto})



# Cuando nada funcione date un descanso

#------------------------------------traer gastos------------------------------------

@login_required(login_url='')
def gast(request):
    if request.method == "POST":
        usuid = request.user.id
        tipog = request.POST.get('tipog')
        monto = request.POST.get('monto')
        fecha= request.POST.get('fecha')
        desc= request.POST.get('descripcion')
        data = {
            'monto': monto,
            'fecha':fecha,
            'descripcion':desc,
            'tipog': tipog,
            'usuarioId': usuid
        }
        
        form = GastosForm(data)
        if form.is_valid():
            try:
                form.save()
                return redirect('/gastos')
            except:
                pass
    else:
        uid= request.user.id
        form = GastosForm()
        tipog = TipoG.objects.filter(usuarioid=uid)
        gasto = Gastos.objects.filter(usuarioId=uid)
        return render(request,'gastos.html',{'form':form,'gastos':gasto, 'tigas':tipog})



# Cuando nada funcione date un descanso
#------------------------------------traer ingresos--------------------------

@login_required(login_url='login')
def ingre(request):
    if request.method == "POST":
        usuid = request.user.id
        tipoing = request.POST.get('tipoing')
        monto = request.POST.get('monto')
        fecha= request.POST.get('fecha')
        desc= request.POST.get('descripcion')
        data = {
            'monto': monto,
            'fecha':fecha,
            'descripcion':desc,
            'tipoing': tipoing,
            'usuarioId': usuid
        }
        form = IngresosForm(data)
        if form.is_valid():
            try:
                form.save()
                return redirect('/ingresos')
            except:
                pass
    else:
        uid= request.user.id
        form = IngresosForm()
        ingreso = Ingresos.objects.filter(usuarioId=uid)
        tipoing = TipoIng.objects.filter(usuarioId=uid)
        return render(request,'ingresos.html',{'form':form,'ingresos':ingreso, 'tiposing':tipoing})



# Cuando nada funcione date un descanso
#----------------------------------------views eliminar gastos e ingresos-------------
@login_required(login_url='login')
def eliminarIng(request, id_ingreso):
    ing = Ingresos.objects.get(id=id_ingreso)
    ing.delete()
    return redirect('/ingresos')
    
@login_required(login_url='login')
def eliminarGasto(request, id_gasto):
    gas = Gastos.objects.get(id=id_gasto)
    gas.delete()
    return redirect('/gastos')


# Cuando nada funcione date un descanso
#------------------------------ Registro y loggin de usuarios ------------------------

def registro(request):
    if request.user.is_authenticated:
        return redirect('/index')
    else:
        form = CrearUsuarioForm()
        if request.method == 'POST':
            form = CrearUsuarioForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Usuario creado correctamente '+ user)
                return redirect('/login')
            else:
                messages.info(request,'El usuario ya existe.')
        return render(request,'usuariocrear.html',{'form': form})

def ingresoUser(request):
    if request.user.is_authenticated:
        return redirect('/index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/index')
            else:
                messages.info(request, 'Usuario y/o contrasena incorrecto')
        return render(request,'login.html',{})


# Cuando nada funcione date un descanso
#-------------------------- desconectar -------------------------------

def desconexion(request):
    logout(request)
    return redirect('login')


# Cuando nada funcione date un descanso
#----------------------------- editar y upgradear GASTOS ---------------------------

@login_required(login_url='login')
def updateGasto(request,id_gasto):
    gastos = Gastos.objects.get(id=id_gasto)
    if request.method == "POST":
        usuid = request.user.id
        tipog = request.POST.get('tipog')
        monto = request.POST.get('monto')
        fecha= request.POST.get('fecha')
        desc= request.POST.get('descripcion')
        data = {
            'monto': monto,
            'fecha':fecha,
            'descripcion':desc,
            'tipog': tipog,
            'usuarioId': usuid
        }
        form = GastosForm(data, instance=gastos)
        if form.is_valid():
            form.save()
            return redirect('/gastos')

@login_required(login_url='login')
def editarGasto(request,id_gasto):
    uid = request.user.id
    gast = Gastos.objects.get(id=id_gasto)
    gasto = Gastos.objects.filter(id=id_gasto)
    form = GastosForm(instance=gast)
    tipog = TipoG.objects.filter(usuarioid=uid)
    return render(request,'editar_gasto.html',{'form': form,'id_gasto':id_gasto, 'gastoedit':gasto, 'tiposg':tipog})



# Cuando nada funcione date un descanso
#----------------------------- editar y upgradear INGREWSOS ---------------------------
@login_required(login_url='login')
def updateIngreso(request,id_ingreso):
    ing = Ingresos.objects.get(id=id_ingreso)
    if request.method == "POST":
        usuid = request.user.id
        tipoing = request.POST.get('tipoing')
        monto = request.POST.get('monto')
        fecha= request.POST.get('fecha')
        desc= request.POST.get('descripcion')
        data = {
            'monto': monto,
            'fecha':fecha,
            'descripcion':desc,
            'tipoing': tipoing,
            'usuarioId': usuid
        }
        form = IngresosForm(data, instance=ing)
        if form.is_valid():
            form.save()
            return redirect('/ingresos')

@login_required(login_url='login')
def editarIngreso(request,id_ingreso):
    uid = request.user.id
    ingre = Ingresos.objects.get(id=id_ingreso)
    ingreso = Ingresos.objects.filter(id=id_ingreso)
    form = IngresosForm(instance=ingre)
    tipoing = TipoIng.objects.filter(usuarioId=uid)
    return render(request,'editar_ingreso.html',{'form': form,'id_ingreso':id_ingreso, 'ingresoedit':ingreso, 'tiposing':tipoing})


# Cuando nada funcione date un descanso
#------------------------- AGREGAR TIPO DE GASTO -------------------------------


@login_required(login_url='login')
def tipoGasto(request):
    if request.method == "POST":
        usuid = request.user.id
        tipog = request.POST.get('tipog')
        data = {
            'tipog':tipog,
            'usuarioid':usuid,
        }

        form = TipoGForm(data)
        if form.is_valid():
            try:
                form.save()                
                return redirect('/tipoggasto')
            except:
                pass
    else:
        uid= request.user.id
        tipog = TipoG.objects.filter(usuarioid=uid)
        return render(request,'tipogasto.html',{'tipog':tipog})


# Cuando nada funcione date un descanso
#---------------------------------- AGREAR TIPO INGRESO -----------------------------
@login_required(login_url='login')
def agregarTipoIng(request):
    if request.method == "POST":
        usuid = request.user.id
        tipoin = request.POST.get('tipoing')
        # form = TipoIngForm(request.POST)
        data = {
            'tipoing':tipoin,
            'usuarioId':usuid,
        }

        form = TipoIngForm(data)
        if form.is_valid():
            try:
                form.save()
                return redirect('/agregartipoing')
            except:
                pass
    else:
        uid= request.user.id
        tipoing = TipoIng.objects.filter(usuarioId=uid)
        return render(request,'tipo_ingreso.html',{'tipoing':tipoing})



# Cuando nada funcione date un descanso
#--------------------------------- EDITAR Y ELIMINAR TIPO GASTO ----------------------------


@login_required(login_url='login')
def eliminarTipoG(request, id_tipog):
    tipog = TipoG.objects.get(id=id_tipog)
    tipog.delete()
    return redirect('/tipoggasto')

@login_required(login_url='login')
def updateTipoG(request,id_tipog):
    ing = TipoG.objects.get(id=id_tipog)
    if request.method == "POST":
        usuid = request.user.id
        tipog = request.POST.get('tipog')
        data = {
            'tipog': tipog,
            'usuarioid': usuid
        }
        form = TipoGForm(data, instance=ing)
        if form.is_valid():
            form.save()
            return redirect('/tipoggasto')

@login_required(login_url='login')
def editarTipoG(request,id_tipog):
    tipogas = TipoG.objects.get(id=id_tipog)
    tipog = TipoG.objects.filter(id=id_tipog)
    form = TipoGForm(instance=tipogas)
    return render(request,'edit_tipog.html',{'form': form,'id_tipog':id_tipog, 'tipogedit':tipog})




# Cuando nada funcione date un descanso
#---------------------------------- EDITAR Y ELIMINAR TIPO INGRESO -------------------------

@login_required(login_url='login')
def eliminarTipoIng(request, id_tipoing):
    tipoing = TipoIng.objects.get(id=id_tipoing)
    tipoing.delete()
    return redirect('/agregartipoing')
    

@login_required(login_url='login')
def updateTipoIng(request,id_tipoing):
    ing = TipoIng.objects.get(id=id_tipoing)
    if request.method == "POST":
        usuid = request.user.id
        tipoing = request.POST.get('tipoing')
        data = {
            'tipoing': tipoing,
            'usuarioId': usuid
        }
        form = TipoIngForm(data, instance=ing)
        if form.is_valid():
            form.save()
            return redirect('/agregartipoing')

@login_required(login_url='login')
def editarTipoIng(request,id_tipoing):
    tipoingre = TipoIng.objects.get(id=id_tipoing)
    tipoing = TipoIng.objects.filter(id=id_tipoing)
    form = TipoIngForm(instance=tipoingre)
    return render(request,'edit_tipo_ing.html',{'form': form,'id_tipoing':id_tipoing, 'tipoingedit':tipoing})
