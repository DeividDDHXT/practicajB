from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea
from .forms import TareaForm

# Vista para mostrar todas las tareas
def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'tasks/lista_tareas.html', {'tareas': tareas})

# Vista para agregar una nueva tarea
def agregar_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        form = TareaForm()
    return render(request, 'tasks/agregar_tarea.html', {'form': form})

# Vista para editar una tarea
def editar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'tasks/editar_tarea.html', {'form': form})

# Vista para eliminar una tarea
def eliminar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    tarea.delete()
    return redirect('lista_tareas')
