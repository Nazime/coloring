import re
from typing import List

from .consts import *


# =================== #
# INTERNALS FUNCTIONS #
# =================== #
def my_re_escape(text):
    escape_char = r"[]"
    returned_text = ""
    for c in text:
        if c in escape_char:
            returned_text += "\\"
        returned_text += c
    return returned_text


ESCAPED_CSI = my_re_escape(CSI)


def remove_attributes_from_sgr(sgr_string: str, attributes: List[str]) -> str:
    """
    Remove unwanted attributes in an SRG sequence.
    SRG sequence start always with '\033[' and end with 'm'.
    Not all attributes have the same number of parameters.
    If all the attributes are removed return an empty string (without CSI and 'm')
    Args:
        sgr_string: SRG string
        attributes: attributes to remove

    Returns:
        SRG string without unwanted attributes
    """
    # TODO: replace remove by a set to optimize lookup
    # Remove the CSI in the beginning and the 'm' at the end
    params = sgr_string[2:-1].split(";")
    keep: List[str] = []  # list of params to keep, to return in the end

    # Since we are going to jump some iterations we can't use
    # for loop, but we will use while loop.
    i = 0
    while True:
        if i >= len(params):
            break
        param = params[i]
        # 38 48 58 are the only attributes that take more than one parameter
        # https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_parameters
        if param not in ["38", "48", "58"]:
            if param not in attributes:
                keep.append(param)
        else:
            second_param = params[i + 1]
            # if second param is 2 => the attribute take 5 param
            if second_param == "2":
                params_to_keep = params[i : i + 5]
                i = i + 4
            # if second param is 5 => the attribute take 3 param
            elif second_param == "5":
                params_to_keep = params[i : i + 3]
                i = i + 2
            else:
                # FIXME: How to handle errors? if the attribute is wrong?
                params_to_keep = []
            if param not in attributes:
                keep.extend(params_to_keep)

        i += 1
    # If keep is empty return an empty string without CSI and 'm'
    if keep:
        return f"{CSI}{';'.join(keep)}m"
    else:
        return ""


def repl_remove_attributes_from_sgr(matchobj, remove: List[str]) -> str:
    """Addapted remove_sequence_from_text function to be used with regex"""
    return remove_attributes_from_sgr(matchobj.group(0), remove)


re_sgr = re.compile(
    fr"""
    {ESCAPED_CSI}
    \d*
    (?:
        ;\d*
    )*
    m
""",
    re.VERBOSE,
)


def remove_attributes_from_string(string, remove: List[str]) -> str:
    """Remove unwanted attributes form a string"""
    return re_sgr.sub(lambda x: repl_remove_attributes_from_sgr(x, remove), string)


# ======================== #
# REMOVE GRAPHIC FUNCTIONS #
# ======================== #
def rmgraphics(string: str) -> str:
    """Remove all graphics attributes (all SGR)"""
    return re_sgr.sub("", string)


def rmcolor(text: str) -> str:
    """Remove all color attributes from a string"""
    # remove all attributes from 30 to 39
    # 30-37 => 8colors
    # 38 => 24 bits colors
    # 39 => reset colors
    remove = [str(i) for i in range(30, 40)]
    return remove_attributes_from_string(text, remove)


def rmbackground(text: str) -> str:
    """Remove all color attributes from a string"""
    # remove all attributes from 40 to 49
    # 40-47 => 8colors background
    # 48 => 24 bits colors background
    # 49 => reset background colors
    attributes = [str(i) for i in range(40, 50)]
    return remove_attributes_from_string(text, attributes)


def rmstyle(text: str) -> str:
    # TODO: change list to set
    # TODO: test rmstyle
    # TODO: make the list outside of the function to optimize (not calculate the list each time)
    attributes = [
        N_UNDERLINE,
        N_DOUBLE_UNDERLINE,
        N_RESET_UNDERLINE,
        N_ITALIC,
        N_RESET_ITALIC,
        N_CROSS,
        N_RESET_CROSS,
        N_BLINK,
        N_RESET_BLINK,
        N_BOLD,
        N_DIM,
        N_RESET_BOLD_AND_DIM,
    ]
    return remove_attributes_from_string(text, attributes)


def rmunderline(text):
    attributes = [N_UNDERLINE, N_DOUBLE_UNDERLINE, N_RESET_UNDERLINE]
    return remove_attributes_from_string(text, attributes)


def rmitalic(text):
    attributes = [N_ITALIC, N_RESET_ITALIC]
    return remove_attributes_from_string(text, attributes)


def rmcross(text):
    attributes = [N_CROSS, N_RESET_CROSS]
    return remove_attributes_from_string(text, attributes)


def rmblink(text):
    attributes = [N_BLINK, N_RESET_BLINK]
    return remove_attributes_from_string(text, attributes)


def rmbold_and_dim(text):
    attributes = [N_BOLD, N_DIM, N_RESET_BOLD_AND_DIM]
    return remove_attributes_from_string(text, attributes)
