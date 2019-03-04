def persegiempat(x,y):
    for i in range(x):
        if i==0 or i== x-1:
            print("@"*y)
        else:
            print("@"+" "*(y-2)+"@")

persegiempat(3,5)