
"""
С начала суток прошло H часов, M минут, S секунд (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60). По данным числам H, M, S
 определите угол (в градусах), на который повернулаcь часовая стрелка с начала суток и выведите его в виде 
действительного числа.
"""

H = int(input("H: "))
M = int(input("M: "))
S = int(input("S: "))


ONE_DEGREE=(12*3600+60*60+60)/360
ANG_H=360/12
ANG_M=360/(60*12)
ANG_S=360/(3600*12)


SUM_ANG=(H*ANG_H)+(M*ANG_M)+(S*ANG_S)

print ("Rounded angle: "+str(round(SUM_ANG)))




