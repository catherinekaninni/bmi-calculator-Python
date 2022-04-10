


height = float (input("Enter height in m: \n"))
weight = int (input("Enter weight in kg\n"))


bmi = round(weight/height**2,2)
print(bmi)
if bmi <= 16:
    print(f' Your BMI is {bmi}. You are Severely underweight')
    

elif bmi <=24.5:
    print(f'Your BMI is {bmi}. You are healthy')


elif     bmi <=30:
    print(f'Your BMI is {bmi}. You are overweight')
        

elif bmi <=35.5:
    print(f'Your BMI is {bmi}. You are obese')

else:
    print(f'Your BMI is {bmi}. You are clinically obese')    
        
     


                 
        
