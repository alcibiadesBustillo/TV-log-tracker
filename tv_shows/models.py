from django.db import models
from django.contrib.auth import get_user_model
import datetime
from django.contrib.admin import widgets

# Create your models here.

# import datetime

# def time_slots(start_time, end_time):
#     t = start_time
#     while t <= end_time:
#         yield t.strftime('%H:%M')
#         t = (datetime.datetime.combine(datetime.date.today(), t) +
#              datetime.timedelta(minutes=15)).time(

# start_time = datetime.time(13, 00)
# end_time = datetime.time(14, 00)
# TIME_CHOICES = list(time_slots(start_time, end_time))

TV_CATEGORY = [
    ('DRAMA', 'Drama.'),
    ('ACTION', 'Action.'),
    ('COMEDY', 'Comedy.'),
    ('CRIME', 'Crime.'),
    ('ADVENTURE', 'Adventure.'),
    ('FANTASY', 'Fantasy.'),
    ('SCIENCE FICTION', 'Science Fiction.'),
    ('SUSPENSE', 'Suspense.'),
    ('THRILLER', 'Thriller.'),
    ('HORROR', 'Horror.'),
    ('ROMANCE', 'Romance.'),
    ('ANIMATION', 'Animation.'),
    ('ANIME', 'Anime.'),
    ('MINI-SERIES', 'Mini-Series.'),
    ('MYSTERY', 'Mistery.'),
    ('FAMILY', 'Family.'),
    ('CHILDREN', 'Chldren.'),
    ('REALITY', 'Realiy.'),
    ('DOCUMENTARY', 'Documentary.'),
    ('SOAP', 'Soap.'),
    ('HISTORY', 'History.'),
    ('SPORT', 'Sport.'),
    ('WESTERN', 'Western.'),
    ('SPECIAL INTEREST', 'Special Interest.'),
    ('GAME SHOW', 'Game Show.'),
    ('TALK SHOW', 'Talk Show.'),
    ('MARTIAL ARTS', 'Martial Arts.'),
    ('FOOD', 'Food.'),
    ('MUSICAL', 'Muscial.'),
    ('WAR', 'War.'),
    ('TRAVEL', 'Travel.'),
    ('NEWS', 'News.'),
    ('HOME AND GARDEN', 'Home and Garden.'),
    ('PODCAST', 'Podcast.'),
    ('INDIE', 'Indie.'),
    

]

class Category(models.Model):
    category = models.CharField(max_length=20, choices=TV_CATEGORY)

    def __str__(self):
        return self.category

class Show(models.Model):
    name = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category, null=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,        
    )    

    def __str__(self):
        return self.name

class Spent(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    date = models.DateField()
    initial_time = models.TimeField()
    final_time = models.TimeField()


    def __str__(self):
        return f'{self.show.author.username}-{self.show.name}'





    