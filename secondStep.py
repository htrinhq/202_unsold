##
## EPITECH PROJECT, 2019
## 202unsold_2018
## File description:
## secondStep
##

def print_z(l: [[float]], zTab: [float]) -> [float]:
    """Displays z values."""
    zTab = [l[0][0],
            l[1][0] + l[0][1],
            l[2][0] + l[1][1] + l[0][2],
            l[3][0] + l[2][1] + l[1][2] + l[0][3],
            l[4][0] + l[3][1] + l[2][2] + l[1][3] + l[0][4],
            l[4][1] + l[3][2] + l[2][3] + l[1][4],
            l[4][2] + l[3][3] + l[2][4],
            l[4][3] + l[3][4],
            l[4][4]]
    #zTab.append(sum(zTab))
    print('z\t20\t30\t40\t50\t60\t70\t80\t90\t100\ttotal')
    print('p(Z=z)', end='\t')
    for i in range(0, 10):
        if i == 9:
            print('{:g}' .format(sum(zTab)))
            return zTab
        else:
            print('{:.03f}' .format(zTab[i]), end='\t')
