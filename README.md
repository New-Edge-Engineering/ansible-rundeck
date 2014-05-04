# Ansible Rundeck Role #

Ansible role to make sure rundeck is installed, configured and running.
Feedback, bug-reports, requests, is welcomed and can be done via
[github issues](https://github.com/New-Edge-Engineering/ansible-time/issues).

## Requirements & Dependencies ##
- Tested on Mac OS X with Ansible 1.5.

## Variables

````yaml
rundeck_version: # desired version of rundeck, defaults to 2.0.3-1-GA
rundeck_plugins: # list of plugin urls that are downloaded and installed into the rundeck libext, default is none.
rundeck_domain:  # the domain and tdl that the web application with accessed by, is automatically prefix by rundeck.
````

## License ##

Licensed under the MIT License. See the LICENSE file for details.
