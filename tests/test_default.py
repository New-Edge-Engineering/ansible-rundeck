import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_directories(File):
    present = [
        "/var/lib/rundeck",
        "/var/rundeck"
    ]
    for directory in present:
        d = File(directory)
        assert True
        assert d.is_directory
        assert d.exists


def test_packages(Package):
    present = [
        "rundeck"
    ]
    for package in present:
        p = Package(package)
        assert p.is_installed
