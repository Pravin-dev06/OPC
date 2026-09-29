from .vm import startvm, listvm
import click

@click.group()
def cli():
    pass

@click.command()
@click.argument("name")
@click.argument("typ")
def start(name, typ):
    startvm(name, typ)

@click.command()
def list():
    listvm()

cli.add_command(start, name="startvm")
cli.add_command(list, name="listvm")