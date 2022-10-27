from django.shortcuts import render


def index_view(request):
    return render(request, 'index.html')

def second_view(request):
    return render(request, 'second_page.html')

def third_view(request):
    return render(request, 'third_page.html')


