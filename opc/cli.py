import click
import subprocess

@click.group()
def cli():
    pass

@cli.group()
def compute():
    pass

@compute.group()
def instances():
    pass


@instances.command()
@click.argument("name")
@click.argument("type")
def startvm(name, type):
    subprocess.run(f"VBoxManage startvm {name} --type={type}".split())


@instances.command()
def listvm():
    subprocess.run("VBoxManage list vms".split())