x = int(input('enter x '))
y = int(input('enter y '))
sq = 1
if (x > 0 and y < 0):
    sq = 4
elif (x < 0):
    if( y > 0 ):
        sq = 2
    else:
        sq = 3
print(sq)