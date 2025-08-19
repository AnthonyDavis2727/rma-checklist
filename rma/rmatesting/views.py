from django.shortcuts import render
from .forms import InputForm

# Create your views here.
def inputForm(request):
    context = {}
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            # Process the form data
            context['success'] = True
    else:
        form = InputForm()
    context['form'] = form
    return render(request, 'input_form.html', context)