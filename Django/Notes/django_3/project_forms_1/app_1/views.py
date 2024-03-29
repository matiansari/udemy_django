from django.shortcuts import render
from app_1 import forms

# Create your views here.
def index(request):
    return render(request, 'app_1/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            #DO SOMETHING
            print('VALIDATION SUCCESS')
            print('Name: ' + form.cleaned_data['name'])
            print('Email: ' + form.cleaned_data['email'])
            print('Text: ' + form.cleaned_data['text'])

    return render(request, 'app_1/form_page.html', {'form':form})
