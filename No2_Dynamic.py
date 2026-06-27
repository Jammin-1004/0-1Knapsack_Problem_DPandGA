import time

# Data Parsing 
def parse_knapsack_data(filepath):
    capacity = 0
    items = []

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith("Total weight capacity:"):
            capacity = int(line.split(":")[1].strip())
            continue

        parts = line.split()

        if len(parts) == 3:
            try:
                items.append({
                    'id': int(parts[0]),
                    'weight': int(parts[1]),
                    'profit': int(parts[2])
                })
            except ValueError:
                continue 

    return capacity, items

# DP Algorithm
def solve_dp(capacity, items):
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    start_time = time.time()

    for i in range(1, n + 1):
        w_i = items[i - 1]['weight']
        p_i = items[i - 1]['profit']

        for w in range(capacity + 1):
            if w_i <= w:
                dp[i][w] = max(p_i + dp[i - 1][w - w_i], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(items[i - 1]['id'])
            w -= items[i - 1]['weight']

    execution_time = time.time() - start_time
    selected_items.reverse()

    return dp[n][capacity], selected_items, execution_time

# Main
if __name__ == "__main__":
    file_path = "TestData(0-1Knapsack)_10.txt" 

    try:
        cap, item_list = parse_knapsack_data(file_path)
        print(f"[{len(item_list)} Load] Bag Capacity: {cap}")

        profit, items, exec_time = solve_dp(cap, item_list)
        print("\n==Dynamic Programming==")
        print(f"MAX Value: {profit}")
        if len(items) <= 50:
            print(f"Selec Item: {items}")
        print(f"Run time: {exec_time:.4f} s")

    except FileNotFoundError:
        print("Check File Path")