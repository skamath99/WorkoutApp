from django.shortcuts import render, redirect

from core.models import Routine, Exercise, StrengthHistory

'''
    ROUTINES
'''


def view_routines(request):
    routines = Routine.objects.all()
    return render(request, 'core/view_routines.html', {'routines': routines})


def select_routine(request):
    if request.method == 'GET':
        routine = Routine.objects.get(pk=request.GET.get('routine_pk'))
        exercises_raw = Exercise.objects.filter(routine=routine)
        exercises = {}
        for exercise in exercises_raw:
            sets = StrengthHistory.objects.filter(exercise=exercise).order_by('-order')
            exercises[exercise] = sets[:exercise.sets]

        context = {
            'routine': routine,
            'exercises': exercises
        }
    else:
        context = None
    return render(request, 'core/selected_routine.html', context)


def create_routine(request):
    if request.method == 'POST':
        Routine.objects.create(
            name=request.POST.get('routine_name')
        )
        return redirect('core:view_routines')
    if request.method == 'GET':
        return render(request, 'core/create_routine.html')
