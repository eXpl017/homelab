# Docker Compose files

- Compose files I use to bring up my services
- Currently, I generate self-signed TLS certs using `mkcert`, will be changing this in the future


## Planned services:

- [x] joplin
- [x] readeck
- [x] pdfding
- [x] vaultwarden
- [ ] freshrss
- [ ] nginx (reverse-proxy for all the above)


## Some issues

- Not all above services' compose suppport docker env vars with `_FILE` suffix for using secrets
    - for now, I have simply stored secret data in `secrets/` folder inside respective dirs
    - this WILL show your secret data in `docker inspect` and in container env vars
    - will be changing this later to directly use secrets in the `entrypoint` scripts

- For joplin, I have hardcoded the username, database and password in the env file
    - THIS IS A HUGE FLAW!
    - its better to pass them as command line options than commit them to a version control
    - ofc, passing them as cli option is bad too, and is a security risk in itself

## Some doubts I need to clear for myself

- `entrypoint` script understanding, so i can edit it enough to be able to pass secrets from there
- what happens when using `env_file` and `environment` together
