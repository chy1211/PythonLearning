de=int(input("輸入所使用的度數"))

if de<=120:
    summer=de*2.1
    nonsummer=de*2.1
elif de>=121 and de<=330:
    summer=de*3.02
    nonsummer=de*2.68
elif de>=331 and de<=500:
    summer=de*4.39
    nonsummer=de*3.61
elif de>=501 and de<=700:
    summer=de*4.97
    nonsummer=de*4.01
elif de>=701:
    summer=de*5.63
    nonsummer=de*4.5
    
print("Summer month:",summer)
print("Non-Summer month:",nonsummer)