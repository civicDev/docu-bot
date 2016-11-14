from django.views.generic.base import TemplateView
from chatterbot.ext.django_chatterbot import views
from .settings import *

class ChatterBotAppView(views.ChatterBotViewMixin, TemplateView):
    template_name = "app.html"
    
    def __init__(self, **kwargs): 
        """
        uncomment this to train the bot. 1 time only.
        trained data in: ..\data\db.sqlite3
        "" "
        train_folder = CHATTERBOT['training_data']
        print('training from folder: ' + train_folder)
        self.chatterbot.train(train_folder)
        "" "
        """
        