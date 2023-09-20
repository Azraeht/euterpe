# Euterpe API

* Get spotify `CLIENT_ID` and `CLIENT_SECRET` from https://developer.spotify.com/

## Configure Raspberry

### Prerequisites

You must:
- Have a Raspberry Pi setup and configured to be accessible through ssh under `raspberry` with a sudoer user
- Ensure it's connected to a speaker

### Install Raspotify

* Installation
```
> cd ansible
> ansible-playbook -i inventory/realm euterpe.yml --diff
```
