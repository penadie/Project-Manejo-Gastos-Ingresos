"""finanzas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.contrib import admin
from django.urls import path
from AppFinanzas import views
from django.contrib.auth import views as auth_views

urlpatterns = [
 # ------------------------- PAG PRINCIPALES -----------------
    path('gastos/', views.gast, name='gastos'),
    path('ingresos/', views.ingre, name='ingresos'),
    path('index/', views.index, name='index'),
    path('moneda/', views.api, name= 'moneda'),
    path('tipoggasto/', views.tipoGasto, name= 'agregar_tipo_gasto'),
    path('agregartipoing/', views.agregarTipoIng, name= 'agregar_tipo_ingreso'),
# -------------------------- GASTOS --------------------------
    path('editgasto/<int:id_gasto>', views.editarGasto),
    path('updategasto/<int:id_gasto>', views.updateGasto),
    path('eliminargasto/<int:id_gasto>', views.eliminarGasto),
# ------------------ Agregar EDITAR Y ELIMINAR TIPOS G -------
    path('eliminartipog/<int:id_tipog>', views.eliminarTipoG),
    path('edittipog/<int:id_tipog>', views.editarTipoG),
    path('updatetipog/<int:id_tipog>', views.updateTipoG),

#--------------------------- INGRESOS ------------------------
    path('editingreso/<int:id_ingreso>', views.editarIngreso),
    path('updateingreso/<int:id_ingreso>', views.updateIngreso),
    path('eliminaring/<int:id_ingreso>', views.eliminarIng),
#-------------- Agregar EDITAR Y ELIMINAR TIPOS ING -----------
    path('eliminartipoing/<int:id_tipoing>', views.eliminarTipoIng),
    path('edittipoing/<int:id_tipoing>', views.editarTipoIng),
    path('updatetipoing/<int:id_tipoing>', views.updateTipoIng),

#-------------------- REGISTRO Y LOGIN USUARIO ---------------
    path('registro/', views.registro,name='register'),
    path('login/', views.ingresoUser, name='login'),
    path('logout/', views.desconexion, name='desconexion'),

#--------------------- RESET CONTRASENNA USUARIO -------------
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name= "reset_password.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="reset_password_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_complete.html"), name="password_reset_complete"),

]
