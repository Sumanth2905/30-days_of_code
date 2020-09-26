#function to calculate factorial using recursion
def Factorial(num):
    if num == 1:
        return 1
    else:
        return (num * Factorial(num-1))   
if __name__ == "__main__":
    print(Factorial(int(input())))