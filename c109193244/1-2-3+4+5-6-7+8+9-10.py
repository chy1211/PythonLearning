ans1=ans2=ans3=0

for i in range(1,11):
    ans1+=i
print(ans1)
for i in range(1,11):
    if i%2==0:
        ans2-=i
    else:
        ans2+=i
print(ans2)
for i in range(2,11):
    if i%4==0:
        ans3+=i
    elif i%4==1:
        ans3+=i
    else:
        ans3-=i
print(ans3)