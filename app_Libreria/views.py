from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor
from django.urls import reverse

# Página de inicio del sistema
def inicio_libreria(request):
    contexto = {
        'titulo': 'Sistema de Administración Libreria AJMG 1194',
    }
    return render(request, 'inicio.html', contexto)

# Agregar autor (muestra formulario y procesa POST)
def agregar_autor(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        nacionalidad = request.POST.get('nacionalidad')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        fecha_fallecimiento = request.POST.get('fecha_fallecimiento') or None
        biografia = request.POST.get('biografia')
        email = request.POST.get('email')
        activo = True if request.POST.get('activo') == 'on' else False

        Autor.objects.create(
            nombre=nombre,
            nacionalidad=nacionalidad,
            fecha_nacimiento=fecha_nacimiento,
            fecha_fallecimiento=fecha_fallecimiento,
            biografia=biografia,
            email=email,
            activo=activo,
        )
        return redirect('ver_autores')

    return render(request, 'autor/agregar_autor.html')

# Ver todos los autores
def ver_autores(request):
    autores = Autor.objects.all()
    return render(request, 'autor/ver_autores.html', {'autores': autores})

# Mostrar formulario de actualización de autor (GET)
def actualizar_autor(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    return render(request, 'autor/actualizar_autor.html', {'autor': autor})

# Procesar la actualización (POST)
def realizar_actualizacion_autor(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    if request.method == 'POST':
        autor.nombre = request.POST.get('nombre')
        autor.nacionalidad = request.POST.get('nacionalidad')
        
        # CORREGIR: Manejar fechas vacías correctamente
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        autor.fecha_nacimiento = fecha_nacimiento if fecha_nacimiento else autor.fecha_nacimiento
        
        fecha_fallecimiento = request.POST.get('fecha_fallecimiento')
        autor.fecha_fallecimiento = fecha_fallecimiento if fecha_fallecimiento else None
        
        autor.biografia = request.POST.get('biografia')
        autor.email = request.POST.get('email') or None  # Permitir email vacío
        autor.activo = True if request.POST.get('activo') == 'on' else False
        
        autor.save()
        return redirect('ver_autores')
    return redirect('actualizar_autor', autor_id=autor_id)

# Borrar autor (confirmación GET + borrado POST)
def borrar_autor(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    if request.method == 'POST':
        autor.delete()
        return redirect('ver_autores')
    return render(request, 'autor/borrar_autor.html', {'autor': autor})
