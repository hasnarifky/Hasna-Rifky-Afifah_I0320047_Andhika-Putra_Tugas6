#Program pengulangan dan fungsi range

angka1 = 10
angka2 = 24

for i in range(angka1, angka2+1) :
    if i==2 or i==3 or i==5 or i==7 :
        print(i, "adalah bilangan prima")
    elif (i>1 and i%2 != 0 and i%3 != 0 and i%5 != 0 and i%7 != 0) :
        print(i, "adalah bilangan prima")
    else :
        print(i,"bukan prima")
