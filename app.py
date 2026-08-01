def main():
    print("Hello, World!")

# app.py
def calculate_total(price, tax_rate):
    """Calculates the total price including tax."""
    # BUG: We are accidentally subtracting the tax!
    return price - (price * tax_rate)

if __name__ == "__main__":
    main()
