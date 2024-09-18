"""
Tempus - Time Related Utils
"""
import arrow
import click

@click.group()
def tempus():
    """ Manipulate Time """

# format
@tempus.command()
@click.argument("epoch", type=int)
@click.option(
    "--fmt", "-f",
    default="YYYY-MM-DD HH:mm:ss ZZ", help="Desired Date/Time format")
@click.option("--tz", "-z",
    default="local",
    help="Format for a specific TimeZone. Default 'local'.")
# pylint: disable=redefined-builtin
def format(epoch, fmt, tz):
    """ Format epoch date/time """
    try:
        date = arrow.get(epoch)
        print(date.to(tz).format(fmt))
    except arrow.parser.ParserError as err:
        print(err)

# parse
@tempus.command()
@click.argument("date_str", type=str)
@click.option("--tz", "-z",
    default="local",
    help="Format for a specific TimeZone. Default 'local'.")
def parse(date_str, tz):
    """ Parse date/time string and display epoch value """
    date = arrow.get(date_str).replace(tzinfo=tz)
    print(date.int_timestamp)

# humanize
@tempus.command()
@click.argument("date_str", type=str)
@click.option("--unit", multiple=True,
    default=["day"],
    help="Time unit(s) to be used in describing the date/time.")
@click.option("--tz", "-z",
    default="local",
    help="Format for a specific TimeZone. Default 'local'.")
def humanize(date_str, unit, tz):
    """
    Convert date/time string to humanized format

    Example: 2023-10-13 -> 42 days ago
    """
    date = arrow.get(date_str)
    units = unit[0] if len(unit) == 1 else unit
    print(date.to(tz).humanize(granularity=units))

# dehumanize
@tempus.command()
@click.argument("human_str", type=str)
@click.option("--tz", "-z",
    default="local",
    help="Format for a specific TimeZone. Default 'local'.")
def dehumanize(human_str, tz):
    """
    Compute a date/time based on human'ish words.

    Example: 42 days ago -> 2023-09-12
    """
    date = arrow.utcnow()
    try:
        print(date.to(tz).dehumanize(human_str))
    except ValueError as err:
        print(err)


# elapsed
@tempus.command()
@click.argument("start")
@click.argument("end")
def elapsed(start, end):
    """
    Compute the elapsed time between two date/time strings
    """
    start_dt = arrow.get(start)
    end_dt = arrow.get(end)

    elapsed = end_dt - start_dt
    print(elapsed)








#
