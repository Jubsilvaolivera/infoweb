#1
#A = int(input())
#B = int(input())

#PROD = A * B

#print("PROD =", PROD)


#2
#N1 = float(input())
#N2 = float(input())

#M = (N1 * 3.5 + N2 * 7.5) / 11

#print("MEDIA =", f"{M:.5f}")


#3
#R = float(input())

#pi = 3.14159

#V = 4/3.0 * pi * (R * R * R)

#print("VOLUME = " f"{V:.3f}")


#4
#import math

#linha1 = map(float, input().split())
#linha2 = map(float, input().split())

#A1, B1 = linha1
#A2, B2 = linha2


#D = math.sqrt(((float(A2) - float(A1))*(float(A2) - float(A1))) + ((float(B2)-float(B1)) *(float(B2)-float(B1))))

#print(f"{D:.4f}")



x, y = raw_input().split(' ')
x = int(x)
y = int(y)

if x > y:
    print x % y
else:
    print y % x