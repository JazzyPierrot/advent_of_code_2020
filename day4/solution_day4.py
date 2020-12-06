import pandas as pd
from common.aoc_functions import split_batch
from numpy import nan
import re

def parse_pass(pass_str):
    """Takes a pass_str in string format and convert it into a dictionnary"""
    pass_dict = {}
    for property in str.split(pass_str, " "):
        pass_dict[property[:3]] = property[4:]
    return pass_dict


def read_pass_batch(path):
    """
    Returns a pandas.DataFrame of passes from a file located at "path".
    Missing values are encoded with numpy.nan
    """
    with open(path) as f:
        return pd.DataFrame(
                [parse_pass(p) for p in split_batch(f, " ")]
                )

def are_valid_passes_A(passes):
    """
    Checks if a passes (`pd.DataFrame`) is valid or not (rule from problem
    A)
    """
    compulsary_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    return ~ passes[compulsary_fields].isnull().any(axis = 1)

def  is_between(passes, field, min, max):
    return pd.to_numeric(passes[field], errors = "coerce"). \
            between(min, max, inclusive = True)

def are_valid_passes_B(passes):
    """
    Checks if a passes (`pd.DataFrame`) is valid or not (rules from problem
    B)
    """
    ecl_cat = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    passes = passes.assign(
            valid_A = are_valid_passes_A,
            valid_byr = lambda x: is_between(x, "byr", 1920, 2002),
            valid_iyr = lambda x: is_between(x, "iyr", 2010, 2020),
            valid_eyr = lambda x: is_between(x, "eyr", 2020, 2030),
            hgt_unit = lambda x: x["hgt"].str.extract("(\D+)"),
            hgt_msr = lambda x: x["hgt"].str.extract("(\d+)"),
            valid_hgt = lambda x:  \
                    (x["hgt_unit"].eq("cm") & is_between(x, "hgt_msr", 150, 193)) | \
                    (x["hgt_unit"].eq("in") & is_between(x, "hgt_msr", 59, 76)),
            valid_hcl = lambda x: x["hcl"].str.match("^#[a-f0-9]{6}$"),
            valid_ecl = lambda x: x["ecl"].isin(ecl_cat),
            valid_pid = lambda x: x["pid"].str.match("^\d{9}$")
            )
    return passes.loc[:, passes.columns.str.startswith("valid")].all(axis = 1)

if __name__ == "__main__":
    passes = read_pass_batch("./day4/input.txt")
    solution_4A = sum(are_valid_passes_A(passes))
    print(
            f'Solution 4A:\n'
            f'------------\n'
            f'{solution_4A} valid passes out of {passes.shape[0]}'
            )
    solution_4B = sum(are_valid_passes_B(passes))
    print()
    print(
            f'Solution 4B:\n'
            f'------------\n'
            f'{solution_4B} valid passes out of {passes.shape[0]}'
            )

