x = int(input())
z = str(input())
y = []
ca,cd = 0,0
for i in range(0,x):
    y.append(z[i])

for i in range(0,len(y)):
    if (y[i]=="A"):
        ca += 1
    else:
        cd += 1

if ca>cd:
    print("Anton")
elif ca<cd:
    print("Danik")
else:
    print("Friendship")
