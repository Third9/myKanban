from django.shortcuts import render

# Create your views here.


def index(request):
    print('index call')
    return render(request, 'kanban/index.html', {})