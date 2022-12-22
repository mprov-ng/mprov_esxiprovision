# Defines the DB Models that will be used by this Django App or section of mProv
from django.db import models
from systems.models import System
import sh, os
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import pre_save, pre_delete, post_save


class VcenterHost(models.Model):
  name=models.CharField(max_length=255, verbose_name="vCenter Hostname")
  payload=models.CharField(max_length=4096, verbose_name="Auto Deploy Payload URL")
  #system=models.ForeignKey(System, on_delete=models.CASCADE, null=True)

  def __str__(self) :
    return self.name

class VCHAssociation(models.Model):
  vcenterHost = models.ForeignKey(VcenterHost, null=True, on_delete=models.CASCADE, verbose_name="VCenter Host")
  system = models.ForeignKey(System, on_delete=models.CASCADE, null=True)

@receiver(post_save, sender=VcenterHost)
def DownloadPayload(sender, instance, **kwargs):
  # attempt to grab a copy of the payload.
  try:
    #sh.cd("/tmp/")
    sh.rm("-f", "/tmp/deploy-tftp.zip")
    sh.wget("-P", "/tmp", "--no-check-certificate", f"{instance.payload}")
    sh.mkdir("-p", f"{os.path.join(settings.MEDIA_ROOT, instance.name)}")
    #sh.cd(f"{os.path.join(settings.MEDIA_ROOT, instance.name)}")
    sh.unzip(["-d", f"{os.path.join(settings.MEDIA_ROOT, instance.name)}", "/tmp/deploy-tftp.zip"])
  except Exception as e:
    # if wget fails, payload fails.
    print(f"Error: Unable to get {instance.payload}: {e} ({e.with_traceback})")
    return
  