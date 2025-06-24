from pizza import Pizza

def order_pizza(pizza: Pizza) -> None:
    """
    Process a pizza order: display description and price.
    """
    print(f"A {pizza}")
    print("Price:", pizza.get_price())

def main() -> None:
    p = Pizza("large")
    p.add_topping("mushroom")
    p.add_topping("pepperoni")
    order_pizza(p)

if __name__ == "__main__":
    main()

