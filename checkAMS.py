
def passThePillow( n: int, time: int) -> int:
    count = n
    pillow = 1
    t=0
    def forward(t, pillow, count):
        for i in range(t, time):
            t=i
            if pillow < count:
                pillow+=1
            elif t==time:
                return pillow
            else:
                backward(t, pillow, count)
                break
    def backward(t, pillow, count):
        for i in range(t, time):
            t=i
            if pillow > 1:
                pillow-=1
            elif t==time:
                return pillow
            else:
                forward(t, pillow, count)
                break
    print(forward(t, pillow, count))
print(passThePillow(4,5))