from django.db import models #import the models from django

class Data(models.Model): #make a class and define the type of values that are store into the database table
	sr = models.IntegerField()
	facilityname = models.CharField(max_length = 100)
	country = models.CharField(max_length = 25)
	synchrotron = models.IntegerField()
	beamline = models.IntegerField()

	def __unicode__(self): #there are string and integer both values, "return self.sr" will not work here
		return "{0}, {1}, {2}, {3}, {4}".format(self.sr, self.facilityname, self.country, self.synchrotron, self.beamline)
#		return self.sr


# Create your models here.
