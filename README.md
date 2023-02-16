# mprov_esxiprovision
This is an mPCC python module add-on that will allow the mPCC to provision ESXi vm server hosts.


## Installation

To install this module you need to activate your mPCC python env:
```
# cd /var/www/mprov_control_center/
# . bin/activate
```

Then you need to install the pip package for this module.
```
# pip install mprov_esxiproviioner
```

Once that is installed, you need to add a couple of things to your `/var/www/mprov_control_center/mprov_control_center/settings.py` file.  

First, look for the `INSTALLED_APPS` array and add `mprov_esxiprovisioner` to the end of the python array.

Second, look for the `MIDDLEWARE` array and add `mprov_esxiprovisioner.middleware.ESXiProvisionerMiddleware` to the beginning of that array.

Lastly, exit your editor and run `touch /var/www/mprov_control_center/mprov_control_center/wsgi.py` to "restart" the wsgi application.
