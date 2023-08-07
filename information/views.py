from django.shortcuts import render

def information(request):
    creator_info = {
        'name': 'Имя создателя',
        'bio': 'Краткое описание создателя сайта.',
    }

    context = {
        'creator_info': creator_info
    }
    return render(request, 'information.html', context)
