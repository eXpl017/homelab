## How this playbook works

> Configures Fail2ban service with SSH jail

### Assumptions

- Configurations specified in `vars` in the yaml file are agreed upon, or should be changed

### Working

1. Install fail2ban on the host
2. Creating config files from templates provided and transfer them to host.
   Below configurations are applied
    - loglevel set to INFO
    - default bantime set to 10m
    - default findtime set to 10m
    - default max retries set to 3
    - ssh bantime set to 1h
    - recidive jail bantime set to 1w
    - recidive jail findtime set to 1d
    - recidive jail max retries set to 5

