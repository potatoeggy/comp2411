# this is the interface to the app

import typer

app = typer.Typer()

@app.command()
def demo():
    """
    Organize and manage the maintenance, renovation, and
    cleaning activities of the campus. As long as the CMMS is concerned, this administrator works
    like a DBA, but that person is not a worker or manager described in the database.
    """
    typer.echo("Hello world")