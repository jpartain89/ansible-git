Ansible-Git  [![Build Status](https://travis-ci.org/jpartain89/ansible-role-git.svg?branch=master)](https://travis-ci.org/jpartain89/ansible-role-git)
=========

This installs git through Apt and then clones the repos of your choice.

Role Variables
--------------

The dictionary `git_dir`:
    - `path`: Currently set to `ansible_user_dir` or `$HOME` `/git` - `~/git`
    - `owner`: Currently set to the UID of the person you run ansible as
    - `group`: Currently set to the UID of the person you run ansible as
    - `mode`: Currently set to 0775 for the Directories

`git_cloning`: There are two specific fields needed, `repo` and `dest`, that go on the same line.
    - `repo`: The address of the git repo you want to clone from
    - `dest`: The destination you want the local clone to be at

Example Playbook
----------------

    - hosts: all
      roles:
         - jpartain89.ansible-git

License
-------

BSD

Author Information
------------------

JPartain89
github.com/jpartain89
