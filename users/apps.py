from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'daysiweb.users'
    verbose_name = "Users"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
