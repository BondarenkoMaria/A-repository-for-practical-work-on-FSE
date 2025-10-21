prev, curr = int(input())

if curr >= prev:
    used = curr - prev
else:
    used = 10000 - prev + curr

if used <= 300:
    payment = 21
elif used <= 600:
    payment = 21 + (used - 300) * 0.06
elif used <= 800:
    payment = 21 + 300 * 0.06 + (used - 600) * 0.04
else:
    payment = 21 + 300 * 0.06 + 200 * 0.04 + (used - 800) * 0.025

price = payment / used
