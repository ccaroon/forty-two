"""
Misc Utilities
"""
import click
import math


@click.group()
def utils():
    """ Utility Commands """


# mp2res
@utils.command()
@click.argument("megapixels", type=int)
@click.argument("aspect_ratio", type=str)
def mp2res(megapixels, aspect_ratio):
    """
    Convert Megapixels to X,Y Resolution

    Args:

        megapixels (int): Number of Megapixels. Ex: 1, 12, 50

        aspect_ratio (str): Aspect Ratio. Ex: 4:3, 16:9
    """
    mp = megapixels * 1000000
    ar1, ar2 = aspect_ratio.split(":")
    aspect = int(ar1) / int(ar2)

    xres = round(math.sqrt(aspect * mp))
    yres = round(math.sqrt((1/aspect) *  mp))

    print(f"{xres}x{yres}")
