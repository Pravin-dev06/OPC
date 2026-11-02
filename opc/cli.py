import click
import subprocess
import os
from pathlib import Path
import httpx

@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {"host": "127.0.0.1", "port": "8000"}

@cli.command()
@click.option("--host")
@click.option("--port")
@click.pass_context
def config(ctx, host, port):
    click.echo(f"This is your host {host}, this is your port {port}")
    if host: ctx.obj['host'] = host
    if port: ctx.obj['port'] = port
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
def start(ctx, name, typ):
    click.echo(f'this is you host{ctx.obj['host']}')
    httpx.post(f"http://{ctx.obj['host']}:{ctx.obj['port']}/instances/{name}/{typ}/startvm")


@instances.command()
@click.pass_context
def list(ctx):
    httpx.get(f"http://{ctx.obj['host']}:{ctx.obj['port']}/instances/listvm")