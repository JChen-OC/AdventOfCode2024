def parse_input(file_path):
    with open(file_path) as file:
        data = list(map(int, file.read().split()))
    return data

def calculate_sums(data): 
    totals = []
    left_list = sorted(data[0::2])
    right_list = sorted(data[1::2])

    absolute_value = sum(abs(left_number - right_number) for left_number, right_number in zip(left_list, right_list))
    totals.append(absolute_value)

    return sum(totals)

def calculate_similarity_score(data):
    left_list = sorted(data[0::2])
    right_list = sorted(data[1::2])

    similarity_score = sum( left_number * right_list.count(left_number) for left_number in left_list)
    return similarity_score

# data = parse_input("inputs/day1.txt")
# print(calculate_sums(data))
# print(calculate_similarity_score(data))
