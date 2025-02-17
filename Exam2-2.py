#การจัดรูปแบการแสดงผลโดยใช้ f-string
import os

os.system('cls')
print("Please Enter your score 3 times by score not more than 100")
f = int(input("Enter first score:"))

s = int(input("Enter second score:"))

t = int(input("Enter third score:"))

total =int((f+s+t)/3)
if total <49:
    Grade ="F"
elif total < 59:
    Grade ="D"
elif total < 69:
    Grade ="C"
elif total < 79:
    Grade ="B"
else:
    Grade ="A"
    
print(f"Your total score is {total}, and your grade is {Grade}.")

