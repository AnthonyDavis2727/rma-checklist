from django.shortcuts import render

# Create your views here.
def inputForm(request):
    return render(request, 'input_form.html')