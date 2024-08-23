def temperatura():
    temp = float(input("Qual a temperatura atual? "))
    
    if temp > 30:
        print("A temperatura está alta")
    elif temp >= 15:
        print("A temperatura está agradável")
    else:
        print("A temperatura está baixa")

temperatura()
