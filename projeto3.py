from decimal import ROUND_DOWN, Decimal


def calculate_change(item_price, amount_paid):
    
    item_price = Decimal(str(item_price))
    amount_paid = Decimal(str(amount_paid))

    if amount_paid < item_price:
        print(f"Faltam R$ {item_price - amount_paid:.2f}!")
        return

    change = amount_paid - item_price
    if change == 0:
        print("Não existe troco!")
        return

    print(f"Troco: R$ {change:.2f}")
    denominations = [
        Decimal("5"),
        Decimal("2"),
        Decimal("1"),
        Decimal("0.50"),
        Decimal("0.25"),
        Decimal("0.10"),
        Decimal("0.05"),
        Decimal("0.01"),
    ]

    for denomination in denominations:
        count = (change / denomination).quantize(Decimal("1"), rounding=ROUND_DOWN)
        if count > 0:
            if denomination >= 1:
                print(f"{count} Nota(s) de R$ {denomination:.2f}")
            else:
                print(f"{count} Moeda(s) de R$ {denomination:.2f}")
            change -= count * denomination


if __name__ == "__main__":
    print("Calculadora de troco")
    print("---------------------")
    item_price = float(input("Valor da mercadoria: R$ "))
    amount_paid = float(input("Valor pago: R$ "))
    calculate_change(item_price, amount_paid)