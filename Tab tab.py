def lend_money(debts, person, amount):
    if person in debts:
        debts[person].append(amount)
    else:
        debts[person] = [amount]


def amount_owed_by(debts, person):
    total = 0
    if person not in debts:
        return 0
    else:
        for amount in debts[person]:
            total+=amount
    return total

def total_amount_owed(debts):
    total = 0
    for person in debts:
        for amount in debts[person]:
            total+=amount
    return total
