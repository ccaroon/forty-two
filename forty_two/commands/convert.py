"""
Convert - Unit Conversion
"""
import click
import re

CONVERSION_MAP = {
    "units":      ("mm", "cm", "in", "ft", "yd", "mi"),
    "conv_amt":   ( 1,    10,   2.54, 12,   3,    1760)
}

# convert
@click.command()
@click.argument("amount")
@click.argument("dest_units")
def convert(amount, dest_units):
    """
    Convert between measurements: amount -> dest_units

    Known Units: mm, cm, in, ft, yd, mi

    # Convert 1 Inch to Millimeters
    >>> forty-two convert 1in mm
    1.0in => 25.4mm
    """
    matches = re.match(r"(\d+(\.\d+)?)(.*)", amount)
    input_value = float(matches.group(1))
    input_units = matches.group(3)

    try:
        result = __convert_imperial(input_value, input_units, dest_units)
        print(f"{input_value}{input_units} => {result}{dest_units}")
    except ValueError as err:
        print(err)


# "units":      ("mm", "cm", "in", "ft", "yd", "mi"),
# "conv_amt":   ( 1,    10,   2.54, 12,   3,    1760)
def __convert_imperial(amount, src_unit, dest_unit):
    """
    5280, ft, mi
    """
    result = amount
    try:
        src_unit_idx = CONVERSION_MAP["units"].index(src_unit)
        dest_unit_idx = CONVERSION_MAP["units"].index(dest_unit)
    except ValueError:
        raise ValueError(f"Don't know how to convert from '{src_unit}' to '{dest_unit}'")

    if src_unit_idx < dest_unit_idx:
        # Convert Up
        conv_amt = CONVERSION_MAP["conv_amt"][src_unit_idx + 1]
        new_unit = CONVERSION_MAP["units"][src_unit_idx + 1]
        new_amt = amount / conv_amt
        result = __convert_imperial(new_amt, new_unit, dest_unit)
    elif src_unit_idx > dest_unit_idx:
        # Convert Down
        conv_amt = CONVERSION_MAP["conv_amt"][src_unit_idx]
        new_unit = CONVERSION_MAP["units"][src_unit_idx - 1]
        new_amt = amount * conv_amt
        result = __convert_imperial(new_amt, new_unit, dest_unit)

    return result
