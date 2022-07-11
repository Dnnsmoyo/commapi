

from django.apps import AppConfig,apps


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
    def ready(self):
        from actstream import registry
        registry.register(self.get_model('Community'),apps.get_model('auth.User'))
