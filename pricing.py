from currency_utils import convert, format_currency

def convert_price(amount, src, dst):
    return {"amount": convert(amount, src, dst), "display": format_currency(convert(amount, src, dst), dst)}
