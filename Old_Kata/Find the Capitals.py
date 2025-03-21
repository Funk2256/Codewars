def capital(capitals):
    return (f"The capital of {capitals.get('state') or capitals['country']} is {capitals['capital']}" for x in capitals)


print(capital({'country': 'Spain', 'capital': 'Madrid'}))
