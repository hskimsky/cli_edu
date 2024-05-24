import boto3
import typer


def get_s3_client():
    # TODO 차후 configure을 통한 credentials로 대체
    try:
        session = boto3.Session(
            aws_access_key_id="xxx",
            aws_secret_access_key="xxx"
        )
        s3_client = session.client('s3')
        return s3_client
    except Exception as e:
        typer.echo(e)
        raise typer.Exit(code=1)


def list_buckets():
    """
    List all S3 buckets.
    """
    s3_client = get_s3_client()
    try:
        response = s3_client.list_buckets()
        buckets = response.get('Buckets', [])
        if not buckets:
            typer.echo("No S3 buckets found.")
        else:
            typer.echo("S3 Buckets:")
            for bucket in buckets:
                typer.echo(f" - {bucket['Name']}")
    except Exception as e:
        typer.echo(f"An error occurred: {e}")
        raise typer.Exit(code=1)
