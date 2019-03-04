##
## EPITECH PROJECT, 2019
## 202unsold_2018
## File description:
## firstStep
##

def proba(values: [int], x: int, y: int) -> float:
    """Get the Probability with subject formula."""
    return (((values[0] - x) * (values[1] - y)) /
            ((5 * values[0] - 150) * (5 * values[1] - 150)))


def fill_joint_law(joint_law: [[float]], values: [int]) -> [[float]]:
    """Fill double tab joint_law with proba() function."""
    for i in range(0, 5):
        x_tab = []
        for x in range(0, 5):
            x_tab.insert(x, proba(values, (x + 1) * 10, (i + 1) * 10))
        joint_law.insert(i, x_tab)
    return joint_law


def print_Xtab(joint_law: [[float]], xTab: [float]) -> [float]:
    """Display Xtab."""
    print('X law', end='\t')
    for i in range(0, 5):
        add = 0
        for x in range(0, 5):
            add += joint_law[x][i]
        xTab.append(add)
        print('%.03f' % (add), end='\t')
    print('{:g}' .format(sum(xTab)))
    return xTab


def print_Ytab(joint_law: [[float]], yTab: [float]) -> [float]:
    """Displays Xtab."""
    print('\tX=10\tX=20\tX=30\tX=40\tX=50\tY law')
    for y in range(0, 5):
        for i in range(0, 5):
            if i == 0:
                print('Y=' + str((y + 1) * 10), end='\t')
            print('%.03f' % joint_law[y][i], end='\t')
        print('%.03f' % sum(joint_law[y]))
        yTab.append(sum(joint_law[y]))
    return yTab
