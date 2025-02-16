#คำนวณพื้นที่และเส้นรอบวงกลม
import os

os.system('cls')
PI = 22/7
Radius =float(input("กรุณาป้อนความยาวรัศมีวงกลม :"))
#Area = round(PI*Radius*Radius,2)
#Circumference = round(2*PI*Radius,2)
Area = PI*Radius*Radius
Circumference = 2*PI*Radius

#print("พื้นที่วงกลม =", Area)
#print("ความยาวเส้นรอบวง =",Circumference)
print("พื้นที่วงกลงม =","%.2f" % Area)
print("ความยาวเส้นรอบวง =", "%.2f" %Circumference)