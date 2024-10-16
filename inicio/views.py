from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from django.shortcuts import render, redirect
from inicio.models import Auto
from inicio.forms import CrearAutoFormulario, BuscarAutoFormulario

def mi_vista(request):
    return HttpResponse('Hola soy la vista')

def inicio(request):
    # return HttpResponse('<h1>Soy la pantalla de inicio </h1>')
    return render(request, 'inicio/index.html')

def vista_datos1(request, nombre):
    nombre_mayuscula = nombre.upper()    
    return HttpResponse(f'Hola {nombre_mayuscula}!!')

def primer_template(request):
    
    # sin with
    # archivo_del_template = open(r'templates\primer_template.html')
    # template = Template(archivo_del_template.read())
    # archivo_del_template.close()
    
    # con with
    with open(r'templates\primer_template.html') as archivo_del_template:
        template = Template(archivo_del_template.read())
        
    contexto = Context()
    
    render_template = template.render(contexto)
    
    return HttpResponse(render_template)


def segundo_template(request):
    
    fecha_actual = datetime.now()
    datos ={
        'fecha_actual': fecha_actual,
        'numeros': list(range(1, 11))
    }
    
    
    
    # v1
    # with open(r'templates\segundo_template.html') as archivo_del_template:
    #     template = Template(archivo_del_template.read())
    # contexto = Context(datos)
    # render_template = template.render(contexto)
    
    # v2
    # template = loader.get_template('segundo_template.html')
    # render_template = template.render(datos)
    # return HttpResponse(render_template)
    
    # v3
    return render(request, 'inicio/segundo_template.html', datos)

def crear_auto(request, marca, modelo, anio):
    
     auto = Auto(marca=marca, modelo=modelo, anio=anio)
     auto.save()
     return render(request, 'inicio/creacion_auto_correcta.html', {'auto': auto})
 
def buscar_auto(request):
    
    formulario = BuscarAutoFormulario(request.GET)
    if formulario.is_valid():
        marca = formulario.cleaned_data.get('marca')
        modelo = formulario.cleaned_data.get('modelo') 
        autos = Auto.objects.filter(marca__icontains=marca, modelo__icontains=modelo)
    else:
        autos = Auto.objects.all()

    return render(request, 'inicio/buscar_auto.html', {'autos': autos, 'form': formulario})

def crear_auto(request):

    # print('Request', request)
    # print('GET', request.GET)
    # print('POST', request.POST)
    
    
    formulario = CrearAutoFormulario()
    
    if request.method == 'POST':
        # auto = Auto(marca=request.POST.get('marca'), modelo=request.POST.get('modelo'), anio=request.POST.get('anio'))
        # auto.save()

        formulario = CrearAutoFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            auto = Auto(marca=request.POST.get('marca'), modelo=request.POST.get('modelo'), anio=request.POST.get('anio'))
            auto.save()
            return redirect('inicio:buscar_auto')
            
        
    return render(request, 'inicio/crear_auto.html', {'form': formulario})