import random
import matplotlib.pyplot as plt

def monte_carlo_dice_simulation(num_simulations=1000000):
    # Initialize frequency counter for sums 2 through 12
    frequency = {s: 0 for s in range(2, 13)}
    
    # Run the simulation
    for _ in range(num_simulations):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice_sum = dice1 + dice2
        frequency[dice_sum] += 1

    # Calculate probabilities for each sum (as percentages)
    probabilities = {s: (frequency[s] / num_simulations) * 100 for s in frequency}
    return frequency, probabilities

def print_probability_table(probabilities):
    print("Sum\tProbability")
    for s in sorted(probabilities.keys()):
        print(f"{s}\t{probabilities[s]:.2f}%")

def plot_probabilities(probabilities):
    sums = sorted(probabilities.keys())
    prob_values = [probabilities[s] for s in sums]
    
    plt.figure(figsize=(8, 5))
    bars = plt.bar(sums, prob_values, color='blue', alpha=0.7)
    plt.xlabel("Sum of Two Dice")
    plt.ylabel("Probability (%)")
    plt.title("Monte Carlo Simulation of Dice Sum Probabilities")
    plt.xticks(sums)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Add actual percentage values on top of each bar
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval, f'{yval:.2f}%', 
                 ha='center', va='bottom', fontsize=10)
    
    plt.show()

def main():
    num_simulations = 1000000

    _, probabilities = monte_carlo_dice_simulation(num_simulations)
    
    print_probability_table(probabilities)
    
    plot_probabilities(probabilities)

if __name__ == "__main__":
    main()
