import testinfra.utils.ansible_runner
from time import time

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_service_running_and_enabled(Service):
    assert Service('docker-registry').is_running
    assert Service('docker-registry').is_enabled


def test_docker_registry(Command, Sudo):
    with Sudo():
        localimage = 'localhost:5000/busybox:%d' % time()

        Command.check_output('docker pull busybox:latest')
        Command.check_output('docker tag busybox:latest %s', localimage)
        Command.check_output('docker push %s', localimage)
        Command.check_output('docker rmi busybox:latest')
        Command.check_output('docker rmi %s', localimage)

        images1 = Command.check_output(
            'docker images --format %s', '{{ .Repository }}:{{ .Tag }}')
        assert images1 == 'registry:2'

        out = Command.check_output('docker run --rm %s id', localimage)
        assert out == 'uid=0(root) gid=0(root) groups=10(wheel)'

        images2 = Command.check_output(
            'docker images --format %s', '{{ .Repository }}:{{ .Tag }}')
        assert sorted(images2.split()) == [localimage, 'registry:2']
        # Clean up in case we re-run the test
        Command.check_output('docker rmi %s', localimage)
