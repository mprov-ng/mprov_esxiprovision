# mprov_esxiprovisioner
![Build Status](https://img.shields.io/github/actions/workflow/status/mprov-ng/mprov_esxiprovision/ci_build.yml?style=plastic)
![Latest Version](https://img.shields.io/pypi/v/mprov_esxiprovisioner.svg)
![Supported Python](https://img.shields.io/pypi/pyversions/mprov_esxiprovisioner.svg)
![Wheel Status](https://img.shields.io/pypi/wheel/mprov_esxiprovisioner.svg)
![License](https://img.shields.io/pypi/l/mprov_esxiprovisioner.svg)

This is an mPCC python module add-on that will allow the mPCC to provision ESXi vm server hosts.


## Installation

To install this module you need to activate your mPCC python env:
```
# cd /var/www/mprov_control_center/
# . bin/activate
```

Then you need to install the pip package for this module.
```
# pip install mprov_esxiprovisioner
```

Once that is installed, you need to add a couple of things to your `/var/www/mprov_control_center/mprov_control_center/settings.py` file.  

First, look for the `INSTALLED_APPS` array and add `mprov_esxiprovisioner` to the end of the python array.

Second, look for the `MIDDLEWARE` array and add `mprov_esxiprovisioner.middleware.ESXiProvisionerMiddleware` to the beginning of that array.

Next, exit your editor and run `touch /var/www/mprov_control_center/mprov_control_center/wsgi.py` to "restart" the wsgi application.

At the command prompt, run `python /var/www/mprov_control_center/manage.py makemigrations mprov_esxiprovisioner` to create the necessary migrations for the plugin.

Once that completes, run `python /var/www/mprov_control_center/manage.py migrate` to create the tables.
