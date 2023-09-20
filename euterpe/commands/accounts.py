import typer
import requests
from rich import print

app = typer.Typer()


@app.command()
def create(client_id: str, client_secret):
    body = {"client_id": client_id, "client_secret": client_secret}
    r = requests.post("http://localhost:8000/account/", json=body)
    if r.status_code == 200:
        print("[green]Account created[/green]")
    else:
        print(f"[yellow]Error while creating account {client_id}:[/yellow] {r.reason}")


@app.command()
def list():
    r = requests.get("http://localhost:8000/accounts")
    accounts = r.json()
    print("[blue]Accounts:[/blue]")
    for account in accounts:
        print(f"- {account['client_id']}")


if __name__ == "__main__":
    app()
