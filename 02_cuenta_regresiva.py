import time
t = 10
while True:
    print(t)
    if t == 0:
        break
    t -= 1
    time.sleep(1)
print("Hecho")