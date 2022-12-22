# used to intercept the call to the IPXE view and do something different
# if this system is supposed to be a vcenter host.

from .views import ESXiIPXEAPIView

class ESXiProvisionerMiddleware:
  def __init__(self, get_response):
    self.get_response = get_response
  
  def __call__(self, request):
    return self.get_response(request)
    
  def process_view(self, request, view_func, *view_args, **view_kwargs):
    if request.get_full_path().startswith("/ipxe/"):
      # let us intercept this.
      esxi_ipxe = ESXiIPXEAPIView()
      return esxi_ipxe.get(request, None, kwargs=view_kwargs)
