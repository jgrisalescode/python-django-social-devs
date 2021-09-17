from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    # Is necesary to connect the separated signals file
    def ready(self):
        import users.signals
