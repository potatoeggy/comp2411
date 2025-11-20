from typer import Typer

app = Typer()

@app.command()
def admin():
    """
    Organize and manage the maintenance, renovation, and
    cleaning activities of the campus. As long as the CMMS is concerned, this administrator works
    like a DBA, but that person is not a worker or manager described in the database.
    """
    pass