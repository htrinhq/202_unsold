##
## EPITECH PROJECT, 2019
## 202unsold_2018
## File description:
## unsold
##

from thirdStep import *
from secondStep import *
from firstStep import *
from sys import argv, stderr

def unsold(values: [int]) -> int:
    """Unsold main function."""
    joint_law = [[]]
    xTab = []
    yTab = []
    zTab = []
    joint_law = fill_joint_law(joint_law, values)
    divider()
    yTab = print_Ytab(joint_law, yTab)
    xTab = print_Xtab(joint_law, xTab)
    divider()
    zTab = print_z(joint_law, zTab)
    divider()
    print_expected_values(xTab, yTab, zTab)
    divider()
    return 0


def divider():
    """Divide Sections with '-'"""
    print('-' * 54)


def error():
    """Error message and exit 84"""
    stderr.write('\033[31mINVALID ARGUMENT\n\033[0m')
    stderr.write('Type \'-h\' for more informations\n')
    exit(84)


def helper():
    """Helper function for 202unsold."""
    print('USAGE\n\t./202unsold a b\n')
    print('DESCRIPTION\n\ta\tconstant computed from the past joint_law')
    print('\tb\tconstant computed from the past joint_law')
