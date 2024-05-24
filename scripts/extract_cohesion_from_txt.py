import re

percentages = []
task_number = 0
with open('cc_ground_truth.txt', 'r') as file:
    for line in file:
        match = re.search(r'Total: (\d+\.\d+)%', line)
        if match:
            percentages.append(f"Task {task_number}: {float(match.group(1))}%")
            task_number += 1

for percentage in percentages:
    print(percentage)