from django.shortcuts import render

def index(request):

    return render(request, 'weather/index.html')

def information(request):
    creator_info = {
        'name': 'Имя создателя',
        'bio': 'Краткое описание создателя сайта.',
    }

    context = {
        'creator_info': creator_info
    }
    return render(request, 'weather/index_info.html', context)
