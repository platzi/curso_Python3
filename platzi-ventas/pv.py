import click

from clients import commands as clients_commands


@click.group()
@click.pass_context
def cli(ctx):
    """An application to manage clients, inventory, sales and produce reports."""
    ctx.obj = {}


cli.add_command(clients_commands.all)
