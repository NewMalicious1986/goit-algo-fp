items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    # Sort items by calories-to-cost ratio
    sorted_items = sorted(items.items(),
                          key=lambda x: x[1]["calories"] / x[1]["cost"],
                          reverse=True)

    selected = []
    total_cost = 0
    total_calories = 0

    for name, info in sorted_items:
        if total_cost + info["cost"] <= budget:
            selected.append(name)
            total_cost += info["cost"]
            total_calories += info["calories"]

    return selected, total_cost, total_calories


def dynamic_programming(items, budget):
    # Convert the items dictionary to a list for indexing
    item_list = list(items.items())
    n = len(item_list)

    # Create the DP table with dimensions (n+1) x (budget+1)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    # Fill in the DP table
    for i in range(1, n + 1):
        name, info = item_list[i - 1]
        cost = info["cost"]
        calories = info["calories"]
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    # Backtracking to find which items were selected
    w = budget
    selected = []
    for i in range(n, 0, -1):
        name, info = item_list[i - 1]
        cost = info["cost"]
        if dp[i][w] != dp[i - 1][w]:
            selected.append(name)
            w -= cost  # Reduce the remaining budget

    selected.reverse()  # Reverse to restore the original order

    total_calories = dp[n][budget]
    total_cost = sum(items[name]["cost"] for name in selected)

    return selected, total_cost, total_calories


def main():
    # Define a budget for the selection problem
    budget = 100
    print("Budget:", budget)

    # Greedy algorithm solution
    selected_greedy, cost_greedy, cal_greedy = greedy_algorithm(items, budget)
    print("\nGreedy Algorithm Result:")
    print("Selected items:", selected_greedy)
    print("Total cost:", cost_greedy)
    print("Total calories:", cal_greedy)

    # Dynamic programming solution
    selected_dp, cost_dp, cal_dp = dynamic_programming(items, budget)
    print("\nDynamic Programming Result:")
    print("Selected items:", selected_dp)
    print("Total cost:", cost_dp)
    print("Total calories:", cal_dp)


if __name__ == "__main__":
    main()
