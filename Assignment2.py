
#convert weight in pounds to kilograms
def convertWeight(weight):
    value1 = weight * 0.45
    print ("Weight in kilograms is ", value1)
    return value1

#convert height in inches to meters
def convertHeight(height):
    value2 = height * 0.025
    print("Height in meters is ", value2) 
    return value2

#square the answer from step2

def squareHeight(value2):
    value3 = value2 * value2
    print("Height squared is ", value3) 
    return value3

#divide the answer from step 1 by the answer from step 3

def divideFinal(value1, value3):
    value4 = value1 / value3
    print ("Final BMI is ", value4)
    return value4

#choose BMI category
def finalResult(value4):
    if value4 < 18.5:
        value5 = "underweight"
        print ("Person is underweight. \n")
    elif value4 >= 18.5 and value4 <= 24.9:
        value5 = "normal"
        print ("Person is in a normal weight range.  \n")
    elif value4 >= 25 and value4 <= 29.9:
        value5 = "over"
        print ("Person is in an overweight range.  \n")
    elif value4 > 30:
       value5 = "obese"
       print ("Person is OBESE. \n")
       return value5


heightF = float(input("Input height in feet "))
heightI = float(input("Input height in inches "))
weight = float(input("Input weight in pounds "))

    #convert from feet and inches to just inches 
height = heightF * 12 + heightI

    #call functions
value1 = float(convertWeight(weight))
value2 = float(convertHeight(height))
value3 = float(squareHeight(value2))
value4 = float(divideFinal(value1,value3))
value5 = (finalResult(value4))

#add incase errors are thrown with main function
# if __name__ == "__main__":
#     main()


input("Press enter to close ")
quit()