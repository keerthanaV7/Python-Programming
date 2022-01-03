n1 = int(input())
n2 = int(input())

def gcd(n1,n2):
    if n2 > n1:
        n2,n1 = n1,n2 
    while n1%n2 != 0:
        rem = n1%n2
        n1 = n2
        n2 = rem
    return n2
gcd = gcd(16,408)
lcm = n1*n2//gcd
print(gcd)
print(lcm)