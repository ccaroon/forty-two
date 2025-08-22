"""
Convert - Unit Conversion
"""
import click
import re

@click.group
def convert():
    """ Unit Conversion """
    pass

# Each successive unit is defined in the previous unit
# Example: 1yd is 3 feet, thus "yd" conv_amt is "3"
#          1ft is 12 inches, thus "ft" conv_amt is "12"
#          Etc, down to the base unit of 1 mm.
LENGTH_UNIT_MAP = {
    "units":      ("mm", "cm", "in", "ft", "yd", "m",                    "km", "mi"),
    "conv_amt":   ( 1,    10,   2.54, 12,   3,    1.09361329833770778653, 1000, 1.609344)
}

TEMPERATURE_FORMULAS = {
    "c": {
        "f": lambda C: (C * 9/5) + 32,
        "k": lambda C: C + 273.15
    },
    "f": {
        "c":  lambda F: (F - 32) * (5/9),
        "k": lambda F: (F - 32) * (5/9) + 273.15
    },
    "k": {
        "c": lambda K: K - 273.15,
        "f": lambda K: (K - 273.15) * (9/5) + 32
    }
}

# length
@convert.command()
@click.argument("amount")
@click.argument("dest_units")
def length(amount, dest_units):
    """
    Convert between lengths: amount -> dest_units

    # Convert 1 Inch to Millimeters
    >>> forty-two convert length 1in mm
    1.0in => 25.4mm
    """
    matches = re.match(r"(\d+(\.\d+)?)(.*)", amount)
    input_value = float(matches.group(1))
    input_units = matches.group(3)

    try:
        result = __convert_length(input_value, input_units, dest_units)
        print(f"{input_value}{input_units} => {result}{dest_units}")
    except ValueError as err:
        print(err)
        print(f"Known Units: {LENGTH_UNIT_MAP['units']}")


# temperature
@convert.command()
@click.argument("amount")
@click.argument("dest_units")
def temp(amount, dest_units):
    """
    Convert between temperature units: amount -> dest_units

    >>> forty-two convert temp 32f c
    32.0f => 0.0c
    """
    matches = re.match(r"(-?\d+(\.\d+)?)(.*)", amount)
    input_value = float(matches.group(1))
    input_units = matches.group(3)

    try:
        result = __convert_temperature(input_value, input_units, dest_units)
        print(f"{input_value}{input_units} => {result}{dest_units}")
    except ValueError as err:
        print(err)
        print(f"Known Units: {list(TEMPERATURE_FORMULAS.keys())}")


def __convert_length(amount, src_unit, dest_unit):
    """
    Convert between length units using recursion.
    """
    result = amount
    try:
        src_unit_idx = LENGTH_UNIT_MAP["units"].index(src_unit)
        dest_unit_idx = LENGTH_UNIT_MAP["units"].index(dest_unit)
    except ValueError:
        raise ValueError(f"Don't know how to convert from '{src_unit}' to '{dest_unit}'")

    if src_unit_idx < dest_unit_idx:
        # Convert Up
        conv_amt = LENGTH_UNIT_MAP["conv_amt"][src_unit_idx + 1]
        new_unit = LENGTH_UNIT_MAP["units"][src_unit_idx + 1]
        new_amt = amount / conv_amt
        result = __convert_length(new_amt, new_unit, dest_unit)
    elif src_unit_idx > dest_unit_idx:
        # Convert Down
        conv_amt = LENGTH_UNIT_MAP["conv_amt"][src_unit_idx]
        new_unit = LENGTH_UNIT_MAP["units"][src_unit_idx - 1]
        new_amt = amount * conv_amt
        result = __convert_length(new_amt, new_unit, dest_unit)

    return result


def __convert_temperature(amount, src_unit, dest_unit):
    """
    Convert between temperature units
    """
    result = None
    formula = TEMPERATURE_FORMULAS.get(src_unit, {}).get(dest_unit, None)
    if formula:
        result = formula(amount)
    else:
        raise ValueError(f"Don't know how to convert from '{src_unit}' to '{dest_unit}'")

    return result
