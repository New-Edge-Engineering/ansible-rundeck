# Ansible Rundeck Role

This is an [Ansible](http://www.ansible.com/) role to install, configure and ensure sure rundeck is running.
Feedback, bug-reports, requests are welcomed and can be done via [github issues](https://github.com/New-Edge-Engineering/ansible-time/issues).

## Execution Requirements
- Tested on Mac OS X with Ansible 1.7 .

## Role Variables

The following variables can be overridden:

 * `rundeck_domain`: Defaults to localhost but should the host name web application with accessed by.
 * `rundeck_database_type`: Defaults to hsqldb but can be set to postgresql or mysql to use those databases. Users and databases are not automatically created.
 * `rundeck_database_host`: Defaults to localhost and only needs to be set if using an externally hosted database.
 * `rundeck_database_port`: Defaults to None and must be set if using a different database than the default hsqldb.
 * `rundeck_database_name`: Defaults to rundeck but allows you to use a different rundeck database name.
 * `rundeck_database_user`: Defaults to rundeck but allows you to use a different username to accesses the rundeck database.
 * `rundeck_database_pass`: Defaults to rundeck but allows you to use a different password for the user access to the rundeck database.
 * `rundeck_users`: A list of dictionaries of name, password ([hashed](http://rundeck.org/docs/administration/authenticating-users.html#propertyfileloginmodule)) and a list of roles (One must be an admin). If empty the default admin is not removed.
 * `rundeck_plugins`: A list of plugin urls that are downloaded and installed into the rundeck libext, default is none.
 * `rundeck_generate_ssh`: True  # automatically generate ssh key, set to False to stop this action.


## Dependencies
This role does not have a hard dependency on any other role to deploy but rundeck does require java to be installed. smola's [ansible-java-role](https://github.com/smola/ansible-java-role) is a good choice with the
following configuration:

 * **Debian:** Ensure java_packages has a debian java package in it, i.e. openjdk-7-jre-headless
 * **RedHat:** Ensure java_packages has a debian java package in it, i.e. java-1.7.0-openjdk, had to adjust role to include RedHat.yml in main.yml to work.

If you choose to use a database then please ensure it is installed before executing this role. The following roles have been used to create databases:

 * **Ubuntu 12.04 & 14.04/PostgreSQL:** [postgresql](https://galaxy.ansible.com/list#/roles/512)
 * **Centos 6.5 & 7.0/PostgreSQL:** [postgresql-on-el6](https://galaxy.ansible.com/list#/roles/766) (with tweeks, watch this space for updates)

## License

Licensed under the MIT License. See the LICENSE file for details.
