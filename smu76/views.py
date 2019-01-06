from django.shortcuts import render


def main_page(request):
    return render(request, 'smu76/index.html')