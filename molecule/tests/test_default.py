def test_hosts_file_exists(host):
    f = host.file('/etc/hosts')
    assert f.exists
