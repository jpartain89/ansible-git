def test_git_is_installed(host):
    '''Verify that git is installed on the system.'''
    git = host.package('git')
    assert git.is_installed


def test_git_lfs_is_installed(host):
    '''Verify that git-lfs is installed on the system.'''
    git_lfs = host.package('git-lfs')
    assert git_lfs.is_installed


def test_git_path_exists(host):
    '''Verify the git directory was created by the role.'''
    git_path = host.file('/root/git')
    assert git_path.exists
    assert git_path.is_directory
