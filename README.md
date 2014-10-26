# Ansible Rundeck Role

This is an [Ansible](http://www.ansible.com/) role to installed, configured and to ensure sure rundeck is running.
Feedback, bug-reports, requests, is welcomed and can be done via [github issues](https://github.com/New-Edge-Engineering/ansible-time/issues).

## Execution Requirements
- Tested on Mac OS X with Ansible 1.7 .

## Role Variables

The following variables can be overridden:

 * `rundeck_domain`: Defaults to localhost but should the host name web application with accessed by.
 * `rundeck_database_type`: Defaults to hsqldb but can be set to postgresql (or mysql, coming soon) to those databases. Users and databases are not automatically created.
 * `rundeck_database_port`: Defaults to None and only needs to be set if using a different port than the default database type.
 * `rundeck_database_name`: Defaults to rundeck but allows you to use a different rundeck database name.
 * `rundeck_database_user`: Defaults to rundeck but allows you to use a different rundeck database username that accesses the rundeck database.
 * `rundeck_database_pass`: Defaults to rundeck but allows you to use a different rundeck database password that the user access to the rundeck database.
 * `rundeck_users`: A list of dictionaries of name, password ([hashed](http://rundeck.org/docs/administration/authenticating-users.html#propertyfileloginmodule)) and a list of roles (One must be an admin). If empty the default admin is not removed.
 * `rundeck_plugins`: A list of plugin urls that are downloaded and installed into the rundeck libext, default is none.


## Dependencies
This role does not have a hard dependency on any other role to deploy but rundeck does require java to be installed. smola.java role is a good choice with the
following configuration:

 * **Debian:** Ensure java_packages has a debian java package in it, i.e. openjdk-7-jre-headless
 * **RedHat:** Ensure java_packages has a debian java package in it, i.e. java-1.7.0-openjdk, had to adjust role to include RedHat.yml in main.yml to work.

## License

Licensed under the MIT License. See the LICENSE file for details.
