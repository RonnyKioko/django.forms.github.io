from django.shortcuts import render, redirect
from crudProject1.models import Student
from crudProject1.forms import StudentForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = StudentForm()
        return render(request, 'index.html', {'form': form})
