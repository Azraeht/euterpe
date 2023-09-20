import typer
from commands import accounts
from commands import server

app = typer.Typer()
app.add_typer(accounts.app, name="accounts")
app.add_typer(server.app, name="server")


if __name__ == "__main__":
    app()
