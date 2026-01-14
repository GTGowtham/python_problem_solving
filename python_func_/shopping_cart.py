def calculate_total_cost(cart):
    total_cost=0
    for item in cart:
       price=float(item['price'])
       quantity=int(item['quantity'])
       total_cost+=price*quantity
    return total_cost
cart=[{'fruit':'Apple','price':'0.5','quantity':'4'},
      {'fruit':'Banana','price':'0.3','quantity':'6'},
      {'fruit':'Orange','price':'0.7','quantity':'3'},]
print(calculate_total_cost(cart))