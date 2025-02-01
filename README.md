# Monte Carlo Dice Simulation vs Analytical Probability

## Introduction
This project simulates rolling two six-sided dice using the Monte Carlo method. The goal is to compare the probabilities obtained from the simulation with the theoretical probabilities calculated analytically.

## Analytical Probability
In an ideal scenario, each sum (from 2 to 12) has a well-defined probability based on the number of ways it can be obtained from two dice:

| Sum | Probability (%) | Fraction |
|----|----------------|----------|
| 2  | 2.78%         | (1/36)   |
| 3  | 5.56%         | (2/36)   |
| 4  | 8.33%         | (3/36)   |
| 5  | 11.11%        | (4/36)   |
| 6  | 13.89%        | (5/36)   |
| 7  | 16.67%        | (6/36)   |
| 8  | 13.89%        | (5/36)   |
| 9  | 11.11%        | (4/36)   |
| 10 | 8.33%         | (3/36)   |
| 11 | 5.56%         | (2/36)   |
| 12 | 2.78%         | (1/36)   |

These probabilities arise because some sums have more possible dice combinations:
- **Sum = 2** (only possible with `1+1`)
- **Sum = 7** (most frequent, possible with `1+6, 2+5, 3+4, 4+3, 5+2, 6+1`)

## Monte Carlo Simulation Results
After running **1,000,000 dice rolls**, we obtained the following estimated probabilities:

| Sum | Monte Carlo Probability (%) |
|----|-----------------------------|
| 2  | 2.79% |
| 3  | 5.56% |
| 4  | 8.34% |
| 5  | 11.14% |
| 6  | 13.90% |
| 7  | 16.65% |
| 8  | 13.86% |
| 9  | 11.09% |
| 10 | 8.36% |
| 11 | 5.55% |
| 12 | 2.75% |

## Conclusion
1. The Monte Carlo simulation results closely approximate the analytical values.
2. Small deviations are expected due to randomness, but as the number of simulations increases, the results converge toward the theoretical probabilities.
3. The largest difference between the analytical and simulated probabilities is expected to be within a small margin due to statistical variance.

Overall, the Monte Carlo method provides an effective way to approximate probability distributions when analytical calculations are difficult or impossible.
