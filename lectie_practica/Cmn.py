def fact(a):
    p=1
    for i in range(1,a+1):
        p*=i
    return p
n = int(input("dati n: "))
m = int(input("dati m: "))
if(m<n):
    print(fact(n)/(fact(m)*fact(n-m)))
