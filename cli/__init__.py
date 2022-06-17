import click

from cli.check_mongodb import check_mongodb


@click.group()
@click.pass_context
def cli(ctx):
    pass


cli.add_command(check_mongodb, "check_mongodb")
