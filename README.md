# Euterpe API

Euterpe is a random and useless but fun project which goals it to provide a simple NFC reader which trigger Spotify songs.


# Setup

## Spotify

* Create an `Euterpe` app on [Spotify](https://developer.spotify.com/)
* Get spotify `CLIENT_ID` and `CLIENT_SECRET`

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
