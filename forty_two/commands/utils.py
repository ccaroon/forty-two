"""
Misc Utilities
"""
import math
import sys
import time

import click


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


# Timer
PROGRESS_START='|'
PROGRESS_MARK='='
PROGRESS_END='|'
PROGRESS_ICONS=[
    '🕛', '🕐', '🕑', '🕒', '🕓', '🕔', '🕕', '🕖', '🕗', '🕘', '🕙', '🕚'
]
REPORT_EVERY=1
@utils.command()
@click.option("--hrs", type=int, default=0, help="Set timer for H hours.")
@click.option("--mins", type=int, default=0, help="Set timer for M minutes.")
@click.option("--secs", type=int, default=0, help="Set timer for S seconds.")
def timer(hrs, mins, secs):
    """
    Start a Timer

    Args:

        hrs (int): Set H hours on the timer.
    
        mins (int): Set M minutes on the timer.

        secs (int): Set S seconds on the timer.

    """
    if hrs or mins or secs:
        limit = (hrs * 60 * 60) + (mins * 60) + secs
    else:
        limit = sys.maxsize

    count = 0
    output = ''
    limit_ind = f"{hrs:02d}:{mins:02d}:{secs:02d}" if hrs or mins or secs else "--:--:--"
    try:
        while count < limit:
            count += 1
            hours = count // 3600
            minutes = (count - (hours * 3600)) // 60
            seconds = count % 60

            icon = PROGRESS_ICONS[count % 12]
            elapsed = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            prefix = f"{icon}[{elapsed}/{limit_ind}]{PROGRESS_START}"
            output += PROGRESS_MARK
            end_mark = '>'
            if count % REPORT_EVERY == 0:
                print(F"{prefix}{output}{end_mark}", end='\r', flush=True)

            if count % 60 == 0:
                print(F"{prefix}{output}{PROGRESS_END}", flush=True)
                output = ""

            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        hours = count // 3600
        minutes = (count - (hours * 3600)) // 60
        seconds = count % 60

        print(f"\nElapsed Time: {hours}h {minutes}m {seconds}s")
