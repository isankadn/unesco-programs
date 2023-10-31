from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import UnescoProgram
from .forms import UnescoProgramForm



def program_list(request):
    programs = UnescoProgram.objects.all()
    can_add = request.user.has_perm('unesco_programs.can_add_program') 
    return render(request, 'program_list.html', {'programs': programs, 'can_add': can_add})


def program_detail(request, program_slug):
    program = get_object_or_404(UnescoProgram, slug=program_slug)
    can_edit = request.user.has_perm('unesco_programs.can_edit_program') 
    return render(request, 'program_detail.html', {'program': program, 'can_edit': can_edit})

@login_required
def add_program(request):
    if not request.user.has_perm('unesco_programs.can_add_program'):
        raise PermissionDenied
    
    if request.method == 'POST':
        form = UnescoProgramForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('program_list')  # Assuming you have a view named 'program_list' to list all programs
    else:
        form = UnescoProgramForm()  
    return render(request, 'add_program.html', {'form': form})

@login_required
def edit_program(request, program_slug):
    if not request.user.has_perm('unesco_programs.can_edit_program'):
        raise PermissionDenied
    program = get_object_or_404(UnescoProgram, slug=program_slug)
    if request.method == 'POST':
        form = UnescoProgramForm(request.POST, request.FILES, instance=program)
        if form.is_valid():
            form.save()
            return redirect('program_detail', program_slug=program.slug) # Assuming this is the correct reverse URL pattern name
    else:
        form = UnescoProgramForm(instance=program)   
    return render(request, 'edit_program.html', {'form': form, 'program': program})


