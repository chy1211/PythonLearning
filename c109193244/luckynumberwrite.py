fp=open("record.txt","r")
f2=open("/SourceCode/python/c109193244/newdir/record.txt","w")
tmp=fp.readline()

while tmp != "":
    tmp=fp.readline()
    tmp1=tmp.replace("\n","")
    tmp2=tmp1.split(",")
    tmp3=tmp2[2]
    total=tmp3.replace("/","")
    print(tmp2)
    print(total)

    sum=0
    for i in total:
        sum+=int(i)
    while sum>=10:
        sum=sum//10+sum%10
    print(sum)

    f2.write(str(sum)+",")
fp.close()