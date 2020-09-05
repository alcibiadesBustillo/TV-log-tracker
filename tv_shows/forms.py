from django import forms
from django.forms import ModelForm

from .models import Spent, Show, Category


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
class ShowForm(ModelForm):
    # name = forms.CharField(max_length = 100)
    # categories = forms.ModelMultipleChoiceField(
    #             widget = forms.CheckboxSelectMultiple,
    #             queryset = Category.objects.all()
    #       )  
    
    class Meta:
        model = Show        
        fields = ('name', 'categories',)

        widgets = {
            'categories': forms.CheckboxSelectMultiple(),
        }
    
        