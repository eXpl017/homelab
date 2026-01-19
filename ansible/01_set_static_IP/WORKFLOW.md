## How this playbook works

> Sets current IP as static IP using `systemd-networkd` and disables `NetworkManager`

### Assumptions

- host is a Raspberry Pi OS (Bookworm and onwards), which implies
    - `systemd` is the service manager
    - `NetworkManager` is the network managing service by default

### Working

1. Displays the configured IPv4 configuration
2. Extracts information from the above, so as to be used when setting up a static configuration
3. Displays status of NetworkManager services before attempting to shut them down
    - Below are the services
        - 
4. Stops, Disables and Masks `NetworkManager` services if their states are `running` or `enabled`
5. Creating interface configuration file using template file provided, and values extracted in step 2
6. Copying the file to `/etc/systemd/network/` to be read by `systemd-networkd`
7. Unmask, Enable and Start `systemd-networkd` if its state is not `running`
8. Display `NetworkManager` state after changes
9. Ensure `systemd-networkd` is in `active` state, and display it
