number_of_calls=int(input("Enter the number of calls: "))
total=0.0
if number_of_calls>=100:
    total=total+2000
    number_of_calls=number_of_calls-100
while number_of_calls>=1:
    for i in range(50):
        if number_of_calls==0:
            break
        total+=0.60
        number_of_calls-=1
    for j in range(50):
        if number_of_calls==0:
            break
        total+=0.50
        number_of_calls-=1
    while number_of_calls>=1:
        total+=0.40
        number_of_calls-=1
    print("The monthly telephone bill is: ",round(total,2)) 
    
    