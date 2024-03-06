from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
    def ready(self):
        import main.signals

# We are overridding ready func, in order to activate signals
# Once a User is created, we trigger a signal to create a Userprofile
# You should create a signlas.py in the app,
