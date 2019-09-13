import math
def Hypotenuse (a, b):
    hypotenuse = 0

    hypotenuse = (math.sqrt((a**2) + (b**2)))

    return hypotenuse

def main():
    a = 0
    b = 0

    a = int (input ("Enter side A length: \n"))
    b = int (input ("Enter side B length: \n"))
    print (Hypotenuse(a, b))

if __name__ == "__main__":
    main()