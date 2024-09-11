from django.shortcuts import render

def show_main(request):
    context = {
        'app_name' : 'Pro Shop',
        'name': 'Fadhli Raihan Ardiansyah',
        'class': 'PBP D',
    }
    return render(request, "main.html", context)