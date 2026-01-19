## How the playbook works

> Installs Docker Engine

### Assumptions

- Trying to install docker on the system for the first time
    - follow instructions for uninstalling docker from their website


### Working

1. Uninstall unofficial packages, and containerd and runc to avoid conflicts, as they come built in with docker engine
2. Created required directories with permissions, getting GPG keys and adding repo to apt source list
3. Updating apt cache and installing docker packages
4. Getting and displaying docker process state
