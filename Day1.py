

with open('Day1Input.txt') as file:
    lines = file.readlines()
    left_list = []
    right_list = []
    for line in lines:
        whitespace = line.find(' ')
        left, right = line[:whitespace].strip(), line[whitespace+1:].strip()
        left_list.append(left)
        right_list.append(right)
    left_list.sort()
    right_list.sort()
    distance = 0
    for i in range(0, len(left_list)):
        distance += abs(int(left_list[i]) - int(right_list[i]))
        print(f"Total distance is {distance}")

    results_hash = {}

    for i in left_list:
        if i not in results_hash:
            results_hash[i] = right_list.count(i)
    sim_score = 0

    for key, value in results_hash.items():
        sim_score += int(key) * int(value)
    print(f"Similarity score is {sim_score}")



