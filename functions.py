# def my_function() :
#     print("Hello world")

# my_function()

# def salutation():
#     hello = "Good morning Man Derickoe"
#     print(hello)

# salutation()

# def salute(name):
#     print(f"Good morning {name}")

# salute('dero')

# def person(name,country,county):
#     print(f'My name is {name} and am from {country} , {county}')

# person('Dero' , 'Kenya' , 'Siaya County')

# def multi(x,y,z):
#     results = x*y*z
#     return results

# print (multi(2,3,4))

# write a function that will calculate BMI of a person

def calculate_BMI(weight_kg, height_m):
    
    if height_m <= 0:
        print("Height must be a positive number of meters.")

    BMI = weight_kg / (height_m ** 2)

    
  


    if BMI < 18.5:
        category = "Underweight"
    elif 18.5 <= BMI < 25:
        category = "Normal (Healthy Weight)"
    elif 25 <= BMI < 30:
        category = "Overweight"
    else:
       print(f"This BMI falls into the '{category}' category.")

       return BMI

      

    print(calculate_BMI(weight_kg, height_m))

    
