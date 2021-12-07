import math
pembatas="----------------------"
print(pembatas)
print("BASIC MATH CALCULATOR")
print("BY : NEOZA")
print(pembatas)

answer=str(input("Calculation[Addition|Subtract|Multiply|Division] : "))
print(pembatas)

if answer.lower()=="addition" or answer.lower()=="add" :
  ad1=int(input("Number(#1) : "))
  ad2=int(input("Number(#2) : "))
  ad=ad1+ad2
  print("=", ad)
  print(pembatas)

elif answer.lower()=="subtraction" or answer.lower()=="subtract" :
  su1=int(input("Number(#1) : "))
  su2=int(input("Number(#2) : "))
  su=su1-su2
  print("=", su)
  print(pembatas)

elif answer.lower()=="multiply" or answer.lower()=="multiplication" : 
  mu1=int(input("Number(#1) : "))
  mu2=int(input("Number(#2) : "))
  mu=mu1*mu2
  print("=", mu)
  print(pembatas)

elif answer.lower()=="division" or answer.lower()=="divide" : 
  di1=int(input("Number(#1) : "))
  di2=int(input("Number(#2) : "))
  di=di1/di2
  print("=", di)
  print(pembatas)

else : 
  print("ERROR")
  print(pembatas)
