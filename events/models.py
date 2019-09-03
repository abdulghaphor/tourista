from django.db import models

class Language(models.Model):
	name = models.CharField(max_length=250)

class Event(models.Model):
	create_date = models.DateField(auto_now_add=True)
	def __str__(self):
		lang = Language.objects.get(name='en')
		temp = self.title.get(language=lang)
		return "id: %s" % (temp)

class EventTitle(models.Model):
	title = models.CharField(max_length=250)
	language = models.ForeignKey(Language,on_delete=models.CASCADE)
	event = models.ForeignKey(Event,on_delete=models.CASCADE,related_name="title")
	def __str__(self):
		return self.title

class EventDate(models.Model):
	start = models.DateField()
	end = models.DateField()
	event = models.ForeignKey(Event, on_delete=models.CASCADE,related_name="dates")

	def __str__(self):
		return "%s - %s" % (self.start, self.end)

class EventLocation(models.Model):
	address = models.TextField()
	language = models.ForeignKey(Language,on_delete=models.CASCADE)
	date = models.ForeignKey(EventDate, on_delete=models.CASCADE,related_name="location")
	event = models.ForeignKey(Event, on_delete=models.CASCADE,related_name="location")

	def __str__(self):
		return "%s on %s - %s" % (self.event, self.start, self.end)

class EventPoster(models.Model):
	image = models.ImageField()
	event = models.ForeignKey(Event, on_delete=models.CASCADE,related_name="posters")
	def __str__(self):
	 	return "Image for %s" % (self.event)

class EventPosterDescription(models.Model):
	description = models.TextField()
	language = models.ForeignKey(Language,on_delete=models.CASCADE)
	poster = models.ForeignKey(Event,on_delete=models.CASCADE,related_name="description")
	def __str__(self):
		return self.event