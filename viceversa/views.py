# git remote add origin https://github.com/vitlilg/viceversa-project-1.git
# git branch -M main
# git push -u origin main

from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reverse(request):
    user_text = request.GET['usertext']
    reversed_text = user_text[::-1]
    return render(request, 'reverse.html', {'usertext': user_text, 'reversedtext': reversed_text})
