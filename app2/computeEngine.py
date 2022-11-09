import random, math, socket
import hashlib

class ExampleHash:

    def __init__(self):
        self.hashFunction = hashlib.new('sha256')

    def compHash(self, data):
        myBytes = data.encode()
        self.hashFunction.update(myBytes)
        return int(self.hashFunction.hexdigest(),base=16)

name = socket.gethostname()
print(name)
e = ExampleHash()
seed = e.compHash(name) % 2**32
print(seed)

#
# 0 = tails
# 1 = heads
#
heads_in_a_row = 0
for i in range(64):
    coin_flip = random.randint(0,1)
    print(coin_flip)
    if 0 == coin_flip:
        heads_in_a_row = 0
    else:
        heads_in_a_row += 1
    print("Heads in a Row:" ,heads_in_a_row)
def isPrime(n):
    prime = True
    for i in range(2,math.floor(math.sqrt(n))):
        if 0 == n % i:
            prime = False
            break
    return prime
