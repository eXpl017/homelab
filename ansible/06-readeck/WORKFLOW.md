## How this playbook works

> Sets up readeck service in a docker container

### Assumptions

- Configurations specified in /readeck-data/config.toml are agreed upon, or should be changed

### Working

1. Create required directies at `/opt`
2. Transfer `docker-compose.yaml` and `config.toml` to above directory
3. Run command `docker compose up -d`
