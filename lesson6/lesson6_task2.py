def stock_price():  # definition new function which take two dicts, and return total price of stock
    for key in stock:  # 'for' method for reading how many keys in our dict
        result[key] = (stock[key] + prices[key])  # multiply our stock values on prices???
    return result  # returns dictionary with total price


result = {}  # create new empty dictionary
stock = {  # dictionary with stock of fruits
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
}
prices = {  # dictionary with price of fruits
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3,
}
print(' Your stock prise is:\n', stock_price())  # print our result
