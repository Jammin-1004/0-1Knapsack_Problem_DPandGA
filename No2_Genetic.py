import random
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

# GA Algorithm 
def solve_ga(capacity, items, pop_size=200, generations=1000, mutation_rate=0.01):
    n = len(items)

    ratio_order = sorted(range(n), key=lambda i: items[i]['profit'] / items[i]['weight'])

    def repair(chromosome):
        total_weight = sum(items[i]['weight'] for i in range(n) if chromosome[i] == 1)
        if total_weight <= capacity:
            return chromosome
        for i in ratio_order:
            if chromosome[i] == 1:
                chromosome[i] = 0
                total_weight -= items[i]['weight']
                if total_weight <= capacity:
                    break
        return chromosome

    def fitness(chromosome):
        return sum(items[i]['profit'] for i in range(n) if chromosome[i] == 1)

    start_time = time.time()

    population = []
    for _ in range(pop_size):
        chrom = [random.randint(0, 1) for _ in range(n)]
        population.append(repair(chrom))

    best_chromosome = None
    best_fitness = -1

    for _ in range(generations):
        fitness_scores = [fitness(ind) for ind in population]

        current_best_idx = fitness_scores.index(max(fitness_scores))
        if fitness_scores[current_best_idx] > best_fitness:
            best_fitness = fitness_scores[current_best_idx]
            best_chromosome = population[current_best_idx][:]

        total_fitness = sum(fitness_scores)
        if total_fitness == 0:
            probs = [1 / pop_size] * pop_size
        else:
            probs = [f / total_fitness for f in fitness_scores]

        new_population = [best_chromosome[:]] 

        while len(new_population) < pop_size:
            p1, p2 = random.choices(population, weights=probs, k=2)
            crossover_point = random.randint(1, n - 1)
            child = p1[:crossover_point] + p2[crossover_point:]

            for i in range(n):
                if random.random() < mutation_rate:
                    child[i] = 1 - child[i]

            child = repair(child)
            new_population.append(child)

        population = new_population

    selected_items = [items[i]['id'] for i in range(n) if best_chromosome[i] == 1]
    execution_time = time.time() - start_time

    return best_fitness, selected_items, execution_time

# Main
if __name__ == "__main__":
    file_path = "TestData(0-1Knapsack)_500.txt" 

    try:
        cap, item_list = parse_knapsack_data(file_path)
        print(f"[{len(item_list)} Load] Bag Capacity: {cap}")

        profit, items, exec_time = solve_ga(cap, item_list, pop_size=200, generations=1000, mutation_rate=0.01)

        print("\n===GA Method===")
        print(f"MAX Value: {profit}")
        if len(items) <= 50:
            print(f"Select Item: {items}")
        else:
            print(f"How much select Item : {len(items)}")
        print(f"Run time: {exec_time:.4f} s")

    except FileNotFoundError:
        print("Check File Path")