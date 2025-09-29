Ansible-Git
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

```bash
  - name: Git
    hosts: all
    roles:
      - jpartain89.ansible-git
```

License
-------

BSD

Author Information
------------------

JPartain89
github.com/jpartain89

Molecule tests
---------------

This role includes a minimal `molecule/default` scenario for smoke-testing the role.

To run locally (from repo root):

```bash
pipenv install --dev
pipenv shell
cd personal_ansible_plays/roles/jpartain89.git
molecule test --scenario-name default
```

The converge play is conservative by default and performs only safe, non-destructive checks. Inspect `molecule/default/converge.yml` to see which variables are set for testing.
