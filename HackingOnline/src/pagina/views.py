from django.shortcuts import render

# Create your views here.

from .forms import cmsmap

import os

def inicio(request):

	return render(request, "inicio.html", {})


def plataforma(request):

	form = cmsmap(request.POST or None)

	if form.is_valid():

		form_data = form.cleaned_data

		website = form_data.get("website")

		print ("Estos son los datos obtenidos -> {0}").format(website)

		output = os.popen("cd herramientas/cmsmap && python cmsmap.py -t %s" %(website)).read()

		return render(request, "plataforma.html", {"output":output, "cmsmap":form,})




	return render(request, "plataforma.html", {"cmsmap":form,})