from django.apps import AppConfig


class LeadsConfig(AppConfig):
    name = 'leads'
    def ready(self):
        from fetchLeads import updater
        updater.start()
