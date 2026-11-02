import click
import subprocess
import os
from pathlib import Path
import httpx

@click.group()
def cli():
    pass

@cli.command()
@click.option("--host", type=str, default="127.0.0.1")
@click.option("--port", type=str, default=8080)
@click.pass_context
def config(ctx, host, port):
    click.echo(f"This is your host {host}, this is your port {port}")
    ctx.obj = {"host": host, "port": port}
    click.echo(ctx.obj)
    

@cli.group()
def compute():
    pass

@compute.group()
def instances():
    pass


@instances.command()
@click.argument("name")
@click.argument("typ")
@click.pass_context
def startvm(ctx, name, typ):
    httpx.post(f"http://127.0.0.1:8000/instances/{name}/{typ}/startvm")


@instances.command()
def listvm():
    subprocess.run("VBoxManage list vms".split())