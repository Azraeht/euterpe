# Euterpe API

[![CI](https://github.com/Azraeht/euterpe/actions/workflows/ci.yml/badge.svg)](https://github.com/Azraeht/euterpe/actions/workflows/ci.yml)

Euterpe is a random and useless but fun project which aims to provide a simple NFC reader  triggering Spotify songs.


# Setup

## Spotify

* Create an `Euterpe` app on [Spotify](https://developer.spotify.com/)
* Get spotify `CLIENT_ID` and `CLIENT_SECRET`

## Configure Raspberry

### Prerequisites

You must:
- Have a Raspberry Pi setup and configured to be accessible through ssh under `raspberry` with a sudoer user
- A RC522 card connected on the Raspberry
- Ensure it's connected to a speaker

### RC522 setup

Here is a wiring plan of the RC522 card on your Raspberry
![Alt text](https://raw.githubusercontent.com/azraeht/euterpe/main/.assets/Raspberry-wiring-RC522.png)

### Install Raspotify

* Installation
```
> cd ansible
> ansible-playbook -i inventory/realm euterpe.yml --diff
```

# Run it!

* Start the API
```
> uvicorn euterpe.api:app --reload
```
* Run the server
```
> python euterpe/cli.py server run
```

# Develop

In order to ease development you may run source directly from your Raspberry PI. You can use VSCode Remote Developpement to achieve that.

* Run VSCode
* `<Ctrl + Shift + P>` then `Remote-SSH: Connect current Window to Remote host`
* Select your `raspberry` host
* When the window is ready `Clone Repository`
