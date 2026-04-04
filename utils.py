# Utils
def calculate_total(items):
    total = 0
    for item in items:
        total = total + item['price'] * item['qty']
    return total

def format_currency(amount):
    return '$' + str(round(amount, 2))
