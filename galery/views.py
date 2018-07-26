from django.shortcuts import render, redirect
from galery.models import Imagenes

def showimg(request):
    class content(type(Imagenes.objects.all())):
        comment = ""
    img_list = []
    for i in Imagenes.objects.all():
        j = content()
        j.Imagenes_name = i.Imagenes_name
        j.Imagenes_url = i.Imagenes_url
        j.Imagenes_data = i.Imagenes_data
        img_list.append(j)
    return render(request, 'showimg.html', {"IMG": img_list})
