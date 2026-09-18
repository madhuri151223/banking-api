def transfer_money(balance, amount):
    if amount <= 0:
        raise ValueError("Transfer amount must be positive")

    if amount > balance:
        raise ValueError("Insufficient balance")

    return balance - amount
