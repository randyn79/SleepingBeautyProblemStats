import random

def coin_flip():
    options = ('Heads', 'Tails')
    outcome = random.choice(options)
    return outcome

def interview(iterations):

    flip_counts = {'Monday Heads': 0,
                   'Monday Tails': 0,
                   'Tuesday Heads': 0,
                   'Tuesday Tails': 0
                   }

    for i in range(iterations):
        outcome = coin_flip()

        if outcome == 'Heads':
            flip_counts['Monday Heads'] += 1
            continue

        if outcome == 'Tails':
            flip_counts['Monday Tails'] += 1

            outcome = coin_flip()

            if outcome == 'Heads':
                flip_counts['Tuesday Heads'] += 1
                continue

            if outcome == 'Tails':
                flip_counts['Tuesday Tails'] += 1
                continue
        
    return flip_counts

def statistics(flip_counts, iterations):

    flip_stats = {}

    # Percentage of each result to iterations
    flip_stats['Monday Heads Pct'] = round(flip_counts['Monday Heads'] / iterations * 100, 2)
    flip_stats['Monday Tails Pct'] = round(flip_counts['Monday Tails'] / iterations * 100, 2)
    flip_stats['Tuesday Heads Pct'] = round(flip_counts['Tuesday Heads'] / iterations * 100, 2)
    flip_stats['Tuesday Tails Pct'] = round(flip_counts['Tuesday Tails'] / iterations * 100, 2)

    # Percentage of each result on Tuesday iterations
    flip_stats['Tuesday Iteration Heads Pct'] = round(flip_counts['Tuesday Heads'] / flip_counts['Monday Tails'] * 100, 2)
    flip_stats['Tuesday Iteration Tails Pct'] = round(flip_counts['Tuesday Tails'] /flip_counts['Monday Tails'] * 100, 2)

    # Percentages of totals to total flips
    flip_stats['Total Flips'] = sum(flip_counts.values())
    flip_stats['Total Heads'] = flip_counts['Monday Heads'] + flip_counts['Tuesday Heads']
    flip_stats['Total Tails'] = flip_counts['Monday Tails'] + flip_counts['Tuesday Tails']
    flip_stats['Total Heads Pct'] = round(flip_stats['Total Heads'] / flip_stats['Total Flips'] * 100, 2)
    flip_stats['Total Tails Pct'] = round(flip_stats['Total Tails'] / flip_stats['Total Flips'] * 100, 2)

    # Percentage of individual results to total flips
    flip_stats['Monday Heads to Total Flips Pct'] = round(flip_counts['Monday Heads'] / flip_stats['Total Flips'] * 100,2)
    flip_stats['Monday Tails to Total Flips Pct'] = round(flip_counts['Monday Tails'] / flip_stats['Total Flips'] * 100, 2)
    flip_stats['Tuesday Heads to Total Flips Pct'] = round(flip_counts['Tuesday Heads'] / flip_stats['Total Flips'] * 100, 2)
    flip_stats['Tuesday Tails to Total Flips Pct'] = round(flip_counts['Tuesday Tails'] / flip_stats['Total Flips'] * 100, 2)

    return flip_stats

def main(iterations):
    flip_counts = interview(iterations)
    print(flip_counts)
    flip_stats = statistics(flip_counts, iterations)
    print(flip_stats)
    

if __name__ == "__main__":
    num_iterations = int(input('How many iterations would you like to run?  '))
    main(num_iterations)
    
    
