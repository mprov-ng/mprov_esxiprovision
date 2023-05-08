# used to intercept the call to the IPXE view and do something different
# if this system is supposed to be a vcenter host.

from .views import ESXiIPXEAPIView
import mprov_control_center.urls 
from django.urls import path
from systems.views_noauth import IPXEAPIView


class ESXiProvisionerMiddleware:
  def __init__(self, get_response):
    self.get_response = get_response
    # append the '/tramp/' url to the recognized patterns. 
    # we will process it below.
    mprov_control_center.urls.urlpatterns.append(
      path('tramp/', IPXEAPIView.as_view()),
    )
  
  def __call__(self, request):
    return self.get_response(request)
    
  def process_view(self, request, view_func, *view_args, **view_kwargs):
    if request.get_full_path().startswith("/ipxe/") or request.get_full_path().startswith("/tramp"):
      # let us intercept this.
      esxi_ipxe = ESXiIPXEAPIView()
      return esxi_ipxe.get(request, None, kwargs=view_kwargs)
