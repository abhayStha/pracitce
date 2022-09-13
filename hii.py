
even = []
odd = []

def func():
    while True:
        try:
            num = int(input("enter a number:- "))
        except:
            print("Sorry")
        for i in range(1,num+1):
            if (i % 2 == 0):
                even.append(i)
            else:
                odd.append(i)
        print(even)
        print(odd)
        
        

func()
    