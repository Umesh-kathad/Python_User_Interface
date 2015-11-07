from django import forms #import forms from django
#it defines the html form input fields

class DataForm(forms.Form): #make a class and define the type of values that user will enter into the html form
	sr = forms.IntegerField()
	facilityname = forms.CharField()
	country = forms.CharField()
	synchrotron = forms.IntegerField()
	beamline = forms.IntegerField()