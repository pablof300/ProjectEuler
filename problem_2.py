n = 2
fibseqence = [1,2] # fibseqence[2]
sum = 2
def fib(n):
    return fibseqence[n-1] + fibseqence[n-2]
inbound = True
while inbound:
    fibb = fib(n)
    fibseqence.append(fibb)
    if fibb > 4000000:
        inbound = False
    if fibb % 2 == 0 & fibb < 4000000:
        print("Summing " + str(fibb))
        sum += fibb
    n = n + 1
print(sum)

