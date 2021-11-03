# git remote add origin https://github.com/vitlilg/viceversa-project-1.git
# git branch -M main
# git push -u origin main

from django.shortcuts import render


def home(request):
    return render(request, 'home.html')
