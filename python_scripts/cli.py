#! /usr/bin/env python3
import click
import psutil

@click.group()
def cli():
    """Sample cli"""


@cli.command("disk_sdk", short_help="Show Disk Infomation using SDK")
def disk_sdk():
    click.echo(psutil.disk_usage("/"))

if __name__ == '__main__':
    cli()