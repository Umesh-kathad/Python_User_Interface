from django.shortcuts import render 

from app2.forms import DataForm #import the class name that we have created in forms.py
from app2.models import Data #import the class name that we have created in models.py
from django.http import HttpResponseRedirect 
from django.http import HttpResponse 
from django.template import Context, loader

def viewdata(request): #define a function
	if request.method == "POST": #check if the requested method is the POST

		form = DataForm(request.POST) #retrieve form object

		snum = request.POST.get('snum','') #store the form input value in a variable 
		facility = request.POST.get('facility','')
		country = request.POST.get('country','')
		synchrotron = request.POST.get('synchrotron','')
		beamline = request.POST.get('beamline','')

		data_obj = Data(sr = snum, facilityname = facility, country = country, synchrotron = synchrotron, beamline = beamline)
		data_obj.save() #to save the input data in database

		return HttpResponseRedirect('/retrieve') # once data is stored, it will redirect user to retrieve page

	else:
		form = DataForm() #if something wrong, it will not display retrieve page

		return render(request, "viewdata.html", {	
			'form': form,
		})


def retrievedata(request): #view for /retrive page
	data_list = Data.objects.all() #to retrieve all objects data that have been entered
	t = loader.get_template('retrievedata.html')
	c = Context({'data_list': data_list,})
	return HttpResponse(t.render(c))

# Create your views here.
