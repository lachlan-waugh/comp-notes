import sys

prob = [0.4, 0.3, 0.15, 0.15]
msgs = [2, 1, 3]
start = 0
width = 1

for msg in msgs:
    msg = int(msg[0]) - 1

    start = start + (float(sum(prob[:msg])) * width)
    width = width * float(prob

    print(start, end=" ")
    print(end)

    arithmetic(start, width, end, prob, msgs[1:]) 

#prob = input("input probabilities\n").split()
#msgs = input("input messages\n").split()
