import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_consul_service_enabled_and_running(host):
    s = host.service('consul')

    assert s.is_enabled
    assert s.is_running


def test_consul_http_port(host):
    iface = host.interface("eth0").addresses
    s = host.socket("tcp://%s:8500" % iface[0])
    assert s.is_listening


def test_consul_rpc_port(host):
    iface = host.interface("eth0").addresses
    s = host.socket("tcp://%s:8300" % iface[0])
    assert s.is_listening


def test_consul_dns_port(host):
    iface = host.interface("eth0").addresses
    s = host.socket("udp://%s:8600" % iface[0])
    assert s.is_listening


def test_consul_serf_port(host):
    iface = host.interface("eth0").addresses
    s = host.socket("tcp://%s:8301" % iface[0])
    assert s.is_listening


def test_consul_members(host):
    host.run_test("/usr/local/bin/consul members")
