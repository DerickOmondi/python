
# # Correct_Password = input("Enter a strong passsword")


# # while Correct_Password:
# #     if Correct_Password == " ":
# #         print("Invalid passsword")
# #         Correct_Password = input("Enter a strong passsword: ")

 
# #     elif len(Correct_Password) < 8:
# #             print("Password Too short")

# # else:
# #      print("Log in successful")

        


# # max_attempts = 3

# # while attempts > 0:
# #     password = input(f"Enter your password,{attempts} Attempts left: ): ")

# #     if password == Correct_Password:
# #         print("Login successful! Access granted.")
# #         break
    
# #     else:
# #         attempts -= 1
# #         print("Incorrect password.")
# #         if attempts == 0:
# #             print(f"Too many attempts, try later ")"




def get_valid_password():
    password = "" 
    
    for attempt in range(1, 4): 

        attempt -= 1
        attempt_remaining = 3 - attempt
        
        print(f"{attempt_remaining} attempts remaining")
        
        password = input("Enter a strong password: ")
        
        correct_password = len(password) > 8 and " " not in password
        
        if correct_password:
            print("Log in succesful!")
            return password
        else:
           
            if len(password) <= 8:
                print("Password must be more than 8 characters long.")
            if " " in password:
                print("Password cannot contain spaces.")
                

    print("Please try again after 30 seconds")
    
password = get_valid_password() 
   
