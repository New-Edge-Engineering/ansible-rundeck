<p><img src="https://cdn.xebialabs.com/assets/files/plugins/rundeck.jpg" alt="rundeck logo" title="rundeck" align="right" height="60" /></p>

Ansible Role: rundeck
===================

[![Build Status](https://ci.devops.sosoftware.pl/buildStatus/icon?job=SoInteractive/rundeck/master)](https://ci.devops.sosoftware.pl/blue/organizations/rundeck/SoInteractive%2Frundeck/activity) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/badge/role-rundeck-blue.svg)](https://galaxy.ansible.com/SoInteractive/rundeck/) [![Twitter URL](https://img.shields.io/twitter/follow/sointeractive.svg?style=social&label=Follow%20%40SoInteractive)](https://twitter.com/sointeractive)

Role to install Rundeck with basic configuration (accounts, plugins, system variables)

Example usage
-------------

Use it in a playbook as follows:
```yaml
- hosts: all
  become: true
  roles:
    - SoInteractive.rundeck
```

Have a look at the [defaults/main.yml](defaults/main.yml) for role variables
that can be overridden.