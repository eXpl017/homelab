## How this playbook works

> Hardens SSH Server

### Assumptions

- `config_list` variable contains things used to harden the server, hence must be agreed upon or changed

### Working

1. Creates backup of current `/etc/ssh/sshd_config` at `/etc/ssh/sshd_config.bak`
    - this could result in overwriting of any file with same name
2. Edits below config changes
    - Disallows empty password logins
    - Disallows root logins
    - Only specified users allowed
    - Runs on port 2222
    - Allows password authentication
    - Allows public key authentication
    - Max authentication retries set to 3
    - Disallows TCP forwarding
    - Authorized keys stored at `/etc/ssh/ansible/authorized_keys`
