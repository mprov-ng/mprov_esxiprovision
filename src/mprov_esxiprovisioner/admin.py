# Used to build the UI components for mProv using Django
from systems.admin import SystemAdmin
from systems.models import System
from mprov_esxiprovisioner.models import VCHAssociation, VcenterHost
from django.contrib import admin
from django.forms import ModelForm

class ESXiProvisioner(admin.TabularInline):
  model = VCHAssociation
  extra = 1
  max_num = 1
  verbose_name = "vCenter Provisioning"
  verbose_name_plural = "vCenter Provisioning"

class ESXiServer(admin.ModelAdmin):
  model = VcenterHost
  def get_model_perms(self, request): 
    return {}

class ESXiProvForm(ModelForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
admin.site.register(VcenterHost, ESXiServer)
admin.site._registry[System].inlines.append(ESXiProvisioner)