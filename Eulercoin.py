mult = 1504170715041707
mod = 4503599627370517

past_coins = set([mult])
total = mult
last_coin = mult
last_try = mult


while True:
    new_try = (last_try + mult) % mod
    # print(new_try)
    if new_try in past_coins:
        break
    if new_try < last_coin:
        total += new_try
        last_coin = new_try
        past_coins.add(new_try)
    last_try = new_try
    print(sorted(past_coins))
    print(total)

print(past_coins)
print(total)