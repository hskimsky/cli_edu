import typer
from aipcli import operations

app = typer.Typer(no_args_is_help=True)


@app.command()
def ls():
    """
    List all S3 buckets.
    """
    operations.list_buckets()


@app.command()
def test():
    """
    just print
    """
    print("hello world")


if __name__ == "__main__":
    app()
