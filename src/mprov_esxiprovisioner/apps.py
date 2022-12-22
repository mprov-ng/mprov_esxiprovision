# Describes this "App" or mProv section, to Django
from django.apps import AppConfig

class ESXiProvisioner(AppConfig):
  default_auto_field = 'django.db.models.BigAutoField'
  name = 'mprov_esxiprovisioner'
  verbose_name = "ESXi Provisioning"
  