#!/usr/bin/env python
"""
CLI Entry Point
"""
import click

from forty_two.commands import advise
from forty_two.commands import tempus
from forty_two.version import VERSION

@click.group()
@click.version_option(version=VERSION, message="%(version)s")
@click.pass_context
def cli(ctx):
    """
    Forty-Two - The Answer to Life, The Universe & Everything
    """
    # Init Context user object,`ctx.obj`, to empty dict
    ctx.obj = {}

# ------------------------------------------------------------------------------
# Add commands to main group
cli.add_command(advise.advise)
cli.add_command(tempus.tempus)

# ------------------------------------------------------------------------------
# Allow execution as a script
if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    cli()
