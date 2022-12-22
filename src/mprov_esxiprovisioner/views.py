# Mainly used if there are API endpoints for this mProv module

from systems.models import NetworkInterface
from systems.serializers import NetworkInterfaceDetailsSerializer
from django.http import HttpResponse
from common.views import MProvView
import platform
from django.shortcuts import render
from django.template.response import TemplateResponse


class ESXiIPXEAPIView(MProvView):
    model = NetworkInterface
    serializer_class = NetworkInterfaceDetailsSerializer
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission
    def get(self, request, format=None, **kwargs):
        ip=""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        # now try to grab the nic for this IP
        queryset = self.model.objects.all()
        ip="172.16.60.1"
        queryset = queryset.filter(ipaddress=ip)
        if queryset.count() == 0:
          # return None to allow the rest of the system to process the requst.
          return None
        
        print(f"PXE from {ip}")
        # we found a nic for this IP, let's grab the system instance.
        system = queryset[0].system

        # and then see if we can grab any related associations to vcenter hosts.
        if system.vchassociation_set.all().count() > 0:
            # we found something
            context = {
                'vchassc':  system.vchassociation_set.all()[0] ,
                'bootserver': platform.node()
            }            
            print(f"Serving ESXi PXE to {ip}")
            return(TemplateResponse(request, "systems/ipxe", context=context, content_type="text/plain" ))
            
        # if we get here, then there doesn't seem to be any VCH Associations, let the normal ipxe code take over. 
        return(None)
        
        # return(render(template_name="ipxe", request=request, context=context, content_type="text/plain" ))
        # pass
