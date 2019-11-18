import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


# def test_hosts_file(host):
#     f = host.file('/etc/hosts')

#     assert f.exists
#     assert f.user == 'root'
#     assert f.group == 'root'

def test_rundeck_is_installed(host):
    rundeck = host.package("rundeck")
    assert rundeck.is_installed


def test_rundeck_running_and_enabled(host):
    rundeck = host.service("rundeckd")
    assert rundeck.is_running
    assert rundeck.is_enabled


def test_rundeck_listening_http(host):
    socket = host.socket('tcp://127.0.0.1:4440')

    assert socket.is_listening


def test_rundeck_user_authentication(host):
    command = """curl --digest -L -D - http://localhost:4440/login \
                -u ansible:ansible"""

    cmd = host.run(command)

    assert 'HTTP/1.1 200 OK' in cmd.stdout
