from django.apps import AppConfig


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'

    def ready(self):
        # Makes sure the Job scheduler runs every time the server starts
        from jobs import updater
        updater.start()
