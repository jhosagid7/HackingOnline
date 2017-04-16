from django.shortcuts import render

# Create your views here.

def inicio(request):

	return render(request, "inicio.html", {})


def plataforma(request):

	return render(request, "plataforma.html", {})