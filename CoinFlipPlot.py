import random
import matplotlib.pyplot as plt

coin_flips = []

for amount in range(25):
    flip = random.randint(0, 1)
    if (flip == 0):
        coin_flips.append(0)
    else:
        coin_flips.append(1)

plt.plot(coin_flips)
plt.axis([0,25, 0, 1])
plt.ylabel("<--Heads                 Tails-->")
plt.xlabel("Number of flips")
plt.title("Flipping A Coin 25 Times")
plt.show()
