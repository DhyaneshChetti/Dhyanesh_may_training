#Part - A: Output and Explanation
"""
Expected Output:
['apple']
['apple', 'banana']
['bread', 'milk']
['apple', 'banana', 'eggs']

Explanation:
1. The first call to add_item("apple") creates a new cart with "apple"
2. The second call to add_item("banana") modifies the same cart, adding "banana", so the cart now has both "apple" and "banana".
3. The third call to add_item("bread", cart) creates a new cart (since we passed None) and adds "bread" and "milk" to it, leaving the original cart unchanged.
4. The fourth call to add_item("eggs") modifies the original cart again, adding "eggs", so it now contains "apple", "banana", and "eggs". The second cart remains unchanged with "bread" and "milk".
"""

#Part - B: Fixed Code
"""
Explanation:
1. In the original code, the default argument `cart=[]` is shared across all calls that do not provide a cart. This means that if you modify the cart in one call, it affects all future calls that use the default cart.
2. By changing the default argument to `cart=None`, we can check if a cart was provided. If not, we create a new empty list inside the function, ensuring that each call gets its own independent cart.
"""
def add_item(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart

#Part - C:
def create_cart(owner, discount=0):
    return {
        "owner": owner,
        "items": [], 
        "discount": discount
    }

def add_to_cart(cart, name, price, qty=1):
    cart["items"].append({
        "name": name, 
        "price": price, 
        "qty": qty
    })

def update_price(price_tuple, new_price):
    """
    Tuples are immutable, meaning once created, their internal elements 
    cannot be changed, added, or removed. Attempting to assign a new 
    value to an index will raise a TypeError.
    """
    try:
        price_tuple[0] = new_price
    except TypeError as e:
        print(f"TypeError caught: {e}")
        print("Explanation: You cannot modify a tuple because it is immutable.")

def calculate_total(cart):
    subtotal = 0
    for item in cart["items"]:
        subtotal += item["price"] * item["qty"]
    discount_amount = subtotal * (cart["discount"] / 100)
    final_total = subtotal - discount_amount
    return final_total

if __name__ == "__main__":
    print("--- Customer 1: Dhyanesh ---")
    dhyanesh_cart = create_cart("Dhyanesh", discount=20)
    add_to_cart(dhyanesh_cart, "Laptop", 3000)
    add_to_cart(dhyanesh_cart, "Mouse", 1500, qty=2)
    print("Dhyanesh's Cart:", dhyanesh_cart)
    print(f"Dhyanesh's Total: {calculate_total(dhyanesh_cart):} Rs\n")

    print("--- Customer 2: Kishore ---")
    kishore_cart = create_cart("Kishore")
    add_to_cart(kishore_cart, "Headphones", 2000)
    print("Kishore's Cart:", kishore_cart)
    print(f"Kishore's Total: {calculate_total(kishore_cart):} Rs\n")
    
    print("--- Proof Carts are Independent ---")
    print(f"Does Dhyanesh have Kishore's items? {dhyanesh_cart['items'] == kishore_cart['items']}")

    print("\n--- Tuple Immutability Test ---")
    my_price = (50.00,)
    update_price(my_price, 45.00)


"""
1. Why is discount=0 safe but cart=[] dangerous?
   Integer objects (like 0) are immutable. You cannot change the number 0 into another number in memory. If you do `discount += 5`, Python just points the variable `discount` to a new integer object (5), leaving the default intact. 
   A list `[]`, however, is mutable. You can change its internal contents (.append) without changing its identity. The default argument keeps pointing to that mutated list object forever.

2. What is the difference between rebinding and mutating?
   - Mutating: Changing the internal state of an existing object in memory (e.g., my_list.append(5)). The object stays at the same memory address.
   - Rebinding: Pointing a variable name to an entirely new object in memory (e.g., my_list = [1, 2, 3]). The original object is untouched (and will eventually be garbage collected if no other variables point to it).

3. Which of these are mutable?
   - Mutable: list, dict, set
   - Immutable: tuple, str, int

4. When you pass a list into a function and modify it, do changes reflect outside? Why?
   Yes as python passes arguments by "object reference". When you pass a list to a function, the function's parameter becomes a new reference pointing to the exact same list object in memory as the variable outside. Mutating the object inside the function changes the shared object, so the changes are visible outside.
"""