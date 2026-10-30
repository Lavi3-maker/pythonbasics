# for loop 
for i in range(1,11):
    print(f"Welcome to my shop! Customer {i} ")

mycustomer=("Eric","Lavender","Christine","Victor","Angela")

for n in mycustomer:
    print(f"Welcome to my school {n} ")

# my_shopping=[130,100,200,120]
# suppose you buy
# bread ksh130
# milk ksh100
# sugar ksh 200
# blueband ksh 120
# calculate the total expense

myshopping=[130,100,200,120]
total=0

for s in myshopping:
    total=total+ s
print(f"Your total expense is {total} ")

# while loop

num=0
while num <=8:
    print(f"loops :{num}")
    num+=2
# imagine you start with 0 and 
# save 100 every day until you save 500

money=0
while money<500:
    money=money+100
    print(f"Money saved {money} ")
print("Congratulation! you reached your target")