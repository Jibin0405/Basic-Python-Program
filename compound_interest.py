P= int(input("enter a number"))
R=int(input("enter another number"))
T=int(input("enter another number"))
def compound_interest(principal, rate, time):
    return principal * ((1 + rate / 100) ** time) - principal
print("Compound Interest ",(P, R, T),"=", compound_interest(P, R, T))
