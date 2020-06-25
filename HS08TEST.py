# cook your dish here
x, y = map(str, input().split())
x = int(x)
y = float(y)
if x%5==0 and y >= x+0.5:
    print(y-(x+0.5))
else:
    print(y)