def calculate_eoq(demand, order_cost, holding_cost):
    from math import sqrt
    return sqrt((2 * demand * order_cost) / holding_cost)

def calculate_safety_stock(std_dev, z_score, lead_time):
    return z_score * std_dev * (lead_time ** 0.5)

# Example usage
if __name__ == "__main__":
    D = 5000        # Annual demand
    S = 100         # Order cost per order
    H = 10          # Holding cost per unit per year
    eoq = calculate_eoq(D, S, H)

    std_dev = 20    # Standard deviation of demand
    z = 1.65        # Z-score for 95% service level
    lead_time = 2   # In weeks
    safety_stock = calculate_safety_stock(std_dev, z, lead_time)

    print(f"EOQ: {eoq:.2f}")
    print(f"Safety Stock: {safety_stock:.2f}")
