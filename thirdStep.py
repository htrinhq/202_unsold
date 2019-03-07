##
## EPITECH PROJECT, 2019
## 202unsold_2018
## File description:
## thirdStep
##

def expected(tab: [float], v: int):
    """Expect values of Y, X and Z."""
    exp = 0
    var = 0
    for i in range(len(tab)):
        exp += (tab[i] * ((i + v) * 10))
    for i in range(len(tab)):
        var += (tab[i] * pow((((i + v) * 10) - exp), 2))
    return exp, var


def print_expected_values(xTab: [float], yTab: [float], zTab: [float]):
    """Display expected values of X, Y, Z."""
    expX, varX = expected(xTab, 1)
    expY, varY = expected(yTab, 1)
    expZ, varZ = expected(zTab, 2)
    print('expected value of X:\t{:.01f}' .format(expX))
    print('variance of X:\t\t{:.01f}' .format(varX))
    print('expected value of Y:\t{:.01f}' .format(expY))
    print('variance of Y:\t\t{:.01f}' .format(varY))
    print('expected value of Z:\t{:.01f}' .format(expZ))
    print('variance of Z:\t\t{:.01f}' .format(varZ))
