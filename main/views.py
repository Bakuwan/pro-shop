from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect
from main.forms import ProductForm
from main.models import ProductEntry

def show_main(request):
    product_entries = ProductEntry.objects.all()
    context = {
        'app_name' : 'Pro Shop',
        'name': 'Fadhli Raihan Ardiansyah',
        'class': 'PBP D',
        'products' : product_entries,
    }
    return render(request, "main.html", context)

def create_product_entry(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)

def show_xml(request):
    data = ProductEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = ProductEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = ProductEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ProductEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

