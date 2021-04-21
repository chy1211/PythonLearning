x=int(input("輸入X軸座標"))
y=int(input("輸入Y軸座標"))
distance=x*x+y*y
if x>0 and y>0:
    print("座標(",x,",",y,")位於第一象限，離原點距離為根號",distance)
elif x<0 and y>0:
    print("座標(",x,",",y,")位於第二象限，離原點距離為根號",distance)
elif x<0 and y<0:
    print("座標(",x,",",y,")位於第三象限，離原點距離為根號",distance)
elif x==0 and y==0:
    print("座標(",x,",",y,")位於原點")
elif x>0 and y==0:
    print("座標(",x,",",y,")位於右半平面X軸上，離原點距離為根號",distance)
elif y>0 and x==0:
    print("座標(",x,",",y,")位於上半平面Y軸上，離原點距離為根號",distance)
elif x<0 and y==0:
    print("座標(",x,",",y,")位於左半平面X軸上，離原點距離為根號",distance)
elif y<0 and x==0:
    print("座標(",x,",",y,")位於下半平面Y軸上，離原點距離為根號",distance)
else:
    print("座標(",x,",",y,")位於第四象限，離原點距離為根號",distance)