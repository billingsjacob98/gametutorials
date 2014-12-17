from django.db import models

class Game(models.Model):

	# Change based on UK/US IP
	RATINGS = (('12', '12'),
		       ('15', '15'),
		       ('18', '18'))

	REVIEWS = (('1', '1 Star'),
			   ('2', '2 Stars'),
			   ('3', '3 Stars'),
			   ('4', '4 Stars'),
			   ('5', '5 Stars'))

	name = models.CharField(max_length=255)
	description = models.TextField()
	release_date = models.DateField()
	publisher = models.CharField(max_length=255)
	game_engine = models.CharField(max_length=255)
	rating = models.CharField(max_length=2, choices=RATINGS)
	review = models.CharField(max_length=1, choices=REVIEWS)
	front_cover = models.ImageField(upload_to='frontcovers', null=True)


	def __str__(self):
		return '%s (%s)' % (self.name, self.release_date.strftime('%Y'))


class Mission(models.Model):
	name = models.CharField(max_length=255)
	number = models.IntegerField()
	video_url = models.URLField()
	game = models.ForeignKey('Game')

	def __str__(self):
		return self.name
