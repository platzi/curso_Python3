import click


@click.group()
def clients():
    """Manages the clients lifecycle"""
    pass


@clients.command()
@click.pass_context
def create(ctx, name, company, email, position):
    """Creates a new client"""
    pass


@clients.command()
@click.pass_context
def list(ctx):
    """List all clients"""
    pass


@clients.command()
@click.pass_context
def update(ctx, client_uid):
    """Updates a single client"""
    pass


@clients.command()
@click.pass_context
def delete(ctx, client_uid):
    """Deletes a client"""
    pass


@clients.command()
@click.pass_context
def search(ctx, query):
    """Searches for a client"""
    pass


all = clients
