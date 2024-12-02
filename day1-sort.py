a=[]
b=[]
with open("data.txt") as file:
    for line in file:
        numa, numb = line.replace("\n","").split("   ")
        a.append(numa)
        b.append(numb)
a.sort()
print(a)
b.sort()
print(b)
c = 0
i = 0
while (i < len(a)):
    c = c + abs(int(a[i]) - int(b[i]))
    i = i + 1
print(c)

i = 0
s = 0
while (i < len(a)):
  s = s + (int(a[i]) * b.count(a[i]))
  i = i + 1
print (s)